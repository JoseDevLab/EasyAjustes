from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QColor
from classes.ui_EditarDestino import Ui_editarDestino

class EditarDestino(QWidget, Ui_editarDestino):
    
    cambioSeleccion = Signal(int,bool)
    editado = Signal()
    
    def __init__(self,path:dict):
        super().__init__()
        self.setupUi(self)
        
        pathOrigen = path['pathOrigen']
        pathConstruir = path['pathConstruir']
        numeracion = path['numeracion']
        strConstruir = pathConstruir.path()[7:]
        strNombre = pathConstruir.fileName()
        self.leOrigen.setText(pathOrigen.filePath())
        self.leOrigen.setToolTip(pathOrigen.filePath())
        self.leConstruir.setText(strConstruir)
        self.leConstruir.setToolTip(strConstruir)
        self.leArchivo.setText(strNombre)
        self.leArchivo.setToolTip(strNombre)
        self.lbNumeracion.setText(numeracion)
        self.cbSeleccion.stateChanged.connect(self.cbSecelChanged)
        
        # Colores iniciales y finales para el hover
        self._backGroundColor1 = QColor(67, 168, 76, 255)
        self._hover_color1 = QColor(151, 234, 22, 255)
        self._backGroundColor2 = QColor(70, 197, 84, 255)
        self._hover_color2 = QColor(214, 255, 0, 255)
        self._current_color1 = self._backGroundColor1
        self._current_color2 = self._backGroundColor2
        # Crear animación para la transición de ambos colores
        tAnimacion = 300
        self.hover_animation1 = QPropertyAnimation(self, b"hover_color1")
        self.hover_animation1.setDuration(tAnimacion)
        self.hover_animation1.setEasingCurve(QEasingCurve.InOutQuad)
        self.hover_animation2 = QPropertyAnimation(self, b"hover_color2")
        self.hover_animation2.setDuration(tAnimacion)
        self.hover_animation2.setEasingCurve(QEasingCurve.InOutQuad)
        
        self.leConstruir.textChanged.connect(lambda: self.editado.emit())
        
    def cbSecelChanged(self, state):
        if state == 2:
            isChecked = True
            self.stopColorAnimation()
            self.startColorAnimation(self._hover_color1,self._hover_color2)
            self.leConstruir.setReadOnly(True)
            self.leConstruir.setStyleSheet('''
                QLineEdit{
                    font-weight: bold;
                }
            ''')
            self.leArchivo.setStyleSheet('''
                QLineEdit{
                    font-weight: bold;
                }                        
            ''')
        else:
            isChecked = False
            self.stopColorAnimation()
            self.startColorAnimation(self._backGroundColor1,self._backGroundColor2)
            self.leConstruir.setReadOnly(False)
            self.leConstruir.setStyleSheet('')
            self.leArchivo.setStyleSheet('')
            
        self.cambioSeleccion.emit(int(self.lbNumeracion.text())-1,isChecked)
        
    def startColorAnimation(self, end_color1, end_color2):
        """ Inicia la animación de los dos colores """
        self.hover_animation1.setStartValue(self._current_color1)
        self.hover_animation1.setEndValue(end_color1)
        self.hover_animation2.setStartValue(self._current_color2)
        self.hover_animation2.setEndValue(end_color2)

        # Ejecutar las animaciones
        self.hover_animation1.start()
        self.hover_animation2.start()
        
    def stopColorAnimation(self):
        self.hover_animation1.stop()
        self.hover_animation2.stop()
        
    def get_hover_color1(self):
        return self._current_color1

    def set_hover_color1(self, color):
        self._current_color1 = color
        self.updateColor()
        
    def get_hover_color2(self):
        return self._current_color2

    def set_hover_color2(self, color):
        self._current_color2 = color
        
    def updateColor(self):
        self.frame.setStyleSheet(f"""
            QFrame#frame {{
                background-color: {self._current_color1.name()};
            }}
            QLabel#lbNumeracion{{
                background-color: {self._current_color2.name()};
            }}
        """)
        
    hover_color1 = Property(QColor, get_hover_color1, set_hover_color1)
    hover_color2 = Property(QColor, get_hover_color2, set_hover_color2)