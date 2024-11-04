import sys
import json
import subprocess
import copy
from pathlib import Path
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressDialog, QMessageBox, QPushButton, QMenu
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QStandardPaths, QFileInfo, QSize, Qt, QDateTime, QDate, QTime
from classes.ui_MainWindow import Ui_EasyAjustes
from classes.AcercaDe import AcercaDe
from classes.Threads import CrearAjuste, FiltrarArchivosPorFecha, CargandoArchivo, CargandoComunes
from classes.ResultadoAjuste import ResultadoAjuste
from classes.ResultadoTxt import ResultadoTxt
from classes.VerPaths import VerPaths

class EasyAjustes(QMainWindow, Ui_EasyAjustes):

    listaPaths = []
    txtPaths = ''
    estadoTxt = {}
    idResultados = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        ahora = QDateTime.currentDateTime()
        self.sugerirCli()
        
        self.btVerResultados.setVisible(False)
        self.btNuevoAjuste_2.setVisible(False)
        self.btNuevoAjuste.setVisible(False)
        self.lbFechaInicial.setVisible(False)
        self.lbFechaFinal.setVisible(False)
        self.dteInicial.setVisible(False)
        self.dteFinal.setVisible(False)
        hace_30min = ahora.addSecs(-30 * 60)
        mas_10min = ahora.addSecs(10 * 60)
        mas_30min = ahora.addSecs(30 * 60)
        self.dteInicial.setDateTime(hace_30min)
        self.dteFinal.setDateTime(mas_10min)
        self.dteInicial.setMaximumDateTime(mas_30min)
        self.dteFinal.setMaximumDateTime(mas_30min)
        self.rbArchivoTxt.setStyleSheet('QRadioButton {font-weight: bold;}')
        
        self.progress_dialog = QProgressDialog("Cargando...", None, 0, 100,self)
        self.cancel_button = QPushButton("Cancelar")
        self.progress_dialog.setCancelButton(self.cancel_button)
        # Quitar el botón de cierre (la "X")
        self.progress_dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.progress_dialog.setModal(True)
        self.progress_dialog.setAutoClose(False)
        self.progress_dialog.setAutoReset(False)
        self.progress_dialog.close() 
        
        self.btVerResultados.clicked.connect(self.verResultados)
        self.btNuevoAjuste_2.clicked.connect(self.nuevoAjuste)
        self.btAcercaDe.clicked.connect(lambda: AcercaDe(self).exec())
        self.actionAcercaDe.triggered.connect(lambda: AcercaDe(self).exec())
        self.btSugerir.clicked.connect(self.sugerirCli)
        self.btSelecTxt.clicked.connect(self.seleccionarCli)
        self.btSelecDest.clicked.connect(self.seleccionarSalida)
        self.btCrearAjuste.clicked.connect(self.crearAjuste)
        self.leSigla.textEdited.connect(lambda text:self.leSigla.setText(text.upper()))
        self.btNuevoAjuste.clicked.connect(self.nuevoAjuste)
        self.btVer.clicked.connect(self.verPaths)
        self.cbSiglas.currentIndexChanged.connect(self.cbSiglasCli)
        self.rbArchivoTxt.clicked.connect(self.radioChanged)
        self.rbBusquedaFecha.clicked.connect(self.radioChanged)
        self.dteInicial.dateTimeChanged.connect(self.dteInicialChanged)
        self.dteFinal.dateTimeChanged.connect(self.dteFinalChanged)
        self.actionLimpiar_historial.triggered.connect(self.limpiarHistorial)
        self.actionSalir.triggered.connect(lambda:self.close())
        
        self.config = self.leer_json('_internal/data/config.json')
        
        if 'siglas' in self.config and type(self.config['siglas'])==list and len(self.config['siglas'])>0:
            self.leSigla.setVisible(False)
            siglas = self.config['siglas']
            for sigla in siglas:
                self.cbSiglas.addItem(sigla)
            self.cbSiglas.setCurrentIndex(1)
        else:
            self.cbSiglas.setVisible(False)
            
        if 'carpetasInicialesFavoritas' in self.config and type(self.config['carpetasInicialesFavoritas'])==list and len(self.config['carpetasInicialesFavoritas'])>0:
            self.carpetasFavoritas = self.config['carpetasInicialesFavoritas']
        else:
            self.carpetasFavoritas = []
            
        self.ultimoPathArchivo = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        if 'ultimoPathArchivo' in self.config and type(self.config['ultimoPathArchivo'])==str and self.config['ultimoPathArchivo']!='':
            path = Path(self.config['ultimoPathArchivo'])
            if path.exists() and path.is_dir():
                self.ultimoPathArchivo = self.config['ultimoPathArchivo']
            else:
                self.config.update({'ultimoPathArchivo': self.ultimoPathArchivo})
                self.escribir_json('_internal/data/config.json',self.config)
                
        self.ultimoPathBusqueda = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        if 'ultimoPathBusqueda' in self.config and type(self.config['ultimoPathBusqueda'])==str and self.config['ultimoPathBusqueda']!='':
            path = Path(self.config['ultimoPathBusqueda'])
            if path.exists() and path.is_dir():
                self.ultimoPathBusqueda = self.config['ultimoPathBusqueda']
            else:
                self.config.update({'ultimoPathBusqueda': self.ultimoPathBusqueda})
                self.escribir_json('_internal/data/config.json',self.config)
            
        self.ultimoPathDestino = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        if 'ultimoPathDestino' in self.config and type(self.config['ultimoPathDestino'])==str and self.config['ultimoPathDestino']!='':
            path = Path(self.config['ultimoPathDestino'])
            if path.exists() and path.is_dir():
                self.ultimoPathDestino = self.config['ultimoPathDestino']
            else:
                self.config.update({'ultimoPathDestino': self.ultimoPathDestino})
                self.escribir_json('_internal/data/config.json',self.config)
        self.leDirecSelec.setText(self.ultimoPathDestino)
        
        self.historial = []
        hisJson = self.leer_json('_internal/data/historial.json')
        if 'historial' in hisJson and type(hisJson['historial'])==list and len(hisJson['historial'])>0:
            self.historial = hisJson['historial']
        self.cargarMenuHistorial()
        
    def leer_json(self,ruta_archivo:str):
        ruta_archivo = Path(ruta_archivo)
        datos = {}
        try:
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"El archivo {ruta_archivo} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {ruta_archivo}.")
        return datos
            
    def escribir_json(self,ruta_archivo:str, datos:dict):
        ruta_archivo = Path(ruta_archivo)
        try:
            with ruta_archivo.open('w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al escribir en el archivo JSON: {str(e)}")
            
        
            
    def cbSiglasCli(self, index):
        if index == 0:
            self.cbSiglas.setVisible(False)
            self.leSigla.setVisible(True)
    
    def sugerirCli(self):
        ahora = QDateTime.currentDateTime()
        self.deFecha.setDate(ahora.date())
        self.teHora.setTime(ahora.time())
        self.leSigla.setText("NN")
        
    def radioChanged(self):
        if self.rbArchivoTxt.isChecked():
            self.rbArchivoTxt.setStyleSheet('QRadioButton {font-weight: bold;}')
            self.rbBusquedaFecha.setStyleSheet('')
            self.lbFechaInicial.setVisible(False)
            self.lbFechaFinal.setVisible(False)
            self.dteInicial.setVisible(False)
            self.dteFinal.setVisible(False)
            self.swSeleccionar.setCurrentIndex(0)
            self.lbRuta.setText('TXT con rutas de archivos')
        else:
            self.rbBusquedaFecha.setStyleSheet('QRadioButton {font-weight: bold;}')
            self.rbArchivoTxt.setStyleSheet('')
            self.lbFechaInicial.setVisible(True)
            self.lbFechaFinal.setVisible(True)
            self.dteInicial.setVisible(True)
            self.dteFinal.setVisible(True)
            self.swSeleccionar.setCurrentIndex(1)
            self.lbRuta.setText('Búsqueda de archivos por fecha de modificación')
            
    def dteInicialChanged(self, dateTime):
        ahora = QDateTime.currentDateTime()
        mas_30min = ahora.addSecs(30 * 60)
        self.dteInicial.setMaximumDateTime(mas_30min)
        
    def dteFinalChanged(self, dateTime):
        ahora = QDateTime.currentDateTime()
        mas_30min = ahora.addSecs(30 * 60)
        self.dteFinal.setMaximumDateTime(mas_30min)

    def seleccionarCli(self):
        if self.rbArchivoTxt.isChecked():
            self.chbIncluirCarp.isChecked()
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Abrir archivo",
                self.ultimoPathArchivo,
                "Archivos de texto (*.txt)"
            )
            if file_path!='':
                self.ultimoPathArchivo = QFileInfo(file_path).path()
                self.progress_dialog.setFixedSize(QSize(600,200))
                cargandoArchivo = CargandoArchivo(file_path,self)
                cargandoArchivo.update_rangeProgress.connect(self.progress_dialog.setRange)
                cargandoArchivo.update_titleProgress.connect(self.progress_dialog.setWindowTitle)
                cargandoArchivo.update_textProgress.connect(self.progress_dialog.setLabelText)
                cargandoArchivo.update_progress.connect(self.progress_dialog.setValue)
                cargandoArchivo.update_cancelEnabled.connect(self.cancel_button.setEnabled)
                cargandoArchivo.finalized.connect(self.cargaTxtCompleta)
                self.progress_dialog.canceled.connect(cargandoArchivo.stop)
                self.progress_dialog.show()
                cargandoArchivo.start()
                    
        elif self.rbBusquedaFecha.isChecked():
            directorio = QFileDialog.getExistingDirectory(
                self, 
                "Seleccionar directorio de búsqueda",
                self.ultimoPathBusqueda
            )
            if directorio:
                self.ultimoPathBusqueda = directorio
                self.progress_dialog.setFixedSize(QSize(600,150))
                buscando = FiltrarArchivosPorFecha(directorio,self)
                buscando.update_rangeProgress.connect(self.progress_dialog.setRange)
                buscando.update_titleProgress.connect(self.progress_dialog.setWindowTitle)
                buscando.update_textProgress.connect(self.progress_dialog.setLabelText)
                buscando.update_progress.connect(self.progress_dialog.setValue)
                buscando.update_cancelEnabled.connect(self.cancel_button.setEnabled)
                buscando.finalized.connect(self.busquedaCompleta)
                self.progress_dialog.canceled.connect(buscando.stop)
                self.progress_dialog.show()
                buscando.start()
                
    def cargaTxtCompleta(self,respuesta:dict):
        self.progress_dialog.close()
        self.progress_dialog.canceled.disconnect()
        self.btVerResultados.setVisible(False)
        self.btNuevoAjuste_2.setVisible(False)
        msgBox = QMessageBox(self)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        correcto = respuesta['correcto']
        if correcto:
            self.leArchSelec.setText(respuesta['file_path'])
            self.leDirecBus.setText('')
            self.txtPaths = respuesta['txtPaths']
            self.listaPaths = respuesta['listaPaths']
            comunes = respuesta['comunes']
            self.setComunes(comunes)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Archivo cargado correctamete 👌.")
            msgBox.setText(f"Se cargaron <b>{len(self.listaPaths)}</b> paths correctamente.")
            msgBox.setInformativeText(f"Puede ver los <B>{len(self.listaPaths)}</b> paths cargados presionando en el botón de <b>Ver/Editar Paths.</b>")
            msgBox.exec()
        else:
            e = respuesta['e']
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("No se cargó el archivo 😢.")
            msgBox.setText("Ocurrió un error al cargar el archivo.\nVerifique el contenido del archivo 👀.")
            msgBox.setInformativeText(f"{str(e)}")
            msgBox.exec()
                
    def busquedaCompleta(self,respuesta:dict):
        self.progress_dialog.close()
        self.progress_dialog.canceled.disconnect()
        self.btVerResultados.setVisible(False)
        self.btNuevoAjuste_2.setVisible(False)
        msgBox = QMessageBox(self)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        if respuesta['correcto']:
            directorio = respuesta['directorio']
            txtPaths = respuesta['txtPaths']
            listaPaths = respuesta['listaPaths']
            comunes = respuesta['comunes']
            msgBox.setWindowTitle(f"Busqueda Completa.")
            msgBox.setText(f"Se encontraron <b>{len(listaPaths)}</b> archivos.")
            if len(listaPaths)>0:
                self.leDirecBus.setText(directorio)
                self.leArchSelec.setText('')
                self.txtPaths = txtPaths
                self.listaPaths = listaPaths
                self.setComunes(comunes)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setInformativeText(f"Paths de archivos seleccionados correctamente 👌.")
                msgBox.exec()
            else:
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setInformativeText(f"No se encontraron archivos en la ruta y fechas específicas.")
                msgBox.exec()
        else:
            msgBox.setWindowTitle(f"La búsqueda no se completó.")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(f"Causa de la interrupción: ")
            msgBox.setInformativeText(f"<b>{respuesta['e']}</b>")
            msgBox.exec()

    def seleccionarSalida(self):
        directorio = QFileDialog.getExistingDirectory(
            self, 
            "Seleccionar directorio dónde guardar el ajuste. 💾",
            self.ultimoPathDestino
        )
        if directorio:
            self.leDirecSelec.setText(directorio)
            self.ultimoPathDestino = directorio
        
    def crearAjuste(self):
        try:
            if self.leSigla.isVisible() and not (len(self.leSigla.text())==2 or len(self.leSigla.text())==3):
                raise Exception('La sigla debe tener 2 o 3 caracteres.')
            if len(self.listaPaths)<=0:
                raise Exception('Debe establecer las rutas de los archivos.')
            if self.cbCarpetaIni.currentText()=='':
                raise Exception('Debe seleccionar la carpeta inicial.')
            if self.teDetalles.toPlainText()=='':
                raise Exception('Debe ingresar una descripción.')
            
            self.progress_dialog.setFixedSize(QSize(600,200))
            self.progress_dialog.setWindowTitle("Creando ajuste...")
            self.progress_dialog.setRange(0,0)
            creandoAjuste = CrearAjuste(self)
            creandoAjuste.update_progress.connect(self.progress_dialog.setValue)
            creandoAjuste.update_textProgress.connect(self.progress_dialog.setLabelText)
            creandoAjuste.update_cancelEnabled.connect(self.cancel_button.setEnabled)
            creandoAjuste.update_rangeProgress.connect(self.progress_dialog.setRange)
            creandoAjuste.finalized.connect(self.ajusteCompletado)
            self.progress_dialog.canceled.connect(creandoAjuste.stop)
            self.progress_dialog.show()
            creandoAjuste.start()
        except Exception as e:
            msgBox = QMessageBox(self)
            msgBox.setWindowTitle("Advertencia")
            msgBox.setText(f"Advertencia: {str(e)}")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec()
            
    def ajusteCompletado(self):
        self.progress_dialog.close()
        self.progress_dialog.canceled.disconnect()
        self.btCrearAjuste.setVisible(False)
        self.btNuevoAjuste.setVisible(True)
        self.btNuevoAjuste_2.setVisible(True)
        self.btVerResultados.setVisible(False)
        self.idResultados += 1
        self.resultados.setResultados(self.estadoTxt,self.listaPaths,self.idResultados)
        if self.leSigla.isVisible():
            sigla = self.leSigla.text()
        elif self.cbSiglas.isVisible():
            sigla = self.cbSiglas.currentText()
        self.swPaneles.setCurrentIndex(1)
        for i in range(self.cbSiglas.count()-1):
            cbSigla = self.cbSiglas.itemText(i+1)
            if cbSigla == sigla:
                self.cbSiglas.removeItem(i+1)
                break
        self.cbSiglas.insertItem(1,sigla)
        self.leSigla.setVisible(False)
        self.cbSiglas.setVisible(True)
        self.cbSiglas.setCurrentIndex(1)
        siglas = []
        for i in range(self.cbSiglas.count()-1):
            siglas.append(self.cbSiglas.itemText(i+1))
        listaPaths = []
        for path in self.listaPaths:
            listaPaths.append({
                'pathOrigen': path['pathOrigen'].filePath(),
                'pathConstruir': path['pathConstruir'].filePath(),
                'pathDestino': path['pathDestino'],
                'numeracion': path['numeracion'],
                'copiado': path['copiado'],
                'mensaje': path['mensaje']
            })
        registroAjuste = {
            'numeracion': self.sbNumeracion.value(),
            'fecha': [self.deFecha.date().day(),self.deFecha.date().month(),self.deFecha.date().year()],
            'hora': [self.teHora.time().hour(),self.teHora.time().minute()],
            'sigla': siglas[0],
            'radioPathsArchivo': self.rbArchivoTxt.isChecked(),
            'pathArchivo': self.leArchSelec.text(),
            'ultimoPathArchivo':self.ultimoPathArchivo,
            'ultimoPathBusqueda':self.ultimoPathBusqueda,
            'ultimoPathDestino':self.ultimoPathDestino,
            'carpetasComunes': [self.cbCarpetaIni.itemText(i) for i in range(self.cbCarpetaIni.count())],
            'cbCarpetaIniIndice': self.cbCarpetaIni.currentIndex(),
            'incluirCarpetaChecked': self.chbIncluirCarp.isChecked(),
            'descripcion': self.teDetalles.toPlainText(),
            'txtPaths': self.txtPaths,
            'estadoTxt': self.estadoTxt,
            'listaPaths': listaPaths
        }
        upConfig = {
            'siglas':siglas,
            'ultimoPathArchivo':self.ultimoPathArchivo,
            'ultimoPathBusqueda':self.ultimoPathBusqueda,
            'ultimoPathDestino':self.ultimoPathDestino
        }
        self.config.update(upConfig)
        self.escribir_json('_internal/data/config.json',self.config)
        self.historial.insert(0,registroAjuste)
        self.escribir_json('_internal/data/historial.json',{'historial':self.historial})
        self.cargarMenuHistorial()

    def nuevoAjuste(self):
        self.swPaneles.setCurrentIndex(0)
        self.btCrearAjuste.setVisible(True)
        self.btVerResultados.setVisible(True)
        self.btNuevoAjuste.setVisible(False)
        self.btNuevoAjuste_2.setVisible(False)
                
    def verResultados(self):
        self.swPaneles.setCurrentIndex(1)
        self.btNuevoAjuste.setVisible(True)
        self.btNuevoAjuste_2.setVisible(True)
        self.btCrearAjuste.setVisible(False)
        self.btVerResultados.setVisible(False)
        self.resultados.setResultados(self.estadoTxt,self.listaPaths,self.idResultados)
            
    def verPaths(self):
        ver = VerPaths(self.txtPaths,self.listaPaths,self)
        ver.pathsEditados.connect(self.pathsEditados)
        ver.exec()
        
    def pathsEditados(self, txt:str, paths:list):
        if len(paths)>0:
            self.btVerResultados.setVisible(False)
            self.btNuevoAjuste_2.setVisible(False)
            self.txtPaths = txt
            self.listaPaths = paths
            cargandoComunes = CargandoComunes(paths,self)
            cargandoComunes.update_rangeProgress.connect(self.progress_dialog.setRange)
            cargandoComunes.update_titleProgress.connect(self.progress_dialog.setWindowTitle)
            cargandoComunes.update_textProgress.connect(self.progress_dialog.setLabelText)
            cargandoComunes.update_progress.connect(self.progress_dialog.setValue)
            cargandoComunes.update_cancelEnabled.connect(self.cancel_button.setEnabled)
            cargandoComunes.finalized.connect(self.comunesCargadas)
            self.progress_dialog.show()
            cargandoComunes.start()

    def comunesCargadas(self,comunes:list):
        self.progress_dialog.close()
        self.setComunes(comunes)
        if self.leArchSelec.text()=='':
            self.leArchSelec.setPlaceholderText('Paths agregados manualmente.')
    
    def setComunes(self,comunes:list):
        if len(comunes)>0:
            self.cbCarpetaIni.clear()
            self.cbCarpetaIni.insertItems(0,comunes)
            i = 0
            for favorita in self.carpetasFavoritas:
                if favorita in comunes:
                    i = comunes.index(favorita)
                    break
            self.cbCarpetaIni.setCurrentIndex(i)
        else:
            self.cbCarpetaIni.clear()
            
    def cargarMenuHistorial(self):
        n = len(self.historial)
        self.menuHistorial.clear()
        if n>0:
            for i in range(n):
                registroAjuste = self.historial[i]
                pathAjuste = registroAjuste['estadoTxt']['pathTxt']
                pathAjuste = QFileInfo(pathAjuste).path()
                menuAjuste = self.menuHistorial.addMenu(pathAjuste)
                menuAjuste.setIcon(QIcon(':icons/resources/images/adjust.svg'))
                actionCargar = QAction(QIcon(":icons/resources/images/load.svg"), "Cargar ajuste", self)
                actionAbrir = QAction(QIcon(":icons/resources/images/folder.svg"), "Abrir carpeta", self)
                actionCargar.triggered.connect(partial(self.cargarAjuste, i))
                actionAbrir.triggered.connect(partial(self.abrir, pathAjuste))
                menuAjuste.addAction(actionCargar)
                menuAjuste.addAction(actionAbrir)
        else:
            actionVacio = QAction(QIcon(":icons/resources/images/empty.svg"),'Vacío',self)
            self.menuHistorial.addAction(actionVacio)
        
    def cargarAjuste(self,index):
        self.swPaneles.setCurrentIndex(0)
        self.btVerResultados.setVisible(True)
        self.btCrearAjuste.setVisible(True)
        self.btNuevoAjuste_2.setVisible(False)
        self.btNuevoAjuste.setVisible(False)
        reg = self.historial[index]
        self.sbNumeracion.setValue(reg['numeracion'])
        fecha = reg['fecha']
        self.deFecha.setDate(QDate(fecha[2],fecha[1],fecha[0]))
        hora = reg['hora']
        self.teHora.setTime(QTime(hora[0],hora[1]))
        self.cbSiglas.setCurrentText(reg['sigla'])
        self.leSigla.setText(reg['sigla'])
        if reg['radioPathsArchivo']:
            self.rbArchivoTxt.setChecked(True)
        else:
            self.rbBusquedaFecha.setChecked(True)
        self.radioChanged()
        self.leArchSelec.setText(reg['pathArchivo'])
        self.ultimoPathArchivo = reg['ultimoPathArchivo']
        self.ultimoPathBusqueda = reg['ultimoPathBusqueda']
        self.leDirecBus.setText(reg['ultimoPathBusqueda'])
        self.ultimoPathDestino = reg['ultimoPathDestino']
        self.leDirecSelec.setText(reg['ultimoPathDestino'])
        self.setComunes(reg['carpetasComunes'])
        self.cbCarpetaIni.setCurrentIndex(reg['cbCarpetaIniIndice'])
        self.chbIncluirCarp.setChecked(reg['incluirCarpetaChecked'])
        self.teDetalles.setPlainText(reg['descripcion'])
        self.estadoTxt = reg['estadoTxt']
        self.txtPaths = reg['txtPaths']
        listaPaths = reg['listaPaths']
        listaPaths_2 = []
        for path in listaPaths:
            path['pathOrigen'] = QFileInfo(path['pathOrigen'])
            path['pathConstruir'] = QFileInfo(path['pathConstruir'])
            listaPaths_2.append(path)
        self.listaPaths = listaPaths_2
        self.idResultados += 1
        
    def limpiarHistorial(self):
        self.historial = []
        self.escribir_json('_internal/data/historial.json',{'historial':self.historial})
        self.cargarMenuHistorial()

    def abrir(self, folder_path):
        error = ''
        try:
            if not Path(folder_path).exists():
                raise FileNotFoundError('La carpeta ya no existe.')
            if sys.platform.startswith('win'):
                subprocess.Popen(f'explorer "{folder_path.replace("/","\\")}"')
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', folder_path])
            elif sys.platform.startswith('linux'):
                subprocess.Popen(['xdg-open', folder_path])
            else:
                error = "Error: Sistema operativo no soportado."
        except FileNotFoundError as e:
            error = f"Error: Carpeta no encontrada: {e}"
        except PermissionError as e:
            error = f"Error: Permisos insuficientes: {e}"
        except OSError as e:
            error = f"Error del sistema operativo: {e}"
        except subprocess.SubprocessError as e:
            error = f"Error en la ejecución del proceso: {e}"
        except ValueError as e:
            error = f"Error: Valor inválido: {e}"
        except Exception as e:
            error = f'Error: {e}'
        if error!='':
            msgBox = QMessageBox(self)
            msgBox.setWindowTitle("No pudo abrirse la carpeta")
            msgBox.setText(f"{str(error)}")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    easyAjustes = EasyAjustes()
    easyAjustes.show()
    sys.exit(app.exec())
