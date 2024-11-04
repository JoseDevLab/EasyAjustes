from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDesktopServices
from classes.ui_AcercaDeEasyAjustes import Ui_Dialog

class AcercaDe(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bt_linkedIn.clicked.connect(lambda:QDesktopServices.openUrl('https://www.linkedin.com/in/joselvillamizar'))