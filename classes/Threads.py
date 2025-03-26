import shutil
import os
from PySide6.QtCore import QObject, Signal, QThread, QFileInfo
from pathlib import Path
from datetime import datetime

class CrearAjuste(QThread):

    update_progress = Signal(int)
    update_titleProgress = Signal(str)
    update_textProgress = Signal(str)
    update_rangeProgress = Signal(int,int)
    update_cancelEnabled = Signal(bool)
    finalized = Signal()

    def __init__(self,mainWindow:QObject | None = ...):
        super().__init__(mainWindow)
        self.mw = mainWindow
        self._is_running = True  # Bandera para controlar la ejecución del hilo
        
    def run(self):
        self.update_rangeProgress.emit(0,100)
        self.update_cancelEnabled.emit(False)
        lisPaths = self.mw.listaPaths
        carpIni = self.mw.cbCarpetaIni.currentText()
        iCarpIni = self.mw.cbCarpetaIni.currentIndex()
        incluirCarp = self.mw.chbIncluirCarp.isChecked()
        dirDestino = self.mw.leDirecSelec.text()
        detalles = self.mw.teDetalles.toPlainText()
        numeracion = self.mw.sbNumeracion.value()
        fecha = self.mw.deFecha.date().toString('ddMMyyyy')
        hora = self.mw.teHora.time().toString('HHmm')
        if self.mw.leSigla.isVisible():
            sigla = self.mw.leSigla.text()
        elif self.mw.cbSiglas.isVisible():
            sigla = self.mw.cbSiglas.currentText()
        nomAjuste = f'AJ{numeracion:03}_{fecha}_{hora}_{sigla}'

        dirDestino = f'{dirDestino}/{nomAjuste}'
        
        comprimir = self.mw.chbComprimir.isChecked()
        formato = self.mw.cbFormato.currentIndex()
        if formato == 0:
            ext = 'zip' # .zip
        elif formato == 1:
            ext = 'tar' # .tar
        elif formato == 2:
            ext = 'gztar' # .tar.gz
        elif formato == 3:
            ext = 'bztar' # .tar.bz2
        else:
            ext = 'xztar' # .tar.xz
        
        if incluirCarp:
            dirDestino1 = f'{dirDestino}/{carpIni}'
        else:
            dirDestino1 = dirDestino
        strTxt = f'{dirDestino}/{nomAjuste}.txt'
        dirTxt = Path(strTxt)
        try:
            if dirTxt.exists():
                mensajeTxt = 'Sobrescrito Correctamente.'
            else:
                mensajeTxt = 'Creado y escrito correctamente.'
            # Crear el directorio si no existe
            dirTxt.parent.mkdir(parents=True, exist_ok=True)
            # Escribir en el archivo
            with open(dirTxt, 'w') as archivo:
                archivo.write(detalles)
            self.mw.estadoTxt = {
                'pathTxt': strTxt,
                'creado': True,
                'mensaje': mensajeTxt
            }
        except PermissionError:
            self.mw.estadoTxt = {
                'pathTxt': strTxt,
                'creado': False,
                'mensaje': 'Error: No tienes permisos para escribir en el directorio.'
            }
        except OSError as e:
            self.mw.estadoTxt = {
                'pathTxt': strTxt,
                'creado': False,
                'mensaje': f'Error del sistema operativo: {e}'
            }
        except Exception as e:
            self.mw.estadoTxt = {
                'pathTxt': strTxt,
                'creado': False,
                'mensaje': f'Error: {e}'
            }

        ordenRepetido = 0
        for i in range(iCarpIni+1):
            if self.mw.cbCarpetaIni.itemText(i) == carpIni:
                ordenRepetido += 1 # Con esto se consigue saber que posición ocupa la carpeta seleccionada entre las repetidas (En el caso de repetirse el mismo nombre de carpeta)
        
        self.update_cancelEnabled.emit(True)
        n = len(lisPaths)
        pasos = 100/n
        for i in range(n):
            if not self._is_running:
                break
            path = lisPaths[i]
            partes = path['pathConstruir'].filePath().split(carpIni)
            try:
                # Verificar si hay suficientes apariciones de la subcadena
                if len(partes) >= ordenRepetido:
                    recortada = carpIni.join(partes[ordenRepetido:])  # Recortar desde la aparición especificada
                else:
                    raise Exception(f"La subcadena '{carpIni}' no apareción {ordenRepetido} veces.")
                fileDestino = f'{dirDestino1}{recortada}'
                fileOrigen = path['pathOrigen'].filePath()
                self.update_textProgress.emit(f'Copiando:\n{fileOrigen}\n\nHacia\n\n{fileDestino}')
                path['pathDestino'] = fileDestino
                pathOrigen = Path(fileOrigen)
                pathDestino = Path(fileDestino)
                if pathDestino.exists():
                    path['mensaje'] = 'Copiado y sobrescrito correctamente.'
                else:
                    path['mensaje'] = 'Copiado correctamente.'
                # Crear el directorio de destino (sin el nombre del archivo)
                directorio_destino = pathDestino.parent
                # Crear el directorio si no existe
                directorio_destino.mkdir(parents=True, exist_ok=True)
                # Copiar el archivo al directorio de destino
                shutil.copy(pathOrigen, pathDestino)
                path['copiado'] = True
                self.update_progress.emit(round(i*pasos))

            except FileNotFoundError:
                path['copiado'] = False
                path['mensaje'] = 'Error: El archivo de origen no se encuentra.'
            except PermissionError:
                path['copiado'] = False
                path['mensaje'] = 'Error: No tienes permisos suficientes para copiar el archivo.'
            except IsADirectoryError:
                path['copiado'] = False
                path['mensaje'] = 'Error: La ruta de destino es un directorio, no un archivo.'
            except OSError as e:
                path['copiado'] = False
                path['mensaje'] = f'Error del sistema operativo: {e}'
                print(f"Error del sistema operativo: {e}")
            except Exception as e:
                path['copiado'] = False
                path['mensaje'] = f'Error: {e}'
            lisPaths[i] = path
        if comprimir:
            self.update_textProgress.emit(f'Comprimiendo archivos ...')
            shutil.make_archive(dirDestino, ext, dirDestino)
        self.mw.listaPaths = lisPaths
        self.finalized.emit()
        
    def stop(self):
        self._is_running = False
        
class CargandoArchivo(QThread):
    
    update_progress = Signal(int)
    update_titleProgress = Signal(str)
    update_textProgress = Signal(str)
    update_rangeProgress = Signal(int,int)
    update_cancelEnabled = Signal(bool)
    finalized = Signal(dict)
    
    def __init__(self,file_path,parent:QObject | None = ...):
        super().__init__(parent)
        self.file_path = file_path
        self._is_running = True  # Bandera para controlar la ejecución del hilo
        
    def run(self):
        self.update_cancelEnabled.emit(False)
        try:
            self.update_rangeProgress.emit(0,0)
            self.update_titleProgress.emit('Leyendo archivo 🧾👓 ...')
            self.update_textProgress.emit(f'Leyendo archivo 🧾👓 ...\n{self.file_path}')
            with open(self.file_path, 'r', encoding='utf-8') as archivo:
                paths = [linea.strip().replace('\\','/') for linea in archivo]
                paths = [path for path in paths if path]
                archivo.seek(0)  # Volver al principio del archivo
                txtPaths = archivo.read()
            paths1 = [path.split(':')[-1] for path in paths]
            paths1 = ['UNIDAD/'+path if path[0]!='/' else 'UNIDAD'+path for path in paths1]
            listaPaths = []
            if len(paths)==0:
                raise Exception(f"El archivo seleccionado esta vacío.")
            self.update_rangeProgress.emit(0,100)
            self.update_titleProgress.emit('Guardando paths encontrados 💾 ...')
            n = len(paths)
            self.update_textProgress.emit(f'Guardando {n} paths encontrados.')
            self.update_cancelEnabled.emit(True)
            paso = 100/n
            for i in range(n):
                if not self._is_running:
                    raise Exception(f'Se canceló la operación.')
                self.update_progress.emit(i*paso)
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
                    'mensaje': 'Operación cancelada.'
                })
            comunes = cargarCarpetasComunes(self,listaPaths)
            respuesta = {
                'correcto': True,
                'file_path': self.file_path,
                'txtPaths': txtPaths,
                'listaPaths': listaPaths,
                'comunes': comunes
            }
        except Exception as e:
            respuesta = {
                'correcto': False,
                'e': e
            }
        self.finalized.emit(respuesta)
            
    def stop(self):
        self._is_running = False
        
class FiltrarArchivosPorFecha(QThread):

    update_progress = Signal(int)
    update_titleProgress = Signal(str)
    update_textProgress = Signal(str)
    update_rangeProgress = Signal(int,int)
    update_cancelEnabled = Signal(bool)
    finalized = Signal(dict)

    def __init__(self,directorio,mainWindow:QObject | None = ...):
        super().__init__(mainWindow)
        self.mw = mainWindow
        self._is_running = True  # Bandera para controlar la ejecución del hilo
        self.directorio = directorio
        fecha_inicio_qt = mainWindow.dteInicial.dateTime()
        fecha_final_qt = mainWindow.dteFinal.dateTime()
        # Convertir a datetime de Python
        self.fecha_inicio = fecha_inicio_qt.toPython()
        self.fecha_final = fecha_final_qt.toPython()

    def run(self):
        self.update_cancelEnabled.emit(True)
        self.update_rangeProgress.emit(0,0)
        self.update_titleProgress.emit('Buscando archivos 🔎👀🔍...')

        listaPaths = []
        txtPaths = ''
        i = 0
        encontrados = 0
        ultimoEncontrado = '🤷‍♂️🤷‍♂️🤷‍♀️🤷‍♀️'
        try:
            # Recorrer directorios y subdirectorios
            for root, dirs, files in os.walk(self.directorio):
                for file in files:
                    if not self._is_running:
                        raise Exception('Se canceló la operación.')
                    file_path = os.path.join(root, file)
                    
                    if i%50==0:
                        self.update_textProgress.emit(f'''Archivos analizados: <b>{i}</b> 👓<br>
Archivos encontrados: <b>{encontrados}</b> ✔<br>
Último encontrado:<br>
👉 <b>{ultimoEncontrado}</b> 👈''')

                    # Obtener la fecha de modificación del archivo
                    timestamp_modificacion = os.path.getmtime(file_path)
                    fecha_modificacion = datetime.fromtimestamp(timestamp_modificacion)

                    # Comprobar si está en el rango
                    if self.fecha_inicio <= fecha_modificacion <= self.fecha_final:
                        encontrados += 1
                        ultimoEncontrado = QFileInfo(file_path).fileName()
#                         self.update_textProgress.emit(f'''Archivos analizados: <b>{i}</b> 👓<br>
# Archivos encontrados: <b>{encontrados}</b> ✔<br>
# Último encontrado:<br>
# 👉 <b>{ultimoEncontrado}</b> 👈''')
                        path = os.path.abspath(file_path)
                        if i!=0:
                            txtPaths += '\n'
                        txtPaths += path
                        path = path.replace('\\','/')
                        path1 = path.split(':')[-1]
                        path1 = ('UNIDAD/'+path1 if path1[0]!='/' else 'UNIDAD'+path1)
                        path0 = QFileInfo(path)
                        path1 = QFileInfo(path1)
                        listaPaths.append({
                            'pathOrigen': path0,
                            'pathConstruir': path1,
                            'pathDestino': '',
                            'numeracion': f'{encontrados}',
                            'copiado': False,
                            'mensaje': 'Operación cancelada.'
                        })
                    i += 1
            comunes = cargarCarpetasComunes(self,listaPaths)
            respuesta = {
                'correcto': True,
                'directorio': self.directorio,
                'txtPaths': txtPaths,
                'listaPaths': listaPaths,
                'comunes': comunes
            }
        except Exception as e:
            respuesta = {
                'correcto': False,
                'e': e
            }
        self.finalized.emit(respuesta)
        
    def stop(self):
        self._is_running = False
        
class CargandoComunes(QThread):
    update_progress = Signal(int)
    update_titleProgress = Signal(str)
    update_textProgress = Signal(str)
    update_rangeProgress = Signal(int,int)
    update_cancelEnabled = Signal(bool)
    finalized = Signal(list)
    def __init__(self,listaPaths:list,parent:QObject | None = ...):
        super().__init__(parent)
        self.listaPaths = listaPaths
        
    def run(self):
        self.update_cancelEnabled.emit(False)
        comunes = cargarCarpetasComunes(self,self.listaPaths)
        self.finalized.emit(comunes)
        
def cargarCarpetasComunes(parent:CargandoArchivo|FiltrarArchivosPorFecha|CargandoComunes,listaPaths:list):
    parent.update_titleProgress.emit('Filtrando carpetas comunes 📁 ...')
    parent.update_rangeProgress.emit(0,100)
    comunes = []
    carpetas1 = []
    parent.update_textProgress.emit(f'Encontrando ruta mas corta ...')
    n = len(listaPaths)
    paso = 100/n if n!=0 else 0
    for i in range(n):
        parent.update_progress.emit(i*paso)
        file = listaPaths[i]
        qFile = file['pathConstruir']
        carpetas = qFile.path().split('/')
        if i!=0:
            if len(carpetas) < len(carpetas1):
                carpetas1 = carpetas
                i0 = i
        else:
            carpetas1 = carpetas
            i0 = i
    parent.update_rangeProgress.emit(0,0)
    parent.update_textProgress.emit(f'Filtrando carpetas comunes 📁 ...\n 🤷‍♂️🤷‍♂️🤷‍♀️🤷‍♀️')
    strComunes = ''
    for i in range(len(carpetas1)):
        carpeta1 = carpetas1[i]
        comun = True
        for j in range(len(listaPaths)):
            file = listaPaths[j]
            if j!=i0:
                qFile = file['pathConstruir']
                carpetas2 = qFile.path().split('/')
                if carpetas2[i] != carpeta1:
                    comun = False
                    break
        if comun:
            strComunes += (f'/{carpeta1}' if strComunes!='' else f'{carpeta1}')
            parent.update_textProgress.emit(f'Filtrando carpetas comunes 📁 ...\n{strComunes}')
            comunes.append(carpeta1)
        else:
            break
    return comunes