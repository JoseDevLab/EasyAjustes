# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultadosiMfUSV.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_resultados(object):
    def setupUi(self, resultados):
        if not resultados.objectName():
            resultados.setObjectName(u"resultados")
        resultados.resize(531, 478)
        resultados.setStyleSheet(u"QFrame#frIz,\n"
"QFrame#frDe{\n"
"	background-color:rgba(0,0,0,0);\n"
"}")
        self.verticalLayout = QVBoxLayout(resultados)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(resultados)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.vlResultados = QVBoxLayout(self.frame)
        self.vlResultados.setObjectName(u"vlResultados")
        self.vlResultados.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.hlTituloResultados = QHBoxLayout(self.frame_2)
        self.hlTituloResultados.setSpacing(5)
        self.hlTituloResultados.setObjectName(u"hlTituloResultados")
        self.hlTituloResultados.setContentsMargins(0, 0, 0, 0)
        self.frIz = QFrame(self.frame_2)
        self.frIz.setObjectName(u"frIz")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frIz.sizePolicy().hasHeightForWidth())
        self.frIz.setSizePolicy(sizePolicy)
        self.frIz.setFrameShape(QFrame.Shape.StyledPanel)
        self.frIz.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frIz)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frPaginas = QFrame(self.frIz)
        self.frPaginas.setObjectName(u"frPaginas")
        self.frPaginas.setMinimumSize(QSize(0, 0))
        self.frPaginas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPaginas.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frPaginas)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btPagAnterior = QPushButton(self.frPaginas)
        self.btPagAnterior.setObjectName(u"btPagAnterior")
        self.btPagAnterior.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/icons/resources/images/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPagAnterior.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btPagAnterior)

        self.lbPaginas = QLabel(self.frPaginas)
        self.lbPaginas.setObjectName(u"lbPaginas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbPaginas.sizePolicy().hasHeightForWidth())
        self.lbPaginas.setSizePolicy(sizePolicy1)
        self.lbPaginas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbPaginas)

        self.btPagSiguiente = QPushButton(self.frPaginas)
        self.btPagSiguiente.setObjectName(u"btPagSiguiente")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/images/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPagSiguiente.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btPagSiguiente)


        self.horizontalLayout.addWidget(self.frPaginas)

        self.horizontalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.hlTituloResultados.addWidget(self.frIz)

        self.lbResultados = QLabel(self.frame_2)
        self.lbResultados.setObjectName(u"lbResultados")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbResultados.sizePolicy().hasHeightForWidth())
        self.lbResultados.setSizePolicy(sizePolicy2)
        self.lbResultados.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hlTituloResultados.addWidget(self.lbResultados)

        self.frDe = QFrame(self.frame_2)
        self.frDe.setObjectName(u"frDe")
        self.frDe.setFrameShape(QFrame.Shape.StyledPanel)
        self.frDe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frDe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.hlTituloResultados.addWidget(self.frDe)


        self.vlResultados.addWidget(self.frame_2)

        self.resultadoTxt = QWidget(self.frame)
        self.resultadoTxt.setObjectName(u"resultadoTxt")

        self.vlResultados.addWidget(self.resultadoTxt)

        self.saResultados = QScrollArea(self.frame)
        self.saResultados.setObjectName(u"saResultados")
        self.saResultados.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 527, 422))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.swResultados = QStackedWidget(self.scrollAreaWidgetContents)
        self.swResultados.setObjectName(u"swResultados")

        self.verticalLayout_3.addWidget(self.swResultados)

        self.saResultados.setWidget(self.scrollAreaWidgetContents)

        self.vlResultados.addWidget(self.saResultados)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(resultados)

        self.swResultados.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(resultados)
    # setupUi

    def retranslateUi(self, resultados):
        resultados.setWindowTitle(QCoreApplication.translate("resultados", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btPagAnterior.setToolTip(QCoreApplication.translate("resultados", u"P\u00e1gina anterior", None))
#endif // QT_CONFIG(tooltip)
        self.btPagAnterior.setText("")
        self.lbPaginas.setText(QCoreApplication.translate("resultados", u"1 al 10 de n", None))
#if QT_CONFIG(tooltip)
        self.btPagSiguiente.setToolTip(QCoreApplication.translate("resultados", u"P\u00e1gina siguiente", None))
#endif // QT_CONFIG(tooltip)
        self.btPagSiguiente.setText("")
        self.lbResultados.setText(QCoreApplication.translate("resultados", u"Resultados Del Ajuste", None))
    # retranslateUi

