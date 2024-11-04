# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowgMkQLr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTextEdit, QTimeEdit,
    QVBoxLayout, QWidget)

from classes.HoverButton import HoverButton
from classes.Resultados import Resultados
import resources_rc

class Ui_EasyAjustes(object):
    def setupUi(self, EasyAjustes):
        if not EasyAjustes.objectName():
            EasyAjustes.setObjectName(u"EasyAjustes")
        EasyAjustes.resize(700, 700)
        icon = QIcon()
        icon.addFile(u":/icons/resources/images/icono.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        EasyAjustes.setWindowIcon(icon)
        EasyAjustes.setStyleSheet(u"QLabel#lbNombre,\n"
"QLabel#lbRuta,\n"
"QLabel#lbInicial,\n"
"QLabel#lbDestino,\n"
"QLabel#lbDetalles,\n"
"QLabel#lbResultados{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"QLabel#lbFechaInicial,\n"
"QLabel#lbFechaFinal{\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.actionCargar = QAction(EasyAjustes)
        self.actionCargar.setObjectName(u"actionCargar")
        self.actionAbrir_carpeta = QAction(EasyAjustes)
        self.actionAbrir_carpeta.setObjectName(u"actionAbrir_carpeta")
        self.actionVacio = QAction(EasyAjustes)
        self.actionVacio.setObjectName(u"actionVacio")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/images/empty.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionVacio.setIcon(icon1)
        self.actionLimpiar_historial = QAction(EasyAjustes)
        self.actionLimpiar_historial.setObjectName(u"actionLimpiar_historial")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/images/clean.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionLimpiar_historial.setIcon(icon2)
        self.actionSalir = QAction(EasyAjustes)
        self.actionSalir.setObjectName(u"actionSalir")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/images/sign_out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSalir.setIcon(icon3)
        self.actionAcercaDe = QAction(EasyAjustes)
        self.actionAcercaDe.setObjectName(u"actionAcercaDe")
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/images/info.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAcercaDe.setIcon(icon4)
        self.centralwidget = QWidget(EasyAjustes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: none;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton#btVerResultados,\n"
"QPushButton#btNuevoAjuste_2{\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 46, 68);\n"
"}\n"
"QFrame{\n"
"	background-color:rgb(160, 206, 255);\n"
"	border-radius:25px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btAcercaDe = QPushButton(self.frame_9)
        self.btAcercaDe.setObjectName(u"btAcercaDe")
        self.btAcercaDe.setMinimumSize(QSize(40, 40))
        self.btAcercaDe.setIcon(icon4)
        self.btAcercaDe.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.btAcercaDe)

        self.btVerResultados = QPushButton(self.frame_9)
        self.btVerResultados.setObjectName(u"btVerResultados")
        self.btVerResultados.setMinimumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/images/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btVerResultados.setIcon(icon5)
        self.btVerResultados.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.btVerResultados)

        self.btNuevoAjuste_2 = QPushButton(self.frame_9)
        self.btNuevoAjuste_2.setObjectName(u"btNuevoAjuste_2")
        self.btNuevoAjuste_2.setMinimumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u":/icons/resources/images/new.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btNuevoAjuste_2.setIcon(icon6)
        self.btNuevoAjuste_2.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.btNuevoAjuste_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.horizontalSpacer_2 = QSpacerItem(104, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"font: 600 30pt \"Lucida Bright\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.swPaneles = QStackedWidget(self.frame_8)
        self.swPaneles.setObjectName(u"swPaneles")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.saPrincipal = QScrollArea(self.page_3)
        self.saPrincipal.setObjectName(u"saPrincipal")
        self.saPrincipal.setMinimumSize(QSize(558, 0))
        self.saPrincipal.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 556, 505))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbNombre = QLabel(self.frame_3)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbNombre)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btSugerir = QPushButton(self.frame_2)
        self.btSugerir.setObjectName(u"btSugerir")

        self.horizontalLayout.addWidget(self.btSugerir)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.sbNumeracion = QSpinBox(self.frame_2)
        self.sbNumeracion.setObjectName(u"sbNumeracion")
        self.sbNumeracion.setMinimumSize(QSize(70, 0))
        self.sbNumeracion.setAutoFillBackground(False)
        self.sbNumeracion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sbNumeracion.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.sbNumeracion.setProperty(u"showGroupSeparator", False)
        self.sbNumeracion.setMaximum(9999)
        self.sbNumeracion.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.sbNumeracion)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.deFecha = QDateEdit(self.frame_2)
        self.deFecha.setObjectName(u"deFecha")
        self.deFecha.setMinimumSize(QSize(110, 0))

        self.horizontalLayout.addWidget(self.deFecha)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.teHora = QTimeEdit(self.frame_2)
        self.teHora.setObjectName(u"teHora")
        self.teHora.setMinimumSize(QSize(80, 0))
        self.teHora.setCurrentSection(QDateTimeEdit.Section.MinuteSection)
        self.teHora.setCalendarPopup(False)
        self.teHora.setCurrentSectionIndex(1)
        self.teHora.setTimeSpec(Qt.TimeSpec.UTC)

        self.horizontalLayout.addWidget(self.teHora)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.leSigla = QLineEdit(self.frame_2)
        self.leSigla.setObjectName(u"leSigla")
        self.leSigla.setMinimumSize(QSize(50, 0))
        self.leSigla.setMaximumSize(QSize(50, 16777215))
        self.leSigla.setMaxLength(3)
        self.leSigla.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leSigla.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.leSigla)

        self.cbSiglas = QComboBox(self.frame_2)
        self.cbSiglas.addItem("")
        self.cbSiglas.setObjectName(u"cbSiglas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSiglas.sizePolicy().hasHeightForWidth())
        self.cbSiglas.setSizePolicy(sizePolicy)
        self.cbSiglas.setMinimumSize(QSize(50, 0))
        self.cbSiglas.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.cbSiglas)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.rbArchivoTxt = QRadioButton(self.frame_12)
        self.rbArchivoTxt.setObjectName(u"rbArchivoTxt")
        self.rbArchivoTxt.setChecked(True)

        self.horizontalLayout_4.addWidget(self.rbArchivoTxt)

        self.horizontalSpacer_4 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.rbBusquedaFecha = QRadioButton(self.frame_12)
        self.rbBusquedaFecha.setObjectName(u"rbBusquedaFecha")
        self.rbBusquedaFecha.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.rbBusquedaFecha)

        self.horizontalSpacer_5 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 4)
        self.btSelecTxt = QPushButton(self.frame_5)
        self.btSelecTxt.setObjectName(u"btSelecTxt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btSelecTxt.sizePolicy().hasHeightForWidth())
        self.btSelecTxt.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btSelecTxt, 1, 0, 1, 1)

        self.lbRuta = QLabel(self.frame_5)
        self.lbRuta.setObjectName(u"lbRuta")
        self.lbRuta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbRuta, 0, 0, 1, 2)

        self.swSeleccionar = QStackedWidget(self.frame_5)
        self.swSeleccionar.setObjectName(u"swSeleccionar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.swSeleccionar.sizePolicy().hasHeightForWidth())
        self.swSeleccionar.setSizePolicy(sizePolicy2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_11 = QVBoxLayout(self.page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.leArchSelec = QLineEdit(self.page)
        self.leArchSelec.setObjectName(u"leArchSelec")
        self.leArchSelec.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.leArchSelec)

        self.swSeleccionar.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbFechaFinal = QLabel(self.page_2)
        self.lbFechaFinal.setObjectName(u"lbFechaFinal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbFechaFinal.sizePolicy().hasHeightForWidth())
        self.lbFechaFinal.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.lbFechaFinal, 2, 0, 1, 1)

        self.dteFinal = QDateTimeEdit(self.page_2)
        self.dteFinal.setObjectName(u"dteFinal")
        self.dteFinal.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dteFinal, 2, 1, 1, 1)

        self.lbFechaInicial = QLabel(self.page_2)
        self.lbFechaInicial.setObjectName(u"lbFechaInicial")
        sizePolicy3.setHeightForWidth(self.lbFechaInicial.sizePolicy().hasHeightForWidth())
        self.lbFechaInicial.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.lbFechaInicial, 1, 0, 1, 1)

        self.dteInicial = QDateTimeEdit(self.page_2)
        self.dteInicial.setObjectName(u"dteInicial")
        self.dteInicial.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dteInicial, 1, 1, 1, 1)

        self.leDirecBus = QLineEdit(self.page_2)
        self.leDirecBus.setObjectName(u"leDirecBus")
        self.leDirecBus.setReadOnly(True)

        self.gridLayout_3.addWidget(self.leDirecBus, 0, 0, 1, 2)

        self.swSeleccionar.addWidget(self.page_2)

        self.gridLayout.addWidget(self.swSeleccionar, 2, 0, 1, 1)

        self.btVer = QPushButton(self.frame_5)
        self.btVer.setObjectName(u"btVer")
        self.btVer.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btVer.sizePolicy().hasHeightForWidth())
        self.btVer.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btVer, 1, 1, 2, 1)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.cbCarpetaIni = QComboBox(self.frame_7)
        self.cbCarpetaIni.setObjectName(u"cbCarpetaIni")
        self.cbCarpetaIni.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cbCarpetaIni.sizePolicy().hasHeightForWidth())
        self.cbCarpetaIni.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.cbCarpetaIni, 1, 0, 1, 1)

        self.chbIncluirCarp = QCheckBox(self.frame_7)
        self.chbIncluirCarp.setObjectName(u"chbIncluirCarp")
        self.chbIncluirCarp.setChecked(True)

        self.gridLayout_2.addWidget(self.chbIncluirCarp, 1, 2, 1, 1)

        self.lbInicial = QLabel(self.frame_7)
        self.lbInicial.setObjectName(u"lbInicial")
        self.lbInicial.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbInicial, 0, 0, 1, 3)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 4, -1, 4)
        self.lbDestino = QLabel(self.frame_6)
        self.lbDestino.setObjectName(u"lbDestino")
        self.lbDestino.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbDestino)

        self.btSelecDest = QPushButton(self.frame_6)
        self.btSelecDest.setObjectName(u"btSelecDest")

        self.verticalLayout_5.addWidget(self.btSelecDest)

        self.leDirecSelec = QLineEdit(self.frame_6)
        self.leDirecSelec.setObjectName(u"leDirecSelec")
        self.leDirecSelec.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.leDirecSelec)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.lbDetalles = QLabel(self.frame_4)
        self.lbDetalles.setObjectName(u"lbDetalles")
        self.lbDetalles.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbDetalles)

        self.teDetalles = QTextEdit(self.frame_4)
        self.teDetalles.setObjectName(u"teDetalles")

        self.verticalLayout_3.addWidget(self.teDetalles)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.saPrincipal.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.saPrincipal)

        self.swPaneles.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.resultados = Resultados(self.page_4)
        self.resultados.setObjectName(u"resultados")

        self.verticalLayout_4.addWidget(self.resultados)

        self.swPaneles.addWidget(self.page_4)

        self.verticalLayout_10.addWidget(self.swPaneles)

        self.frBotones = QFrame(self.frame_8)
        self.frBotones.setObjectName(u"frBotones")
        self.frBotones.setMinimumSize(QSize(0, 30))
        self.frBotones.setStyleSheet(u"QFrame{\n"
"	border-radius: 35px;\n"
"}\n"
"QPushButton{\n"
"	norder: none;\n"
"	border-radius: 35px;\n"
"	color: white;\n"
"	background: qlineargradient(\n"
"                    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                    stop: 0 rgba(109, 242, 127, 255),\n"
"                    stop: 1 rgba(127, 130, 239, 255)\n"
"    );\n"
"	\n"
"	font: 700 24pt \"Arial Narrow\";\n"
"}\n"
"QPushButton:hover{\n"
"	background: qlineargradient(\n"
"                    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                    stop: 0 rgba(230, 228, 47, 255),\n"
"                    stop: 1 rgba(60, 233, 103, 255)\n"
"    );\n"
"	font: 700 40pt \"Arial Narrow\";\n"
"}")
        self.frBotones.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBotones.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frBotones)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btCrearAjuste = HoverButton(self.frBotones)
        self.btCrearAjuste.setObjectName(u"btCrearAjuste")
        self.btCrearAjuste.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_3.addWidget(self.btCrearAjuste)

        self.btNuevoAjuste = HoverButton(self.frBotones)
        self.btNuevoAjuste.setObjectName(u"btNuevoAjuste")
        self.btNuevoAjuste.setMinimumSize(QSize(0, 70))

        self.horizontalLayout_3.addWidget(self.btNuevoAjuste)


        self.verticalLayout_10.addWidget(self.frBotones)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.horizontalSpacer = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame)

        EasyAjustes.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EasyAjustes)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 33))
        self.menuHistorial = QMenu(self.menubar)
        self.menuHistorial.setObjectName(u"menuHistorial")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        EasyAjustes.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(EasyAjustes)
        self.statusbar.setObjectName(u"statusbar")
        EasyAjustes.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHistorial.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuHistorial.addAction(self.actionVacio)
        self.menuArchivo.addAction(self.actionLimpiar_historial)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcercaDe)

        self.retranslateUi(EasyAjustes)

        self.swPaneles.setCurrentIndex(0)
        self.swSeleccionar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EasyAjustes)
    # setupUi

    def retranslateUi(self, EasyAjustes):
        EasyAjustes.setWindowTitle(QCoreApplication.translate("EasyAjustes", u"Easy Ajustes", None))
        self.actionCargar.setText(QCoreApplication.translate("EasyAjustes", u"Cargar", None))
        self.actionAbrir_carpeta.setText(QCoreApplication.translate("EasyAjustes", u"Abrir carpeta", None))
        self.actionVacio.setText(QCoreApplication.translate("EasyAjustes", u"Vac\u00edo", None))
        self.actionLimpiar_historial.setText(QCoreApplication.translate("EasyAjustes", u"Limpiar historial", None))
        self.actionSalir.setText(QCoreApplication.translate("EasyAjustes", u"Salir", None))
        self.actionAcercaDe.setText(QCoreApplication.translate("EasyAjustes", u"Acerca de Easy Ajustes", None))
#if QT_CONFIG(tooltip)
        self.btAcercaDe.setToolTip(QCoreApplication.translate("EasyAjustes", u"Acerca de Easy Ajustes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btAcercaDe.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Acerca de Easy Ajustes", None))
#endif // QT_CONFIG(statustip)
        self.btAcercaDe.setText("")
#if QT_CONFIG(tooltip)
        self.btVerResultados.setToolTip(QCoreApplication.translate("EasyAjustes", u"Ver Resultados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btVerResultados.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Ver Resultados", None))
#endif // QT_CONFIG(statustip)
        self.btVerResultados.setText("")
#if QT_CONFIG(tooltip)
        self.btNuevoAjuste_2.setToolTip(QCoreApplication.translate("EasyAjustes", u"Nuevo Ajuste", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btNuevoAjuste_2.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Nuevo Ajuste", None))
#endif // QT_CONFIG(statustip)
        self.btNuevoAjuste_2.setText("")
        self.label.setText(QCoreApplication.translate("EasyAjustes", u"Easy Ajustes", None))
        self.lbNombre.setText(QCoreApplication.translate("EasyAjustes", u"Nombre del ajuste", None))
#if QT_CONFIG(tooltip)
        self.btSugerir.setToolTip(QCoreApplication.translate("EasyAjustes", u"Sugerir nombre.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btSugerir.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Sugerir nombre con fecha y hora actual.", None))
#endif // QT_CONFIG(statustip)
        self.btSugerir.setText(QCoreApplication.translate("EasyAjustes", u"Sugerir", None))
        self.label_2.setText(QCoreApplication.translate("EasyAjustes", u"AJ", None))
#if QT_CONFIG(tooltip)
        self.sbNumeracion.setToolTip(QCoreApplication.translate("EasyAjustes", u"Numeraci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.sbNumeracion.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Numeraci\u00f3n del ajuste.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.sbNumeracion.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.sbNumeracion.setSpecialValueText("")
        self.label_3.setText(QCoreApplication.translate("EasyAjustes", u"_", None))
#if QT_CONFIG(tooltip)
        self.deFecha.setToolTip(QCoreApplication.translate("EasyAjustes", u"Fecha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.deFecha.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Fecha", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("EasyAjustes", u"_", None))
#if QT_CONFIG(tooltip)
        self.teHora.setToolTip(QCoreApplication.translate("EasyAjustes", u"Hora", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.teHora.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Hora", None))
#endif // QT_CONFIG(statustip)
        self.teHora.setDisplayFormat(QCoreApplication.translate("EasyAjustes", u"hh:mm", None))
        self.label_9.setText(QCoreApplication.translate("EasyAjustes", u"_", None))
#if QT_CONFIG(tooltip)
        self.leSigla.setToolTip(QCoreApplication.translate("EasyAjustes", u"Sigla", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.leSigla.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Sigla de tu nombre y apellido. Ej: JV (Jose Villamizar)", None))
#endif // QT_CONFIG(statustip)
        self.leSigla.setPlaceholderText(QCoreApplication.translate("EasyAjustes", u"Sigla", None))
        self.cbSiglas.setItemText(0, QCoreApplication.translate("EasyAjustes", u"__", None))

#if QT_CONFIG(tooltip)
        self.cbSiglas.setToolTip(QCoreApplication.translate("EasyAjustes", u"Sigla", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.cbSiglas.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Siglas recientes.", None))
#endif // QT_CONFIG(statustip)
        self.rbArchivoTxt.setText(QCoreApplication.translate("EasyAjustes", u"PATHS desde archivo.txt", None))
        self.rbBusquedaFecha.setText(QCoreApplication.translate("EasyAjustes", u"PATHS desde b\u00fasqueda por fechas", None))
#if QT_CONFIG(statustip)
        self.btSelecTxt.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Seleccionar archivo.", None))
#endif // QT_CONFIG(statustip)
        self.btSelecTxt.setText(QCoreApplication.translate("EasyAjustes", u"Seleccionar", None))
        self.lbRuta.setText(QCoreApplication.translate("EasyAjustes", u"TXT con rutas de archivos", None))
#if QT_CONFIG(tooltip)
        self.leArchSelec.setToolTip(QCoreApplication.translate("EasyAjustes", u"Archivo seleccionado.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.leArchSelec.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Archivo seleccionado.", None))
#endif // QT_CONFIG(statustip)
        self.leArchSelec.setPlaceholderText(QCoreApplication.translate("EasyAjustes", u"Ning\u00fan archivo a\u00fan.", None))
        self.lbFechaFinal.setText(QCoreApplication.translate("EasyAjustes", u"Fecha Final:", None))
        self.lbFechaInicial.setText(QCoreApplication.translate("EasyAjustes", u"Fecha Inicial:", None))
        self.leDirecBus.setPlaceholderText(QCoreApplication.translate("EasyAjustes", u"Directorio de b\u00fasqueda.", None))
#if QT_CONFIG(tooltip)
        self.btVer.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btVer.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Ver, Modificar, Agregar.", None))
#endif // QT_CONFIG(statustip)
        self.btVer.setText(QCoreApplication.translate("EasyAjustes", u"Ver\n"
"Editar Paths", None))
#if QT_CONFIG(tooltip)
        self.cbCarpetaIni.setToolTip(QCoreApplication.translate("EasyAjustes", u"Carpeta inicial", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.cbCarpetaIni.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Carpeta m\u00e1s externa del ajuste.", None))
#endif // QT_CONFIG(statustip)
        self.chbIncluirCarp.setText(QCoreApplication.translate("EasyAjustes", u"Incluir\n"
"carpeta", None))
        self.lbInicial.setText(QCoreApplication.translate("EasyAjustes", u"Carpeta inicial", None))
        self.lbDestino.setText(QCoreApplication.translate("EasyAjustes", u"Carpeta destino", None))
#if QT_CONFIG(statustip)
        self.btSelecDest.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Seleccionar d\u00f3nde guardar el ajuste.", None))
#endif // QT_CONFIG(statustip)
        self.btSelecDest.setText(QCoreApplication.translate("EasyAjustes", u"Seleccionar", None))
#if QT_CONFIG(tooltip)
        self.leDirecSelec.setToolTip(QCoreApplication.translate("EasyAjustes", u"Directorio seleccionado.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.leDirecSelec.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Directorio seleccionado para guardar el ajuste.", None))
#endif // QT_CONFIG(statustip)
        self.leDirecSelec.setPlaceholderText(QCoreApplication.translate("EasyAjustes", u"Ning\u00fan directorio a\u00fan.", None))
        self.lbDetalles.setText(QCoreApplication.translate("EasyAjustes", u"Descripci\u00f3n y Detalles", None))
#if QT_CONFIG(statustip)
        self.teDetalles.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Para qu\u00e9 CAT est\u00e1 dirigido y detalles adicionales.", None))
#endif // QT_CONFIG(statustip)
        self.teDetalles.setHtml(QCoreApplication.translate("EasyAjustes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.teDetalles.setPlaceholderText(QCoreApplication.translate("EasyAjustes", u"Para qu\u00e9 CAT est\u00e1 dirigido y detalles adicionales.", None))
#if QT_CONFIG(statustip)
        self.btCrearAjuste.setStatusTip(QCoreApplication.translate("EasyAjustes", u"Crear el ajuste.", None))
#endif // QT_CONFIG(statustip)
        self.btCrearAjuste.setText(QCoreApplication.translate("EasyAjustes", u"CREAR AJUSTE", None))
        self.btNuevoAjuste.setText(QCoreApplication.translate("EasyAjustes", u"NUEVO AJUSTE", None))
        self.menuHistorial.setTitle(QCoreApplication.translate("EasyAjustes", u"Historial", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("EasyAjustes", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("EasyAjustes", u"Ayuda", None))
    # retranslateUi

