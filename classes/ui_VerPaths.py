# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerPathsRAFzhu.ui'
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_verPaths(object):
    def setupUi(self, verPaths):
        if not verPaths.objectName():
            verPaths.setObjectName(u"verPaths")
        verPaths.setWindowModality(Qt.WindowModality.NonModal)
        verPaths.resize(1406, 586)
        icon = QIcon()
        icon.addFile(u":/icons/resources/images/icono.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        verPaths.setWindowIcon(icon)
        verPaths.setStyleSheet(u"QLabel#lbPaths,\n"
"QLabel#lbModificar{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"QFrame#frIz,\n"
"QFrame#frDe{\n"
"	background-color:rgba(0,0,0,0);\n"
"}")
        verPaths.setModal(False)
        self.verticalLayout = QVBoxLayout(verPaths)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(verPaths)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 600 30pt \"Lucida Bright\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbPaths = QLabel(self.frame)
        self.lbPaths.setObjectName(u"lbPaths")
        self.lbPaths.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbPaths)

        self.tePaths = QPlainTextEdit(self.frame)
        self.tePaths.setObjectName(u"tePaths")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tePaths.sizePolicy().hasHeightForWidth())
        self.tePaths.setSizePolicy(sizePolicy)
        self.tePaths.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_2.addWidget(self.tePaths)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.btValidar = QPushButton(self.frame)
        self.btValidar.setObjectName(u"btValidar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btValidar.sizePolicy().hasHeightForWidth())
        self.btValidar.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/images/flecha.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btValidar.setIcon(icon1)
        self.btValidar.setIconSize(QSize(50, 50))

        self.verticalLayout_3.addWidget(self.btValidar)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frTituloDestinos = QFrame(self.frame_3)
        self.frTituloDestinos.setObjectName(u"frTituloDestinos")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frTituloDestinos.sizePolicy().hasHeightForWidth())
        self.frTituloDestinos.setSizePolicy(sizePolicy3)
        self.frTituloDestinos.setMinimumSize(QSize(0, 0))
        self.frTituloDestinos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frTituloDestinos.setFrameShadow(QFrame.Shadow.Raised)
        self.hlTituloDestinos = QHBoxLayout(self.frTituloDestinos)
        self.hlTituloDestinos.setSpacing(0)
        self.hlTituloDestinos.setObjectName(u"hlTituloDestinos")
        self.hlTituloDestinos.setContentsMargins(0, 0, 0, 0)
        self.frIz = QFrame(self.frTituloDestinos)
        self.frIz.setObjectName(u"frIz")
        sizePolicy2.setHeightForWidth(self.frIz.sizePolicy().hasHeightForWidth())
        self.frIz.setSizePolicy(sizePolicy2)
        self.frIz.setFrameShape(QFrame.Shape.StyledPanel)
        self.frIz.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frIz)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/images/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPagAnterior.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btPagAnterior)

        self.lbPaginas = QLabel(self.frPaginas)
        self.lbPaginas.setObjectName(u"lbPaginas")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lbPaginas.sizePolicy().hasHeightForWidth())
        self.lbPaginas.setSizePolicy(sizePolicy4)
        self.lbPaginas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbPaginas)

        self.btPagSiguiente = QPushButton(self.frPaginas)
        self.btPagSiguiente.setObjectName(u"btPagSiguiente")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/images/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPagSiguiente.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btPagSiguiente)


        self.horizontalLayout_4.addWidget(self.frPaginas)

        self.horizontalSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.hlTituloDestinos.addWidget(self.frIz)

        self.lbModificar = QLabel(self.frTituloDestinos)
        self.lbModificar.setObjectName(u"lbModificar")
        sizePolicy3.setHeightForWidth(self.lbModificar.sizePolicy().hasHeightForWidth())
        self.lbModificar.setSizePolicy(sizePolicy3)
        self.lbModificar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hlTituloDestinos.addWidget(self.lbModificar)

        self.frDe = QFrame(self.frTituloDestinos)
        self.frDe.setObjectName(u"frDe")
        sizePolicy2.setHeightForWidth(self.frDe.sizePolicy().hasHeightForWidth())
        self.frDe.setSizePolicy(sizePolicy2)
        self.frDe.setFrameShape(QFrame.Shape.StyledPanel)
        self.frDe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frDe)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.hlTituloDestinos.addWidget(self.frDe)


        self.verticalLayout_4.addWidget(self.frTituloDestinos)

        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 650, 411))
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.frEditarVarios = QFrame(self.frame_3)
        self.frEditarVarios.setObjectName(u"frEditarVarios")
        self.frEditarVarios.setMinimumSize(QSize(0, 0))
        self.frEditarVarios.setFrameShape(QFrame.Shape.StyledPanel)
        self.frEditarVarios.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frEditarVarios)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leSeleccion = QLineEdit(self.frEditarVarios)
        self.leSeleccion.setObjectName(u"leSeleccion")

        self.horizontalLayout_2.addWidget(self.leSeleccion)

        self.btEditSeleccion = QPushButton(self.frEditarVarios)
        self.btEditSeleccion.setObjectName(u"btEditSeleccion")

        self.horizontalLayout_2.addWidget(self.btEditSeleccion)


        self.verticalLayout_4.addWidget(self.frEditarVarios)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_5.addWidget(self.buttonBox)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(verPaths)
        self.buttonBox.accepted.connect(verPaths.accept)
        self.buttonBox.rejected.connect(verPaths.reject)

        QMetaObject.connectSlotsByName(verPaths)
    # setupUi

    def retranslateUi(self, verPaths):
        verPaths.setWindowTitle(QCoreApplication.translate("verPaths", u"Ver - Editar Paths", None))
        self.label.setText(QCoreApplication.translate("verPaths", u"Ver - Editar Paths", None))
        self.lbPaths.setText(QCoreApplication.translate("verPaths", u"Paths Archivos", None))
        self.label_4.setText("")
#if QT_CONFIG(tooltip)
        self.btValidar.setToolTip(QCoreApplication.translate("verPaths", u"Validar Paths", None))
#endif // QT_CONFIG(tooltip)
        self.btValidar.setText("")
#if QT_CONFIG(tooltip)
        self.btPagAnterior.setToolTip(QCoreApplication.translate("verPaths", u"P\u00e1gina anterior", None))
#endif // QT_CONFIG(tooltip)
        self.btPagAnterior.setText("")
        self.lbPaginas.setText(QCoreApplication.translate("verPaths", u"1 al 10 de n", None))
#if QT_CONFIG(tooltip)
        self.btPagSiguiente.setToolTip(QCoreApplication.translate("verPaths", u"P\u00e1gina siguiente", None))
#endif // QT_CONFIG(tooltip)
        self.btPagSiguiente.setText("")
        self.lbModificar.setText(QCoreApplication.translate("verPaths", u"Modificar Destinos", None))
        self.btEditSeleccion.setText(QCoreApplication.translate("verPaths", u"Editar seleccionados", None))
    # retranslateUi

