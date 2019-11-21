#coding:utf-8
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import os
import re
import time
from main_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from scapy.error import Scapy_Exception
from scapy.all import IFACES,sendp
from scapy.config import conf
from scapy.utils import PcapReader, rdpcap

def isValidIP(ip):
    return re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)
    
def isValidMac(mac):
    return re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac)

def get_netcard():
    netcard_info = []
    for iface_name in sorted(IFACES.data):
        dev = IFACES.data[iface_name]
        mac = dev.mac
        if not mac or dev.is_invalid():
            continue
        netcard_info.append([str(dev.name), str(dev.ip), dev.mac])
    return netcard_info

def get_packetList():
    packetList = {}
    list_dir = [x[:-5] for x in os.listdir("./packets") if x[-5:] == ".pcap"]
    for filename in list_dir:
        try:
            packets = rdpcap("./packets/" + filename + ".pcap")
            packetList[filename] = packets[0]
        except Scapy_Exception as identifier:
            print("./packets/" + filename + ".pcap", identifier)
    return packetList

class main_Form(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        self.netcardList = get_netcard()
        self.pktItems = []
        self.isSending = False
        self.shouldStop = False
        self.packetList = get_packetList()
        self.setupUi(self)
        self.cmbNetCard.clear()
        self.cmbNetCard.addItems([ "%-16s%s" % (x[1], x[0]) for x in self.netcardList])
        for pktname in self.packetList.keys():
            item = QtWidgets.QListWidgetItem(pktname)
            item.setCheckState(QtCore.Qt.Checked)
            item.setHidden(True)
            self.pktItems.append((pktname, item))
        self.listPkt.clear()
        [self.listPkt.addItem(item[1]) for item in self.pktItems]
        

    def on_listPkt_currentItemChanged(self, item : QtWidgets.QListWidgetItem, item_pre : QtWidgets.QListWidgetItem):
        p = (self.packetList[item.text()])
        self.edtInfo.setText("Packet Size:%d\n%s" % (len(p), p.show(dump=True)))

    def on_listPkt_itemChanged(self, item : QtWidgets.QListWidgetItem):
        self.lblCount.setText("已选%d/%d" % (len([ pkt for pkt in self.pktItems if pkt[1].checkState() ]), len(self.pktItems)))

    def on_btnGetNCMac_clicked(self, isbool = None):
        if isbool == None:
            return
        self.edtSrcMac.setText(self.netcardList[self.cmbNetCard.currentIndex()][2])
        self.edtSrcIP.setText(self.netcardList[self.cmbNetCard.currentIndex()][1])

    def on_btnSend_clicked(self, isbool = None):
        if isbool == None:
            return
        sendPktList = []
        if self.btnSend.text() == "开始发包" and self.isSending:
            return
        if self.btnSend.text() == "停止发包":
            self.shouldStop = True
            self.btnSend.setText("开始发包")
            return
        self.btnSend.setText("停止发包")
        self.sendPackets()
        self.btnSend.setText("开始发包")

    def on_edtSrcMac_textChanged(self, text):
        self.edtSrcMac.setStyleSheet("" if isValidMac(text) else "color:red")

    def on_edtDstMac_textChanged(self, text):
        self.edtDstMac.setStyleSheet("" if isValidMac(text) else "color:red")

    def on_edtSrcIP_textChanged(self, text):
        self.edtSrcIP.setStyleSheet("" if isValidIP(text) else "color:red")

    def on_edtDstIP_textChanged(self, text):
        self.edtDstIP.setStyleSheet("" if isValidIP(text) else "color:red")

    def on_btnCheckAll_clicked(self, isbool = None):
        if isbool == None:
            return
        [item.setCheckState(QtCore.Qt.Checked) for item in self.pktItems]
            
    def on_btnCheckInv_clicked(self, isbool = None):
        if isbool == None:
            return
        for item in self.pktItems:
            item.setCheckState(QtCore.Qt.Unchecked if item.checkState() else QtCore.Qt.Checked)

    def on_edtFilter_textChanged(self, text):
        [item[1].setHidden(bool(text and text not in item[0])) for item in self.pktItems]

    def constructPacketList(self):
        PktList = []
        srcMac = self.edtSrcMac.text()
        dstMac = self.edtDstMac.text()
        srcIP = self.edtSrcIP.text()
        dstIP = self.edtDstIP.text()
        for i in range(self.listPkt.count()):
            if self.listPkt.item(i).checkState() == False:
                continue
            pkt = self.packetList[self.listPkt.item(i).text()].copy()
            if self.cbxSrcMac.checkState() and isValidMac(srcMac):
                pkt["Ether"].src = srcMac
            if self.cbxDstMac.checkState() and isValidMac(dstMac):
                pkt["Ether"].dst = dstMac
            if pkt.haslayer("IP"):
                if self.cbxSrcIP.checkState() and isValidIP(srcIP):
                    pkt["IP"].src = srcIP
                if self.cbxDstIP.checkState() and isValidIP(dstIP):
                    pkt["IP"].dst = dstIP
            PktList.append(pkt)
        return PktList

    def sendPackets(self):
        self.isSending = True
        self.shouldStop = False
        PktList = self.constructPacketList()
        sendNetcard = self.netcardList[self.cmbNetCard.currentIndex()][0]
        socket = conf.L2socket(iface=sendNetcard)
        sendInvterval = int(self.edtInter.text()) / 1000 if self.edtInter.text().isdigit() else 0
        sendLoop = int(self.edtLoop.text()) if self.edtLoop.text().isdigit() else 1
        self.SendProgress.setMaximum(sendLoop)
        now_time = time.time()
        old_time = now_time
        pktCount = 0
        old_pktCount = pktCount
        pktRate = 0
        for loopInx in range(sendLoop):
            QtWidgets.QApplication.processEvents()
            for pkt in PktList:
                socket.send(pkt)
                pktCount += 1
                time.sleep(sendInvterval)
                if pktCount % 100 == 0:
                    now_time = time.time()
                    pktRate = int((pktCount - old_pktCount) / (now_time - old_time))
                self.lblSendStatus.setText("已发:%d  %d/s" % (pktCount, pktRate))
                if self.shouldStop:
                    break
            self.SendProgress.setValue(loopInx + 1)
            if self.shouldStop:
                break
        self.isSending = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = main_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())