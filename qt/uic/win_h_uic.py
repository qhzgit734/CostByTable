# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_h_uic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(593, 554)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.commandLinkButton = QCommandLinkButton(Form)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout.addWidget(self.commandLinkButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"help", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">CostByTable</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">---------------help---------------</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u514d\u8d23\u58f0\u660e:\u672c\u8f6f\u4ef6\u4ec5\u4f9b\u5b66\u4e60\u4f7f\u7528\uff0c\u4e25\u7981\u5546\u7528\u3002\u82e5\u5546\u7528\u4ea7\u751f\u4e00\u5207\u8fdd\u6cd5\u540e\u679c\u4e0e\u672c\u4eba\u65e0\u5173\uff01</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53'; font-weight:600;\">\u4e00\u3001\u516c\u5171</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">1\u3001\u5bfc\u51fa\u6587\u4ef6\u5c06\u8986\u76d6\u539f\u6587\u4ef6\uff0c\u8bf7\u6ce8"
                        "\u610f\u5907\u4efd\u3002\u5bfc\u51fa</span> <span style=\" font-family:'\u5b8b\u4f53';\">'\u7ed3\u679c.xlsx'\u65f6\uff0c\u4f1a\u6309\u76ee\u6807\u6587\u4ef6\u6807\u7b7e\u9875\u540d\u79f0\u81ea\u52a8\u8ffd\u52a0\u6807\u7b7e\u9875</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u3001\u6e90\u76ee\u5f55\u6307\u9009\u4e2dexcel\u6587\u4ef6\u5bf9\u5e94\u76ee\u5f55</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">3\u3001\u6e05\u5355\u6570\u636e\u533a\u57df\u4e2d\uff0c\u6240\u6709\u6570\u636e\u586b\u5168\uff0c\u65e0\u7684\u60c5\u51b5\u586b'0'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4\u3001'\u4f9d\u636e'\u6307excel\u6587\u4ef6\u7b2c\u4e00\u884c\u6807\u9898\u884c,\u5fc5\u987b\u4e3a\u4e24\u4e2aexcel\u5171\u6709\u7684"
                        "\u6807\u9898</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53'; font-weight:600;\">\u4e8c\u3001\u6570\u636e\u5e93\u6587\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">1\u3001\u6570\u636e\u5e93\u7684excel\u6587\u4ef6\u53ef\u4ee5\u628a\u6240\u6709\u5355\u4f4d\u5de5\u7a0b\u7684\u90fd\u590d\u5236\u8fdb\u53bb\uff0c\u82e5\u6709\u91cd\u590d'\u5339\u914d\u4f9d\u636e'\uff08\u793a\u4f8b\uff1a\u9879\u76ee\u540d\u79f0\u53ca\u7279\u5f81\u63cf\u8ff0\u4e2d\u91cd\u590d\u6e05\u5355\u9879\uff09\u5b58\u5728\uff0c\u8f6f\u4ef6\u81ea\u52a8\u9009\u7b2c\u4e00\u6761\u5339\u914d\u7684\u6e05\u5355</span> </p>\n"
"<p style="
                        "\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">2\u3001'\u6570\u636e\u5e93-\u5904\u7406-\u5bfc\u51fa'\u4e3a\u6839\u636e\u4f9d\u636e\u9879\u53bb\u7a7a\u503c\u3001\u53bb\u91cd\u590d\u540e\u7684\u6570\u636e\u5e93\u6587\u4ef6\uff0c\u5bfc\u51fa\u5230\u6e90\u76ee\u5f55</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">3\u3001'\u6570\u636e\u5e93-\u5904\u7406-\u5bfc\u51fa'\u65f6\uff0c\u5148\u5229\u7528'\u5339\u914d\u4f9d\u636e'\u9009\u4e2d\u4f9d\u636e\uff0c\u518d\u70b9\u51fb'\u786e\u8ba4'\u751f\u6210\u53bb\u7a7a\u503c\u4f9d\u636e\u3002\u53bb\u91cd\u590d\u4f9d\u636e\u7684\u751f\u6210\u540c\u4e0a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u5b8b\u4f53';\"><"
                        "br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53'; font-weight:600;\">\u4e09\u3001\u76ee\u6807\u6587\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1<span style=\" font-family:'\u5b8b\u4f53';\">\u3001\u70b9\u51fb'\u590d\u7528\u6570\u636e'\u6309\u94ae\u540e\uff0c\u4f1a\u751f\u6210\u4e00\u4e2a'\u7ed3\u679c.xlsx'\u6587\u4ef6\u5230\u6e90\u76ee\u5f55\uff0c\u6587\u4ef6\u6309excel\u76ee\u6807\u6587\u4ef6'\u5339\u914d\u4f9d\u636e'\u987a\u5e8f\u6392\u5217\uff0c\u518d\u5c06\u5bf9\u5e94\u5185\u5bb9\u76f4\u63a5\u590d\u5236\u5230excel\u76ee\u6807\u6587\u4ef6\u4e2d\u5373\u53ef</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">2\u3001\u5339\u914d\u6570\u91cf\u8003\u8651'\u5339\u914d"
                        "\u4f9d\u636e'\u4e2d\u6240\u6709\u6e05\u5355\u9879\uff08'\u5339\u914d\u4f9d\u636e'\u5217\u7684\u7a7a\u503c\u4e0d\u53c2\u4e0e\u5339\u914d\uff09</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">by qhz734</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">20220910</span></p"
                        "></body></html>", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"\u8bbf\u95eeGITHUB", None))
    # retranslateUi

