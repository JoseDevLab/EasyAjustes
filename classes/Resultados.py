import math
from PySide6.QtWidgets import QWidget,QSizePolicy,QVBoxLayout,QSpacerItem
from classes.ui_Resultados import Ui_resultados
from classes.ResultadoAjuste import ResultadoAjuste
from classes.ResultadoTxt import ResultadoTxt

class Resultados(QWidget,Ui_resultados):
    def __init__(self,parent:QWidget|None=...):
        super().__init__(parent)
        self.setupUi(self)
        self.estadoTxt = {}
        self.listaPaths = []
        self.idResultados = 0
        self.btPagAnterior.clicked.connect(self.retrocederPagina)
        self.btPagSiguiente.clicked.connect(self.avanzarPagina)
        
    def setResultados(self,estadoTxt:dict,listaPaths:list,idResultados:int):
        if self.idResultados != idResultados:
            self.estadoTxt = estadoTxt
            self.listaPaths = listaPaths
            self.idResultados = idResultados
            resultadoTxt = self.vlResultados.takeAt(1).widget()
            resultadoTxt.deleteLater()
            pages = [self.swResultados.widget(i) for i in range(self.swResultados.count())]
            for page in pages:
                self.swResultados.removeWidget(page)
            page1 = QWidget()
            # page1.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
            layout = QVBoxLayout(page1)
            layout.setContentsMargins(0,0,0,0)
            if len(listaPaths)<=10:
                self.frPaginas.setVisible(False)
                self.hlTituloResultados.setStretch(3,1)
            else:
                self.frPaginas.setVisible(True)
                self.hlTituloResultados.setStretch(3,2)
                self.lbPaginas.setText(f'1 al 10 de {len(listaPaths)}')
                self.btPagAnterior.setEnabled(False)
                self.btPagSiguiente.setEnabled(True)
            # layout.addWidget(ResultadoTxt(estadoTxt,self))
            self.vlResultados.insertWidget(1,ResultadoTxt(estadoTxt,self))
            for path in (listaPaths if len(listaPaths)<=10 else listaPaths[:10]):
                layout.addWidget(ResultadoAjuste(path,self))
            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout.addItem(spacer)
            self.swResultados.addWidget(page1)
            
    def avanzarPagina(self):
        n = len(self.listaPaths)
        nPag = math.ceil(n/10)
        pagActual = self.swResultados.currentIndex()
        pagCreadas = self.swResultados.count()
        if pagActual == 0:
            self.btPagAnterior.setEnabled(True)
        if pagActual+2==nPag:
            self.btPagSiguiente.setEnabled(False)
        desde = (pagActual+1)*10
        hasta = (pagActual+2)*10
        self.lbPaginas.setText(f'{desde+1} al {n if pagActual+2==nPag else hasta} de {n}')
        if pagCreadas < nPag:
            if pagActual+1 == pagCreadas:
                page = QWidget()
                # page.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
                layout = QVBoxLayout(page)
                layout.setContentsMargins(0,0,0,0)
                paths = self.listaPaths[desde:] if pagActual+2==nPag else self.listaPaths[desde:hasta]
                for path in paths:
                    layout.addWidget(ResultadoAjuste(path,self))
                spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer)
                self.swResultados.addWidget(page)
        self.swResultados.setCurrentIndex(pagActual+1)
                
    def retrocederPagina(self):
        n = len(self.listaPaths)
        nPag = math.ceil(n/10)
        pagActual = self.swResultados.currentIndex()
        if pagActual+1==nPag:
            self.btPagSiguiente.setEnabled(True)
        if pagActual == 1:
            self.btPagAnterior.setEnabled(False)
        desde = (pagActual-1)*10
        hasta = (pagActual)*10
        self.lbPaginas.setText(f'{desde+1} al {hasta} de {n}')
        self.swResultados.setCurrentIndex(pagActual-1)