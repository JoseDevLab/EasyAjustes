# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultadoAjustenNDCbi.ui'
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

class Ui_resultadoAjuste(object):
    def setupUi(self, resultadoAjuste):
        if not resultadoAjuste.objectName():
            resultadoAjuste.setObjectName(u"resultadoAjuste")
        resultadoAjuste.resize(534, 106)
        resultadoAjuste.setStyleSheet(u"QLabel#lbOrigen,\n"
"QLabel#lbDestino,\n"
"QLabel#lbMensaje{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"QLabel#lbNumeracion{\n"
"	font: 9pt \"Roman\";\n"
"}\n"
"QLabel#lbNumeracion{border-radius:10px}\n"
"QLabel{color: black;}\n"
"QFrame#frame{border-radius:12px}\n"
"QPushButton{\n"
"	border-radius:10px;\n"
"	background-color: rgb(50, 78, 173);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(73, 115, 253);\n"
"}")
        self.verticalLayout = QVBoxLayout(resultadoAjuste)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(resultadoAjuste)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbCheck = QLabel(self.frame)
        self.lbCheck.setObjectName(u"lbCheck")
        self.lbCheck.setMaximumSize(QSize(50, 50))
        self.lbCheck.setPixmap(QPixmap(u":/icons/resources/images/check.png"))
        self.lbCheck.setScaledContents(True)

        self.gridLayout.addWidget(self.lbCheck, 0, 3, 2, 1)

        self.lbDestino = QLabel(self.frame)
        self.lbDestino.setObjectName(u"lbDestino")

        self.gridLayout.addWidget(self.lbDestino, 1, 1, 1, 1)

        self.lbOrigen = QLabel(self.frame)
        self.lbOrigen.setObjectName(u"lbOrigen")

        self.gridLayout.addWidget(self.lbOrigen, 0, 1, 1, 1)

        self.lbX = QLabel(self.frame)
        self.lbX.setObjectName(u"lbX")
        self.lbX.setMaximumSize(QSize(50, 50))
        self.lbX.setPixmap(QPixmap(u":/icons/resources/images/red_x.png"))
        self.lbX.setScaledContents(True)

        self.gridLayout.addWidget(self.lbX, 0, 4, 2, 1)

        self.lePathOrigen = QLineEdit(self.frame)
        self.lePathOrigen.setObjectName(u"lePathOrigen")
        self.lePathOrigen.setReadOnly(True)

        self.gridLayout.addWidget(self.lePathOrigen, 0, 2, 1, 1)

        self.lePathDestino = QLineEdit(self.frame)
        self.lePathDestino.setObjectName(u"lePathDestino")
        self.lePathDestino.setReadOnly(True)

        self.gridLayout.addWidget(self.lePathDestino, 1, 2, 1, 1)

        self.lbMensaje = QLabel(self.frame)
        self.lbMensaje.setObjectName(u"lbMensaje")
        self.lbMensaje.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.lbMensaje, 2, 1, 1, 1)

        self.lbNumeracion = QLabel(self.frame)
        self.lbNumeracion.setObjectName(u"lbNumeracion")
        self.lbNumeracion.setMinimumSize(QSize(20, 0))
        self.lbNumeracion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbNumeracion, 0, 0, 3, 1)

        self.teMensaje = QPlainTextEdit(self.frame)
        self.teMensaje.setObjectName(u"teMensaje")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teMensaje.sizePolicy().hasHeightForWidth())
        self.teMensaje.setSizePolicy(sizePolicy)
        self.teMensaje.setMinimumSize(QSize(0, 27))
        self.teMensaje.setReadOnly(True)

        self.gridLayout.addWidget(self.teMensaje, 2, 2, 1, 1)

        self.btAbrir = QPushButton(self.frame)
        self.btAbrir.setObjectName(u"btAbrir")
        icon = QIcon()
        icon.addFile(u":/icons/resources/images/open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btAbrir.setIcon(icon)
        self.btAbrir.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.btAbrir, 2, 3, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(resultadoAjuste)

        QMetaObject.connectSlotsByName(resultadoAjuste)
    # setupUi

    def retranslateUi(self, resultadoAjuste):
        resultadoAjuste.setWindowTitle(QCoreApplication.translate("resultadoAjuste", u"Form", None))
        self.lbCheck.setText("")
        self.lbDestino.setText(QCoreApplication.translate("resultadoAjuste", u"Destino:", None))
        self.lbOrigen.setText(QCoreApplication.translate("resultadoAjuste", u"Origen:", None))
        self.lbX.setText("")
        self.lePathOrigen.setPlaceholderText(QCoreApplication.translate("resultadoAjuste", u"Path Origen.", None))
        self.lePathDestino.setPlaceholderText(QCoreApplication.translate("resultadoAjuste", u"Path Destino.", None))
        self.lbMensaje.setText(QCoreApplication.translate("resultadoAjuste", u"Mensaje:", None))
        self.lbNumeracion.setText(QCoreApplication.translate("resultadoAjuste", u"1", None))
#if QT_CONFIG(tooltip)
        self.teMensaje.setToolTip(QCoreApplication.translate("resultadoAjuste", u"Mensaje del proceso.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.teMensaje.setStatusTip(QCoreApplication.translate("resultadoAjuste", u"0", None))
#endif // QT_CONFIG(statustip)
        self.teMensaje.setPlaceholderText(QCoreApplication.translate("resultadoAjuste", u"Sin mensaje.", None))
#if QT_CONFIG(tooltip)
        self.btAbrir.setToolTip(QCoreApplication.translate("resultadoAjuste", u"Abrir Ubicaci\u00f3  Del Archivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btAbrir.setStatusTip(QCoreApplication.translate("resultadoAjuste", u"Abrir Ubicaci\u00f3  Del Archivo.", None))
#endif // QT_CONFIG(statustip)
        self.btAbrir.setText("")
    # retranslateUi

