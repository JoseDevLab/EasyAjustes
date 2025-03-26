import os
import subprocess
import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QObject, QEvent, QFileInfo
from classes.ui_ResultadoAjuste import Ui_resultadoAjuste

class ResultadoAjuste(QWidget, Ui_resultadoAjuste):
    def __init__(self, path:dict, parent:QWidget|None=...):
        super().__init__(parent)
        self.setupUi(self)
        pathOrigen = path['pathOrigen'].filePath()
        pathDestino = path['pathDestino']
        numeracion = path['numeracion']
        copiado = path['copiado']
        mensaje = path['mensaje']
        self.lePathOrigen.setText(pathOrigen)
        self.lePathOrigen.setToolTip(pathOrigen)
        self.lePathOrigen.setStatusTip(pathOrigen)
        self.lePathDestino.setText(pathDestino)
        self.lePathDestino.setToolTip(pathDestino)
        self.lePathDestino.setStatusTip(pathDestino)
        self.lbNumeracion.setText(numeracion)
        self.lbNumeracion.setStatusTip(f'Archivo numero: {numeracion}')
        if copiado:
            self.lbCheck.setVisible(True)
            self.lbX.setVisible(False)
            style =('QFrame#frame{background-color: rgb(118, 168, 110);}'
                    'QFrame#frame:hover{background-color: rgb(134, 189, 124);}'
                    'QLabel#lbNumeracion{background-color:rgb(134, 189, 124);}')
        else:
            self.lbCheck.setVisible(False)
            self.lbX.setVisible(True)
            self.btAbrir.setEnabled(False)
            style =('QFrame#frame{background-color: rgb(144, 55, 55);}'
                    'QFrame#frame:hover{background-color: rgb(171, 65, 65);}'
                    'QLabel#lbNumeracion{background-color:rgb(171, 65, 65);}')
        self.frame.setStyleSheet(style)
        self.lbCheck.setToolTip('Ok.')
        self.lbCheck.setStatusTip('Ok.')
        self.lbX.setToolTip('Error.')
        self.lbX.setStatusTip('Error.')

        self.teMensaje.setPlainText(mensaje)
        self.teMensaje.setStatusTip('Mensaje del proceso.')
        self.teMensaje.document().adjustSize()
        
        self.btAbrir.clicked.connect(self.abrir)

        # Crear un filtro de eventos y asociarlo al QPlainTextEdit
        filtro = MiFiltroDeEventos(self)
        self.teMensaje.installEventFilter(filtro)
        
    def abrir(self):
        folder_path = QFileInfo(self.lePathDestino.text()).path()
        if sys.platform.startswith('win'):
            # Para Windows
            subprocess.Popen(f'explorer "{os.path.normpath(folder_path)}"')
        elif sys.platform == 'darwin':
            # Para macOS
            subprocess.Popen(['open', folder_path])
        elif sys.platform.startswith('linux'):
            # Para Linux
            subprocess.Popen(['xdg-open', folder_path])
        else:
            print("Sistema operativo no soportado.")

class MiFiltroDeEventos(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hNormal = parent.teMensaje.height()
        self.animacion = QPropertyAnimation(parent.teMensaje, b"minimumHeight")
        self.animacion.setDuration(300)
        self.animacion.setEasingCurve(QEasingCurve.InQuad) # InQuad, InOutQuad, InCubic, InOutExpo, OutInBack

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            inicial = self.parent().teMensaje.height()
            final = self.calcAltura()
            if final > inicial:
                self.animacion.stop()
                self.animacion.setStartValue(inicial)
                self.animacion.setEndValue(final)
                self.animacion.start()
        elif event.type() == QEvent.Leave:
            inicial = self.parent().teMensaje.height()
            final = self.hNormal
            if final < inicial:
                self.animacion.stop()
                self.animacion.setStartValue(inicial)
                self.animacion.setEndValue(final)
                self.animacion.start()
        # Continuar procesando otros eventos normalmente
        return super().eventFilter(obj, event)
    
    def calcAltura(self):
        altura_total = 0
        block = self.parent().teMensaje.document().firstBlock()
        while block.isValid():
            # Obtener la altura de cada bloque de texto
            block_height = self.parent().teMensaje.document().documentLayout().blockBoundingRect(block).height()
            altura_total += block_height
            block = block.next()
        return altura_total