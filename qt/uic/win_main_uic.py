# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_main_uic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 607)
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 250))
        self.groupBox_2.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 50))
        self.label_10.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton_10 = QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_11.addWidget(self.checkBox)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 11, 11, 11)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_8.addWidget(self.label_8)

        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 50))
        self.listWidget.setMaximumSize(QSize(16777215, 80))
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.setFlow(QListView.LeftToRight)

        self.verticalLayout_8.addWidget(self.listWidget)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 250))
        self.groupBox.setMaximumSize(QSize(450, 16777215))
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(self.groupBox)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 426, 278))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(400, 16777215))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 50))
        self.label_9.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(100, 16777215))
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"\u5bfc\u5165")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 426, 278))
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_9.addWidget(self.label_13)

        self.pushButton_8 = QPushButton(self.page_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_9.addWidget(self.pushButton_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.label_14)

        self.pushButton_9 = QPushButton(self.page_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_10.addWidget(self.pushButton_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.toolBox.addItem(self.page_2, u"\u5904\u7406")

        self.verticalLayout.addWidget(self.toolBox)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(400, 16777215))
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(150, 0))
        self.label_17.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_13.addWidget(self.label_17)

        self.comboBox_4 = QComboBox(self.groupBox_5)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_13.addWidget(self.comboBox_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 50))
        self.label_18.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_18)


        self.gridLayout_3.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 150))

        self.gridLayout_3.addWidget(self.textBrowser, 5, 0, 1, 2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(350, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_14.addWidget(self.label_4)

        self.pushButton_11 = QPushButton(self.tab_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_14.addWidget(self.pushButton_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(300, 0))
        self.pushButton_7.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_14.addWidget(self.pushButton_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_14, 2, 0, 1, 2)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(400, 16777215))
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 0))
        self.label_16.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.label_16)

        self.comboBox_3 = QComboBox(self.groupBox_4)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_12.addWidget(self.comboBox_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 50))
        self.label_15.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_15)


        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_7.addWidget(self.label)

        self.listWidget_2 = QListWidget(self.frame)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMaximumSize(QSize(16777215, 50))
        self.listWidget_2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget_2.setFlow(QListView.LeftToRight)

        self.verticalLayout_7.addWidget(self.listWidget_2)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 905, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionhelp)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8868\u683c\u62a5\u4ef7", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u76ee\u6807\u6587\u4ef6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5730\u5740\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"excel\u6807\u7b7e\u9875:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u4f9d\u636e:", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8986\u76d6\u975e\u7a7a\u6570\u636e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u590d\u7528\u6570\u636e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f9d\u636e\uff1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\u6587\u4ef6\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e\u5e93\u6587\u4ef6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5730\u5740:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"excel\u6807\u7b7e\u9875:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u53bb\u7a7a\u503c\u4f9d\u636e:", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u53bb\u91cd\u590d\u9879\u4f9d\u636e:", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u901a\u7528\u529f\u80fd", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u65b0\u6e05\u5355:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u65b0\u6e05\u5355\u6587\u4ef6", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"excel\u6807\u7b7e\u9875\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5730\u5740:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u4f9d\u636e:", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u62a5\u544a\uff1a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u65e7\u6e05\u5355:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u65e7\u6e05\u5355\u6587\u4ef6", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"excel\u6807\u7b7e\u9875\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5730\u5740:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f9d\u636e:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6e05\u5355\u5bf9\u6bd4", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

