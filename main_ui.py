# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 515)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnCheckAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheckAll.setObjectName("btnCheckAll")
        self.gridLayout.addWidget(self.btnCheckAll, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cmbNetCard = QtWidgets.QComboBox(self.groupBox)
        self.cmbNetCard.setObjectName("cmbNetCard")
        self.gridLayout_3.addWidget(self.cmbNetCard, 1, 1, 1, 3)
        self.edtInter = QtWidgets.QLineEdit(self.groupBox)
        self.edtInter.setStyleSheet("")
        self.edtInter.setObjectName("edtInter")
        self.gridLayout_3.addWidget(self.edtInter, 7, 1, 1, 1)
        self.cbxSrcIP = QtWidgets.QCheckBox(self.groupBox)
        self.cbxSrcIP.setObjectName("cbxSrcIP")
        self.gridLayout_3.addWidget(self.cbxSrcIP, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)
        self.edtDstMac = QtWidgets.QLineEdit(self.groupBox)
        self.edtDstMac.setEnabled(False)
        self.edtDstMac.setObjectName("edtDstMac")
        self.gridLayout_3.addWidget(self.edtDstMac, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 7, 2, 1, 1)
        self.cbxDstIP = QtWidgets.QCheckBox(self.groupBox)
        self.cbxDstIP.setObjectName("cbxDstIP")
        self.gridLayout_3.addWidget(self.cbxDstIP, 4, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtInfo = QtWidgets.QTextEdit(self.groupBox_2)
        self.edtInfo.setReadOnly(True)
        self.edtInfo.setObjectName("edtInfo")
        self.horizontalLayout.addWidget(self.edtInfo)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 4)
        self.edtLoop = QtWidgets.QLineEdit(self.groupBox)
        self.edtLoop.setObjectName("edtLoop")
        self.gridLayout_3.addWidget(self.edtLoop, 7, 3, 1, 1)
        self.btnSend = QtWidgets.QPushButton(self.groupBox)
        self.btnSend.setObjectName("btnSend")
        self.gridLayout_3.addWidget(self.btnSend, 8, 0, 1, 4)
        self.edtSrcIP = QtWidgets.QLineEdit(self.groupBox)
        self.edtSrcIP.setEnabled(False)
        self.edtSrcIP.setObjectName("edtSrcIP")
        self.gridLayout_3.addWidget(self.edtSrcIP, 4, 1, 1, 1)
        self.btnGetNCMac = QtWidgets.QPushButton(self.groupBox)
        self.btnGetNCMac.setObjectName("btnGetNCMac")
        self.gridLayout_3.addWidget(self.btnGetNCMac, 1, 0, 1, 1)
        self.edtDstIP = QtWidgets.QLineEdit(self.groupBox)
        self.edtDstIP.setEnabled(False)
        self.edtDstIP.setObjectName("edtDstIP")
        self.gridLayout_3.addWidget(self.edtDstIP, 4, 3, 1, 1)
        self.cbxDstMac = QtWidgets.QCheckBox(self.groupBox)
        self.cbxDstMac.setObjectName("cbxDstMac")
        self.gridLayout_3.addWidget(self.cbxDstMac, 2, 2, 1, 1)
        self.cbxSrcMac = QtWidgets.QCheckBox(self.groupBox)
        self.cbxSrcMac.setMaximumSize(QtCore.QSize(500, 16777215))
        self.cbxSrcMac.setObjectName("cbxSrcMac")
        self.gridLayout_3.addWidget(self.cbxSrcMac, 2, 0, 1, 1)
        self.edtSrcMac = QtWidgets.QLineEdit(self.groupBox)
        self.edtSrcMac.setEnabled(False)
        self.edtSrcMac.setObjectName("edtSrcMac")
        self.gridLayout_3.addWidget(self.edtSrcMac, 2, 1, 1, 1)
        self.SendProgress = QtWidgets.QProgressBar(self.groupBox)
        self.SendProgress.setMaximum(100)
        self.SendProgress.setProperty("value", -1)
        self.SendProgress.setTextVisible(True)
        self.SendProgress.setObjectName("SendProgress")
        self.gridLayout_3.addWidget(self.SendProgress, 9, 0, 1, 3)
        self.lblSendStatus = QtWidgets.QLabel(self.groupBox)
        self.lblSendStatus.setText("")
        self.lblSendStatus.setObjectName("lblSendStatus")
        self.gridLayout_3.addWidget(self.lblSendStatus, 9, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 3, 3, 1)
        self.btnCheckInv = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheckInv.setObjectName("btnCheckInv")
        self.gridLayout.addWidget(self.btnCheckInv, 2, 1, 1, 1)
        self.listPkt = QtWidgets.QListWidget(self.centralwidget)
        self.listPkt.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listPkt.setObjectName("listPkt")
        self.gridLayout.addWidget(self.listPkt, 1, 0, 1, 3)
        self.edtFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.edtFilter.setMaximumSize(QtCore.QSize(250, 16777215))
        self.edtFilter.setObjectName("edtFilter")
        self.gridLayout.addWidget(self.edtFilter, 0, 0, 1, 3)
        self.lblCount = QtWidgets.QLabel(self.centralwidget)
        self.lblCount.setText("")
        self.lblCount.setObjectName("lblCount")
        self.gridLayout.addWidget(self.lblCount, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.cbxSrcMac.clicked['bool'].connect(self.edtSrcMac.setEnabled)
        self.cbxSrcIP.toggled['bool'].connect(self.edtSrcIP.setEnabled)
        self.cbxDstMac.toggled['bool'].connect(self.edtDstMac.setEnabled)
        self.cbxDstIP.toggled['bool'].connect(self.edtDstIP.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "发包工具"))
        self.btnCheckAll.setText(_translate("MainWindow", "全选"))
        self.groupBox.setTitle(_translate("MainWindow", "发包设置"))
        self.edtInter.setText(_translate("MainWindow", "0"))
        self.cbxSrcIP.setText(_translate("MainWindow", "源IP"))
        self.label.setText(_translate("MainWindow", "发包间隔(ms)："))
        self.label_2.setText(_translate("MainWindow", "循环次数："))
        self.cbxDstIP.setText(_translate("MainWindow", "目的IP"))
        self.groupBox_2.setTitle(_translate("MainWindow", "报文原始信息"))
        self.edtLoop.setText(_translate("MainWindow", "1"))
        self.btnSend.setText(_translate("MainWindow", "开始发包"))
        self.btnGetNCMac.setText(_translate("MainWindow", "填充源信息"))
        self.cbxDstMac.setText(_translate("MainWindow", "目的Mac"))
        self.cbxSrcMac.setText(_translate("MainWindow", "源Mac"))
        self.btnCheckInv.setText(_translate("MainWindow", "反选"))
        self.edtFilter.setPlaceholderText(_translate("MainWindow", "Filter"))
