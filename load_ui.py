# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\loading.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadWindow(object):
    def setupUi(self, LoadWindow):
        LoadWindow.setObjectName("LoadWindow")
        LoadWindow.resize(409, 148)
        LoadWindow.setStyleSheet("background-color: rgb(0, 120, 215);")
        self.centralwidget = QtWidgets.QWidget(LoadWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        LoadWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadWindow)

    def retranslateUi(self, LoadWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadWindow.setWindowTitle(_translate("LoadWindow", "Loading..."))
        self.label.setText(_translate("LoadWindow", "CatSend"))
