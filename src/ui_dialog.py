# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\dialog.ui'
#
# Created: Sat Apr 07 23:07:41 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(368, 393)
        self.verticalLayout = QtGui.QVBoxLayout(MainDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(MainDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 371, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 381, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 90, 251, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(60, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 190, 381, 16))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 210, 251, 81))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(70, 50, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.listView = QtGui.QListView(self.groupBox_3)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_4.addWidget(self.listView)
        self.widget = QtGui.QWidget(self.groupBox_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_dirbtn = QtGui.QPushButton(self.widget)
        self.add_dirbtn.setObjectName(_fromUtf8("add_dirbtn"))
        self.horizontalLayout.addWidget(self.add_dirbtn)
        self.del_dirbtn = QtGui.QPushButton(self.widget)
        self.del_dirbtn.setObjectName(_fromUtf8("del_dirbtn"))
        self.horizontalLayout.addWidget(self.del_dirbtn)
        self.verticalLayout_4.addWidget(self.widget)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.widget_2 = QtGui.QWidget(self.groupBox_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_6 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.capturebtn = QtGui.QPushButton(self.widget_2)
        self.capturebtn.setObjectName(_fromUtf8("capturebtn"))
        self.horizontalLayout_2.addWidget(self.capturebtn)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.widget_3 = QtGui.QWidget(self.groupBox_3)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_7 = QtGui.QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.downloadbtn = QtGui.QPushButton(self.widget_3)
        self.downloadbtn.setObjectName(_fromUtf8("downloadbtn"))
        self.horizontalLayout_3.addWidget(self.downloadbtn)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.savebtn = QtGui.QPushButton(MainDialog)
        self.savebtn.setObjectName(_fromUtf8("savebtn"))
        self.horizontalLayout_4.addWidget(self.savebtn)
        self.canclebtn = QtGui.QPushButton(MainDialog)
        self.canclebtn.setObjectName(_fromUtf8("canclebtn"))
        self.horizontalLayout_4.addWidget(self.canclebtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.action_start = QtGui.QAction(MainDialog)
        self.action_start.setObjectName(_fromUtf8("action_start"))
        self.action_stop = QtGui.QAction(MainDialog)
        self.action_stop.setObjectName(_fromUtf8("action_stop"))
        self.action_config = QtGui.QAction(MainDialog)
        self.action_config.setObjectName(_fromUtf8("action_config"))
        self.action_exit = QtGui.QAction(MainDialog)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_restart = QtGui.QAction(MainDialog)
        self.action_restart.setObjectName(_fromUtf8("action_restart"))
        self.action_about = QtGui.QAction(MainDialog)
        self.action_about.setObjectName(_fromUtf8("action_about"))

        self.retranslateUi(MainDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.savebtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainDialog.accept)
        QtCore.QObject.connect(self.canclebtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "JAVShell设置", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainDialog", "启动选项", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainDialog", "开机自动启动", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainDialog", "自动登录Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainDialog", "登录信息", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainDialog", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainDialog", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainDialog", "自动登录JAV", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainDialog", "登录信息", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainDialog", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainDialog", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainDialog", "系统设置", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainDialog", "存储位置", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainDialog", "录像路径：", None, QtGui.QApplication.UnicodeUTF8))
        self.add_dirbtn.setText(QtGui.QApplication.translate("MainDialog", "增加", None, QtGui.QApplication.UnicodeUTF8))
        self.del_dirbtn.setText(QtGui.QApplication.translate("MainDialog", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainDialog", "抓拍路径", None, QtGui.QApplication.UnicodeUTF8))
        self.capturebtn.setText(QtGui.QApplication.translate("MainDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainDialog", "下载路径", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadbtn.setText(QtGui.QApplication.translate("MainDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainDialog", "存储位置", None, QtGui.QApplication.UnicodeUTF8))
        self.savebtn.setText(QtGui.QApplication.translate("MainDialog", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.canclebtn.setText(QtGui.QApplication.translate("MainDialog", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.action_start.setText(QtGui.QApplication.translate("MainDialog", "启动", None, QtGui.QApplication.UnicodeUTF8))
        self.action_start.setToolTip(QtGui.QApplication.translate("MainDialog", "启动JAVClient", None, QtGui.QApplication.UnicodeUTF8))
        self.action_stop.setText(QtGui.QApplication.translate("MainDialog", "停止", None, QtGui.QApplication.UnicodeUTF8))
        self.action_stop.setToolTip(QtGui.QApplication.translate("MainDialog", "停止JAVClient", None, QtGui.QApplication.UnicodeUTF8))
        self.action_config.setText(QtGui.QApplication.translate("MainDialog", "显示配置", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainDialog", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setToolTip(QtGui.QApplication.translate("MainDialog", "退出JAVShell", None, QtGui.QApplication.UnicodeUTF8))
        self.action_restart.setText(QtGui.QApplication.translate("MainDialog", "重新启动", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("MainDialog", "关于JAVShell", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setToolTip(QtGui.QApplication.translate("MainDialog", "关于JAVShell", None, QtGui.QApplication.UnicodeUTF8))

import sharenet_rc