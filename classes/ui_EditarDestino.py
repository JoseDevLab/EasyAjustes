# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditarDestinoUXMHgB.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_editarDestino(object):
    def setupUi(self, editarDestino):
        if not editarDestino.objectName():
            editarDestino.setObjectName(u"editarDestino")
        editarDestino.resize(555, 58)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editarDestino.sizePolicy().hasHeightForWidth())
        editarDestino.setSizePolicy(sizePolicy)
        editarDestino.setStyleSheet(u"QLabel#lbOrigen,\n"
"QLabel#lbConstruir{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"QLabel#lbNumeracion{\n"
"	font: 9pt \"Roman\";\n"
"}\n"
"QLabel{color: black;}\n"
"QFrame#frame{\n"
"	background-color: rgb(67, 168, 76);\n"
"	border-radius:12px\n"
"}\n"
"QLabel#lbNumeracion{\n"
"	background-color:rgb(70, 197, 84);\n"
"	border-radius:10px\n"
"}")
        self.verticalLayout = QVBoxLayout(editarDestino)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(editarDestino)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.leConstruir = QLineEdit(self.frame)
        self.leConstruir.setObjectName(u"leConstruir")
        self.leConstruir.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.leConstruir, 1, 4, 1, 1)

        self.leOrigen = QLineEdit(self.frame)
        self.leOrigen.setObjectName(u"leOrigen")
        self.leOrigen.setReadOnly(True)

        self.gridLayout.addWidget(self.leOrigen, 0, 3, 1, 4)

        self.leArchivo = QLineEdit(self.frame)
        self.leArchivo.setObjectName(u"leArchivo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leArchivo.sizePolicy().hasHeightForWidth())
        self.leArchivo.setSizePolicy(sizePolicy1)
        self.leArchivo.setMinimumSize(QSize(130, 0))
        self.leArchivo.setReadOnly(True)

        self.gridLayout.addWidget(self.leArchivo, 1, 6, 1, 1)

        self.lbConstruir = QLabel(self.frame)
        self.lbConstruir.setObjectName(u"lbConstruir")

        self.gridLayout.addWidget(self.lbConstruir, 1, 2, 1, 1)

        self.lbOrigen = QLabel(self.frame)
        self.lbOrigen.setObjectName(u"lbOrigen")

        self.gridLayout.addWidget(self.lbOrigen, 0, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.lbArchivo = QLabel(self.frame)
        self.lbArchivo.setObjectName(u"lbArchivo")

        self.gridLayout.addWidget(self.lbArchivo, 1, 5, 1, 1)

        self.lbNumeracion = QLabel(self.frame)
        self.lbNumeracion.setObjectName(u"lbNumeracion")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbNumeracion.sizePolicy().hasHeightForWidth())
        self.lbNumeracion.setSizePolicy(sizePolicy2)
        self.lbNumeracion.setMinimumSize(QSize(20, 0))
        self.lbNumeracion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbNumeracion, 0, 1, 2, 1)

        self.cbSeleccion = QCheckBox(self.frame)
        self.cbSeleccion.setObjectName(u"cbSeleccion")

        self.gridLayout.addWidget(self.cbSeleccion, 0, 0, 2, 1)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(editarDestino)

        QMetaObject.connectSlotsByName(editarDestino)
    # setupUi

    def retranslateUi(self, editarDestino):
        editarDestino.setWindowTitle(QCoreApplication.translate("editarDestino", u"Form", None))
        self.lbConstruir.setText(QCoreApplication.translate("editarDestino", u"Construir:", None))
        self.lbOrigen.setText(QCoreApplication.translate("editarDestino", u"Origen:", None))
        self.label_3.setText(QCoreApplication.translate("editarDestino", u"UNIDAD/", None))
        self.lbArchivo.setText(QCoreApplication.translate("editarDestino", u"/", None))
        self.lbNumeracion.setText(QCoreApplication.translate("editarDestino", u"1", None))
        self.cbSeleccion.setText("")
    # retranslateUi

