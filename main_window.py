# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(877, 556)
        MainWindow.setMinimumSize(QtCore.QSize(859, 556))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("网络.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_3.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网络爬取"))
        self.label_3.setText(_translate("MainWindow", "操作日志："))
        self.textBrowser.setToolTip(_translate("MainWindow", "<html><head/><body><p>操作日志</p></body></html>"))
        self.label.setText(_translate("MainWindow", "输入你要爬取的页数："))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>此处输入数字</p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按钮开始爬取</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "开始爬取"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击此按钮查看文件</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "查看已爬取的文件"))
        self.label_6.setText(_translate("MainWindow", "斗鱼直播数据实时抓取"))
        self.label_5.setText(_translate("MainWindow", "爬取进度："))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>实时进度</p></body></html>"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>用户代理</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "user-agent："))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击可切换用户代理</p></body></html>"))
        self.comboBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "功能持续开发中..."))
        self.action_2.setText(_translate("MainWindow", "功能持续开发中..."))
        self.action_3.setText(_translate("MainWindow", "功能持续开发中..."))
