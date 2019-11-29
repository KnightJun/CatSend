#coding:utf-8
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import os
import re
import time
from main_ui import Ui_MainWindow
from load_ui import Ui_LoadWindow
from PyQt5 import QtWidgets, QtCore, QtGui,Qt

def loadScapy():
    global Scapy_Exception,IFACES,sendp,conf,PcapReader, rdpcap
    from scapy.error import Scapy_Exception
    from scapy.all import IFACES,sendp
    from scapy.config import conf
    from scapy.utils import PcapReader, rdpcap

def isValidIP(ip):
    return re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)
    
def isValidMac(mac):
    return re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac)

def isMulticastMac(mac):
    return int(mac[0:2],16) & 1

def isMulticastIP(ip):
    return int(ip[0:3]) >= 224

def get_netcard():
    netcard_info = []
    for iface_name in sorted(IFACES.data):
        dev = IFACES.data[iface_name]
        mac = dev.mac
        if not mac or dev.is_invalid():
            continue
        netcard_info.append([str(dev.name), str(dev.ip), dev.mac])
    return netcard_info

class load_Form(QtWidgets.QMainWindow, Ui_LoadWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        super(Ui_LoadWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.startTimer(500, timerType = QtCore.Qt.VeryCoarseTimer)

    def timerEvent(self, event):
        loadScapy()
        self.close()

class main_Form(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.netcardList = get_netcard()
        self.pktItems = []
        self.isSending = False
        self.shouldStop = False
        self.on_btnReload_clicked()
        self.cmbNetCard.clear()
        self.cmbNetCard.addItems([ "%-16s%s" % (x[1], x[0]) for x in self.netcardList])
        

    def on_btnReload_clicked(self, isbool = None):
        if isbool != None:
            return
        self.packetList = {}
        self.pktItems.clear()
        list_dir = [x[:-5] for x in os.listdir("./packets") if x[-5:] == ".pcap"]
        for filename in list_dir:
            try:
                packets = rdpcap("./packets/" + filename + ".pcap")
                self.packetList[filename] = packets[0]
            except Scapy_Exception as identifier:
                print("./packets/" + filename + ".pcap", identifier)
        
        for pktname in self.packetList.keys():
            item = QtWidgets.QListWidgetItem(pktname)
            item.setCheckState(QtCore.Qt.Checked)
            item.setHidden(True)
            self.pktItems.append((pktname, item))
        self.listPkt.clear()
        [self.listPkt.addItem(item[1]) for item in self.pktItems]
        self.on_listPkt_itemChanged(None)
        return

    def on_listPkt_currentItemChanged(self, item : QtWidgets.QListWidgetItem, item_pre : QtWidgets.QListWidgetItem):
        if item:
            p = (self.packetList[item.text()])
            self.edtInfo.setText("Packet Size:%d\n%s" % (len(p), p.show(dump=True)))

    def on_listPkt_itemChanged(self, item):
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
            if self.cboxRepeat.checkState():
                self.SendProgress.setMaximum(1)
                self.SendProgress.setValue(0)
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
        [item[1].setCheckState(QtCore.Qt.Checked) for item in self.pktItems if not item[1].isHidden()]
            
    def on_btnCheckInv_clicked(self, isbool = None):
        if isbool == None:
            return
        for item in self.pktItems:
            if not item[1].isHidden():
                item = item[1]
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
                if self.cboxNoChangeBroad.checkState():
                    if not isMulticastMac(pkt["Ether"].dst):
                        pkt["Ether"].dst = dstMac 
                else:
                    pkt["Ether"].dst = dstMac 
            if pkt.haslayer("IP"):
                if self.cbxSrcIP.checkState() and isValidIP(srcIP):
                    pkt["IP"].src = srcIP
                if self.cbxDstIP.checkState() and isValidIP(dstIP):
                    if self.cboxNoChangeBroad.checkState():
                        if not isMulticastIP(pkt["IP"].dst):
                            pkt["IP"].dst = dstIP
                        else:
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
        if self.cboxRepeat.checkState():
            self.SendProgress.setMaximum(0)
            self.SendProgress.setValue(0)
            sendLoop = sys.maxsize
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
            if not self.cboxRepeat.checkState():
                self.SendProgress.setValue(loopInx + 1)
            if self.shouldStop:
                break
        self.isSending = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    lf = load_Form()
    lf.show()
    app.exec_()
    my_pyqt_form = main_Form()
    my_pyqt_form.show()
    app.exec_()
