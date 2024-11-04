import math
from pathlib import Path
from PySide6.QtWidgets import QWidget,QDialog, QVBoxLayout, QSpacerItem, QSizePolicy, QMessageBox, QDialogButtonBox, QStackedWidget
from PySide6.QtCore import Signal, QFileInfo
from classes.ui_VerPaths import Ui_verPaths
from classes.EditarDestino import EditarDestino

class VerPaths(QDialog, Ui_verPaths):
    pathsEditados = Signal(str,list)
    def __init__(self,txtPaths,listaPaths,parent:QWidget|None):
        super().__init__(parent)
        self.setupUi(self)
        
        # Se cambian los textos de los botones 'Ok' y 'Cancel'
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Registrar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')
        self.frEditarVarios.setVisible(False)
        
        self.txtPaths = txtPaths
        self.listaPaths = listaPaths
        self.indexChecked = []
        
        self.tePaths.setPlainText(txtPaths)
        
        self.buttonBox.accepted.connect(self.aceptado)
        self.btValidar.clicked.connect(self.validarPaths)
        self.btEditSeleccion.clicked.connect(self.editarSeleccionados)
        self.btPagSiguiente.clicked.connect(self.avanzarPagina)
        self.btPagAnterior.clicked.connect(self.retrocederPagina)
        
        self.vlEditar = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vlEditar.setContentsMargins(5,5,5,5)
        self.cargarEdicionInicial()
        self.cargarCarpetasComunes()
        
    def cargarEdicionInicial(self):
        while self.vlEditar.count():
            child = self.vlEditar.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.swEditar = QStackedWidget(self)
        self.swEditar.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
        page1 = QWidget()
        page1.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
        layout1 = QVBoxLayout(page1)
        layout1.setContentsMargins(0,0,0,0)
        if len(self.listaPaths)<=10:
            self.frPaginas.setVisible(False)
            self.hlTituloDestinos.setStretch(3,1)
        else:
            self.frPaginas.setVisible(True)
            self.hlTituloDestinos.setStretch(3,2)
            self.lbPaginas.setText(f'1 al 10 de {len(self.listaPaths)}')
            self.btPagAnterior.setEnabled(False)
            self.btPagSiguiente.setEnabled(True)
        for path in (self.listaPaths if len(self.listaPaths)<=10 else self.listaPaths[:10]):
            editarDestino = EditarDestino(path)
            editarDestino.cambioSeleccion.connect(self.checkClicked)
            editarDestino.editado.connect(lambda:self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True))
            layout1.addWidget(editarDestino)
        self.swEditar.addWidget(page1)
        self.vlEditar.addWidget(self.swEditar)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vlEditar.addItem(spacer)
        
    def avanzarPagina(self):
        n = len(self.listaPaths)
        nPag = math.ceil(n/10)
        pagActual = self.swEditar.currentIndex()
        pagCreadas = self.swEditar.count()
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
                page.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
                layout = QVBoxLayout(page)
                layout.setContentsMargins(0,0,0,0)
                paths = self.listaPaths[desde:] if pagActual+2==nPag else self.listaPaths[desde:hasta]
                for path in paths:
                    editarDestino = EditarDestino(path)
                    editarDestino.cambioSeleccion.connect(self.checkClicked)
                    editarDestino.editado.connect(lambda:self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True))
                    layout.addWidget(editarDestino)
                if pagActual+2==nPag:
                    spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                    layout.addItem(spacer)
                self.swEditar.addWidget(page)
        self.swEditar.setCurrentIndex(pagActual+1)
                
    def retrocederPagina(self):
        n = len(self.listaPaths)
        nPag = math.ceil(n/10)
        pagActual = self.swEditar.currentIndex()
        if pagActual+1==nPag:
            self.btPagSiguiente.setEnabled(True)
        if pagActual == 1:
            self.btPagAnterior.setEnabled(False)
        desde = (pagActual-1)*10
        hasta = (pagActual)*10
        self.lbPaginas.setText(f'{desde+1} al {hasta} de {n}')
        self.swEditar.setCurrentIndex(pagActual-1)
            
        
    def aceptado(self):
        n = len(self.listaPaths)
        nPag = math.ceil(n/10)
        i = 0
        for j in range(self.swEditar.count()):
            if j+1==nPag:
                m = n-10*j
            else:
                m = 10
            for k in range(m):
                widget = self.getEditarDestinoAt(i)
                strConstruir = f'UNIDAD/{widget.leConstruir.text()}/{widget.leArchivo.text()}'
                self.listaPaths[i]['pathConstruir'] = QFileInfo(strConstruir)
                i += 1
        self.pathsEditados.emit(self.txtPaths,self.listaPaths)
        
    def validarPaths(self):
        msgBox = QMessageBox(self)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        try:
            txtPaths = self.tePaths.toPlainText()
            paths = [linea.strip().replace('\\','/') for linea in txtPaths.splitlines()]
            paths = [path for path in paths if path]
            paths1 = [path.split(':')[-1] for path in paths]
            paths1 = ['UNIDAD/'+path if path[0]!='/' else 'UNIDAD'+path for path in paths1]
            listaPaths = []
            for i in range(len(paths)):
                path0 = QFileInfo(paths[i])
                if not (Path(path0.filePath()).is_absolute()):
                    raise Exception(f"El Path número <b>{i+1}</b> debe ser absoluto.")
                if not path0.exists():
                    raise Exception(f"El Path número <b>{i+1}</b> apunta a un archivo que no existe.")
                
                path1 = QFileInfo(paths1[i])
                listaPaths.append({
                    'pathOrigen': path0,
                    'pathConstruir': path1,
                    'pathDestino': '',
                    'numeracion': f'{i+1}',
                    'copiado': False,
                    'mensaje': ''
                })
            self.listaPaths = listaPaths
            self.txtPaths = txtPaths
            self.indexChecked = []
            self.cargarEdicionInicial()
            self.cargarCarpetasComunes()
            msgBox.setWindowTitle("Todo bien 👍.")
            msgBox.setText("Todos los paths son válidos 🎉.")
            msgBox.setInformativeText(f"Puede continuar modificando los destinos de ser necesario y registrar.")
            msgBox.setIcon(QMessageBox.Information)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        except Exception as e:
            msgBox.setWindowTitle("Path no válido 😢.")
            msgBox.setText("Verifique que los paths sean correctos 👀.")
            msgBox.setInformativeText(f"{str(e)}")
            msgBox.setIcon(QMessageBox.Warning)
        msgBox.exec()
        
    def checkClicked(self,index,isChecked):
        if isChecked:
            self.indexChecked.append(index)
        else:
            self.indexChecked.remove(index)
        if len(self.indexChecked) > 0:
            self.frEditarVarios.setVisible(True)
        else:
            self.frEditarVarios.setVisible(False)
            
    def editarSeleccionados(self):
        strConstruir = self.leSeleccion.text()
        for i in self.indexChecked:
            # editarDestino = self.vlEditar.itemAt(i).widget()
            editarDestino = self.getEditarDestinoAt(i)
            editarDestino.leConstruir.setText(strConstruir)
            editarDestino.leConstruir.setToolTip(strConstruir)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        
    def getEditarDestinoAt(self,index):
        indexPag = int((index)/10)
        indexWid = index-10*indexPag
        page = self.swEditar.widget(indexPag)
        editarDestino = page.layout().itemAt(indexWid).widget()
        return editarDestino

    def cargarCarpetasComunes(self):
        comunes = ''
        carpetas1 = []
        for i in range(len(self.listaPaths)):
            file = self.listaPaths[i]
            qFile = file['pathConstruir']
            carpetas = qFile.path().split('/')
            if i!=0:
                if len(carpetas) < len(carpetas1):
                    carpetas1 = carpetas
                    i0 = i
            else:
                carpetas1 = carpetas
                i0 = i
        for i in range(len(carpetas1)-1):
            carpeta1 = carpetas1[i+1]
            comun = True
            for j in range(len(self.listaPaths)):
                file = self.listaPaths[j]
                if j!=i0:
                    qFile = file['pathConstruir']
                    carpetas2 = qFile.path().split('/')
                    if carpetas2[i+1] != carpeta1:
                        comun = False
                        break
            if comun:
                comunes += ('/' if comunes!='' else '')
                comunes += carpeta1
            else:
                break
        if comunes!='':
            self.leSeleccion.setText(comunes)