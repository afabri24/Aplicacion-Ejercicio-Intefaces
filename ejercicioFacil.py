from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from pantallaPrincipal import Ui_PantallaPrincipal
from pantallaRutinas import Ui_Rutinas
from pantallaCamara import Ui_CamaraEjercicio
from pantallaEjercicio import Ui_Ejercicio

class SegundaPantalla(QMainWindow, Ui_Rutinas):
    def __init__(self, parent=None):
        super(SegundaPantalla, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Rutinas')

class TerceraPantalla(QMainWindow, Ui_CamaraEjercicio):
    def __init__(self, parent=None):
        super(TerceraPantalla, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Camara')
        self.btnInicio.clicked.connect(self.abrirInicio)
        self.timer = QTimer(self)  # Inicializa el atributo timer
        
    def abrirInicio(self):
            self.close()
    
    def closeEvent(self, event):
        self.apagarCamara()
        event.accept()

        
class CuartaPantalla(QMainWindow, Ui_Ejercicio):
    def __init__(self, parent=None):
        super(CuartaPantalla, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Ejercicio')
        self.timer = QTimer(self)
        
    def closeEvent(self, event):
        self.apagarCamara()
        event.accept()

class PantallaPrincipal(QMainWindow, Ui_PantallaPrincipal):
    def __init__(self, parent=None):
        super(PantallaPrincipal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Pantalla Principal')
        self.btnRutinas.clicked.connect(self.abrirRutinas)
        self.second_window = SegundaPantalla(self)
        self.btnCamara.clicked.connect(self.abrirCamara)
        self.third_window = TerceraPantalla(self)
        self.btnEjercicio.clicked.connect(self.abrirEjercicio)
        self.fourth_window = CuartaPantalla(self)

    def abrirRutinas(self):
        self.second_window.show()
    def abrirCamara(self):
        self.third_window.show()
        self.third_window.activarCamara()
    def abrirEjercicio(self):
        self.fourth_window.show()
        self.fourth_window.activarCamara()
    
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PantallaPrincipal()
    window.show()
    sys.exit(app.exec())