from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QImageReader,QImage)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)


class Ui_PantallaPrincipal(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(473, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 471, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.imagenPrincipal = QLabel(self.verticalLayoutWidget)
        self.imagenPrincipal.setObjectName(u"ImagenPrincipal1")
        self.imagenPrincipal.setScaledContents(True)      
        image = QImage('IntefacesUsuarioAvanzadas/recursos/imagenPrincipal.jpeg')
        if image.isNull():
            print("Failed to load image")
        else:
            pixmap = QPixmap.fromImage(image)
            self.imagenPrincipal.setPixmap(pixmap)
        
        
        
        self.verticalLayout.addWidget(self.imagenPrincipal)

        self.btnEjercicio = QPushButton(self.verticalLayoutWidget)
        self.btnEjercicio.setObjectName(u"Ejercicio")

        self.verticalLayout.addWidget(self.btnEjercicio)

        self.btnRutinas = QPushButton(self.verticalLayoutWidget)
        self.btnRutinas.setObjectName(u"Rutinas")

        self.verticalLayout.addWidget(self.btnRutinas)

        self.btnCamara = QPushButton(self.verticalLayoutWidget)
        self.btnCamara.setObjectName(u"Camara")

        self.verticalLayout.addWidget(self.btnCamara)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.btnEjercicio.setText(QCoreApplication.translate("MainWindow", u"Iniciar Ejercicio", None))
        self.btnRutinas.setText(QCoreApplication.translate("MainWindow", u"Ver rutinas", None))
        self.btnCamara.setText(QCoreApplication.translate("MainWindow", u"Ver camara", None))
    # retranslateUi

