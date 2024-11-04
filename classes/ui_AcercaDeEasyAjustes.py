# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AcercaDeEasyAjusteshtjmRn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(474, 434)
        Dialog.setStyleSheet(u"QDialog{\n"
"background-color:rgb(25, 42, 63)\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QLabel#titulo{\n"
"font: 600 30pt \"Lucida Bright\";\n"
"}\n"
"QLabel#metaInfo{\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton#bt_linkedIn{\n"
"	border-radius:8px;\n"
"	font: 12pt \"Arial\";\n"
"	color:rgb(255, 255, 254);\n"
"	border:None;\n"
"	background-color: None;\n"
"}\n"
"QPushButton#bt_linkedIn:hover{\n"
"	border-radius:12px;\n"
"	font: 12pt \"Arial\";\n"
"	color:rgb(0,51, 102);\n"
"	background-color: white;\n"
"}\n"
"QFrame#frame{\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titulo)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 150))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.metaInfo = QLabel(self.frame)
        self.metaInfo.setObjectName(u"metaInfo")
        self.metaInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.metaInfo.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.metaInfo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.bt_linkedIn = QPushButton(self.frame)
        self.bt_linkedIn.setObjectName(u"bt_linkedIn")
        icon = QIcon()
        icon.addFile(u":/icons/resources/images/Linkedin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_linkedIn.setIcon(icon)
        self.bt_linkedIn.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bt_linkedIn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Acerca de Easy Ajustes", None))
        self.titulo.setText(QCoreApplication.translate("Dialog", u"Easy Ajustes", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"La aplicaci\u00f3n Easy Ajustes es una herramienta dise\u00f1ada para facilitar la creaci\u00f3n de ajustes, lo cual consiste en copiar archivos de un lugar y pegarlos en otro conservando parte del directorio original.\n"
"\n"
"Esta aplicaci\u00f3n se desarroll\u00f3 sin \u00e1nimo de lucro y cualquier comercio o cobro alrededor de la m\u00edsma, esta prohibido.", None))
        self.metaInfo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Nombre:</span><span style=\" font-size:11pt;\"> Easy Ajustes<br/></span><span style=\" font-size:11pt; font-weight:700;\">Versi\u00f3n:</span><span style=\" font-size:11pt;\"> 1.1.0.0<br/></span><span style=\" font-size:11pt; font-weight:700;\">Copyright: </span><span style=\" font-size:14pt;\">\u00a9 </span><span style=\" font-size:11pt;\">Jose Leonardo Villamizar Reyes<br/></span><span style=\" font-size:11pt; font-weight:700;\">\u00daltima revisi\u00f3n:</span><span style=\" font-size:11pt;\"> 25 de octubre del 2024<br/></span><span style=\" font-size:11pt; font-weight:700;\">Idioma:</span><span style=\" font-size:11pt;\"> Espa\u00f1ol (Espa\u00f1a, internacional)</span><span style=\" font-size:11pt;\"><br/></span><span style=\" font-size:11pt; font-weight:700;\">Desarrollado por:</span><span style=\" font-size:11pt;\"> Jose Leonardo Villamizar Reyes</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"LinkedIn", None))
        self.bt_linkedIn.setText(QCoreApplication.translate("Dialog", u"https://www.linkedin.com/in/joselvillamizar", None))
    # retranslateUi

