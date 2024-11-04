# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultadoTxtjEMruv.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_resultadoTxt(object):
    def setupUi(self, resultadoTxt):
        if not resultadoTxt.objectName():
            resultadoTxt.setObjectName(u"resultadoTxt")
        resultadoTxt.resize(481, 72)
        resultadoTxt.setStyleSheet(u"QLabel#lbArchivo,\n"
"QLabel#lbMensaje{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"QLabel{color: black;}\n"
"QFrame#frame{border-radius:12px}\n"
"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius:10px;\n"
"	background-color: rgb(50, 78, 173);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(73, 115, 253);\n"
"}")
        self.verticalLayout = QVBoxLayout(resultadoTxt)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(resultadoTxt)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.lbMensaje = QLabel(self.frame)
        self.lbMensaje.setObjectName(u"lbMensaje")
        self.lbMensaje.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_3.addWidget(self.lbMensaje, 1, 0, 1, 1)

        self.lbArchivo = QLabel(self.frame)
        self.lbArchivo.setObjectName(u"lbArchivo")

        self.gridLayout_3.addWidget(self.lbArchivo, 0, 0, 1, 1)

        self.lbX = QLabel(self.frame)
        self.lbX.setObjectName(u"lbX")
        self.lbX.setPixmap(QPixmap(u":/icons/resources/images/red_x.svg"))

        self.gridLayout_3.addWidget(self.lbX, 0, 3, 1, 1)

        self.leRutaTxt = QLineEdit(self.frame)
        self.leRutaTxt.setObjectName(u"leRutaTxt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leRutaTxt.sizePolicy().hasHeightForWidth())
        self.leRutaTxt.setSizePolicy(sizePolicy1)
        self.leRutaTxt.setReadOnly(True)

        self.gridLayout_3.addWidget(self.leRutaTxt, 0, 1, 1, 1)

        self.lbCheck = QLabel(self.frame)
        self.lbCheck.setObjectName(u"lbCheck")
        self.lbCheck.setPixmap(QPixmap(u":/icons/resources/images/check.svg"))

        self.gridLayout_3.addWidget(self.lbCheck, 0, 2, 1, 1)

        self.teMensajeTxt = QPlainTextEdit(self.frame)
        self.teMensajeTxt.setObjectName(u"teMensajeTxt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.teMensajeTxt.sizePolicy().hasHeightForWidth())
        self.teMensajeTxt.setSizePolicy(sizePolicy2)
        self.teMensajeTxt.setMinimumSize(QSize(0, 27))
        self.teMensajeTxt.setReadOnly(True)
        self.teMensajeTxt.setBackgroundVisible(False)

        self.gridLayout_3.addWidget(self.teMensajeTxt, 1, 1, 1, 1)

        self.btAbrir = QPushButton(self.frame)
        self.btAbrir.setObjectName(u"btAbrir")
        icon = QIcon()
        icon.addFile(u":/icons/resources/images/open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btAbrir.setIcon(icon)
        self.btAbrir.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btAbrir, 1, 2, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(resultadoTxt)

        QMetaObject.connectSlotsByName(resultadoTxt)
    # setupUi

    def retranslateUi(self, resultadoTxt):
        resultadoTxt.setWindowTitle(QCoreApplication.translate("resultadoTxt", u"Form", None))
        self.lbMensaje.setText(QCoreApplication.translate("resultadoTxt", u"Mensaje:", None))
        self.lbArchivo.setText(QCoreApplication.translate("resultadoTxt", u"Archivo.txt:", None))
        self.lbX.setText("")
        self.leRutaTxt.setPlaceholderText(QCoreApplication.translate("resultadoTxt", u"Sin Ruta.", None))
        self.lbCheck.setText("")
        self.teMensajeTxt.setPlaceholderText(QCoreApplication.translate("resultadoTxt", u"Sin mensaje.", None))
#if QT_CONFIG(tooltip)
        self.btAbrir.setToolTip(QCoreApplication.translate("resultadoTxt", u"Abrir Ubicaci\u00f3  Del Archivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btAbrir.setStatusTip(QCoreApplication.translate("resultadoTxt", u"Abrir Ubicaci\u00f3  Del Archivo.", None))
#endif // QT_CONFIG(statustip)
        self.btAbrir.setText("")
    # retranslateUi

