from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QEvent, Property
from PySide6.QtGui import QColor

class HoverButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Colores iniciales y finales para el hover
        self._backGroundColor1 = QColor(109, 242, 127, 255)
        self._hover_color1 = QColor(230, 228, 47, 255)
        self._backGroundColor2 = QColor(127, 130, 239, 255)
        self._hover_color2 = QColor(60, 233, 103, 255)
        self._current_color1 = self._backGroundColor1
        self._current_color2 = self._backGroundColor2
        
        self._fontSize = 24
        self._hover_fontSize = 40
        self._current_fontSize = self._fontSize

        self.setStyleSheet(f"""
            QPushButton {{
                border: none;
                border-radius: 35px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 {self._current_color1.name()},
                    stop: 1 {self._current_color2.name()}
                );
                font: 700 {self._current_fontSize}pt "Arial Narrow";
            }}
        """)

        # Crear animación para la transición de ambos colores
        tAnimacion = 1000
        self.hover_animation1 = QPropertyAnimation(self, b"hover_color1")
        self.hover_animation1.setDuration(tAnimacion)
        self.hover_animation1.setEasingCurve(QEasingCurve.InOutQuad)

        self.hover_animation2 = QPropertyAnimation(self, b"hover_color2")
        self.hover_animation2.setDuration(tAnimacion)
        self.hover_animation2.setEasingCurve(QEasingCurve.InOutQuad)
        
        self.hover_animation3 = QPropertyAnimation(self, b"hover_fontSize")
        self.hover_animation3.setDuration(250)
        self.hover_animation3.setEasingCurve(QEasingCurve.InOutQuad) # InQuad, InOutQuad, InCubic, InOutExpo, OutInBack

    def event(self, event):
        """ Captura eventos hover y animación """
        if event.type() == QEvent.Enter:  # Cuando el mouse entra
            self.stopColorAnimation()
            self.startColorAnimation(self._hover_color1, self._hover_color2, self._hover_fontSize)
        elif event.type() == QEvent.Leave:  # Cuando el mouse sale
            self.stopColorAnimation()
            self.startColorAnimation(self._backGroundColor1, self._backGroundColor2, self._fontSize)  # Volver a los colores originales
        return super().event(event)

    def startColorAnimation(self, end_color1, end_color2, fontSize):
        """ Inicia la animación de los dos colores """
        self.hover_animation1.setStartValue(self._current_color1)
        self.hover_animation1.setEndValue(end_color1)

        self.hover_animation2.setStartValue(self._current_color2)
        self.hover_animation2.setEndValue(end_color2)
        
        self.hover_animation3.setStartValue(self._current_fontSize)
        self.hover_animation3.setEndValue(fontSize)

        # Ejecutar las animaciones
        self.hover_animation1.start()
        self.hover_animation2.start()
        self.hover_animation3.start()
        
    def stopColorAnimation(self):
        self.hover_animation1.stop()
        self.hover_animation2.stop()
        self.hover_animation3.stop()

    # Getters y Setters para los colores del gradiente
    def get_hover_color1(self):
        return self._current_color1

    def set_hover_color1(self, color):
        """ Actualiza el color superior del gradiente """
        self._current_color1 = color
        self.updateGradient()

    def get_hover_color2(self):
        return self._current_color2

    def set_hover_color2(self, color):
        """ Actualiza el color inferior del gradiente """
        self._current_color2 = color
        #self.updateGradient()
        
    def get_fontFize(self):
        return self._current_fontSize
    
    def set_fontSize(self, size):
        self._current_fontSize = size
        # self.updateGradient()

    def updateGradient(self):
        """ Actualiza el gradiente con los colores actuales """
        self.setStyleSheet(f"""
            QPushButton {{
                border: none;
                border-radius: 35px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 {self._current_color1.name()},
                    stop: 1 {self._current_color2.name()}
                );
                font: 700 {self._current_fontSize}pt "Arial Narrow";
            }}
        """)

    # Definir las propiedades para las animaciones
    hover_color1 = Property(QColor, get_hover_color1, set_hover_color1)
    hover_color2 = Property(QColor, get_hover_color2, set_hover_color2)
    hover_fontSize = Property(float, get_fontFize, set_fontSize)