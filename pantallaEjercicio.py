from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget, QMessageBox)

import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
sentadillas = 0
pesoMuerto= 0
saltoTijera=0
remoInclinado=0
separacion=False
aux=0
up = False
down = False

ejercicio=1

class Ui_Ejercicio(object):
    def setupUi(self, PantallaEjercicio):
        if not PantallaEjercicio.objectName():
            PantallaEjercicio.setObjectName(u"PantallaEjercicio")
        PantallaEjercicio.resize(800, 602)
        self.centralwidget = QWidget(PantallaEjercicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(400, 0, 401, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rutinas = QLabel(self.verticalLayoutWidget)
        self.rutinas.setObjectName(u"rutinas")

        self.verticalLayout.addWidget(self.rutinas)

        self.lbEjercicio1 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicio1.setObjectName(u"lbEjercicio1")
        self.lbEjercicio1.setStyleSheet("background-color: #EB4A37")
        

        self.verticalLayout.addWidget(self.lbEjercicio1)

        self.lbEjercicioRecord1 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicioRecord1.setObjectName(u"lbEjercicioRecord1")

        self.verticalLayout.addWidget(self.lbEjercicioRecord1)

        self.lbEjercicio2 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicio2.setObjectName(u"lbEjercicio2")
        self.lbEjercicio2.setStyleSheet("background-color: #EB4A37")

        self.verticalLayout.addWidget(self.lbEjercicio2)

        self.lbEjercicioRecord2 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicioRecord2.setObjectName(u"lbEjercicioRecord2")

        self.verticalLayout.addWidget(self.lbEjercicioRecord2)

        self.lbEjercicio3 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicio3.setObjectName(u"lbEjercicio3")
        self.lbEjercicio3.setStyleSheet("background-color: #EB4A37")

        self.verticalLayout.addWidget(self.lbEjercicio3)

        self.lbEjercicioRecord3 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicioRecord3.setObjectName(u"lbEjercicioRecord3")

        self.verticalLayout.addWidget(self.lbEjercicioRecord3)

        self.lbEjercicio4 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicio4.setObjectName(u"lbEjercicio4")
        self.lbEjercicio4.setStyleSheet("background-color: #EB4A37")

        self.verticalLayout.addWidget(self.lbEjercicio4)

        self.lbEjercicioRecord4 = QLabel(self.verticalLayoutWidget)
        self.lbEjercicioRecord4.setObjectName(u"lbEjercicioRecord4")

        self.verticalLayout.addWidget(self.lbEjercicioRecord4)

        self.btnEjercicio = QPushButton(self.verticalLayoutWidget)
        self.btnEjercicio.setObjectName(u"btnEjercicio")

        self.verticalLayout.addWidget(self.btnEjercicio)

        
        
        
        
        
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 390, 401, 211))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.contadorEjercicio = QLabel(self.verticalLayoutWidget_2)
        self.contadorEjercicio.setObjectName(u"contadorEjercicio")
        self.contadorEjercicio.setTextFormat(Qt.RichText)
        self.contadorEjercicio.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.contadorEjercicio)

        self.cuadroAfirmacion = QLabel(self.verticalLayoutWidget_2)
        self.cuadroAfirmacion.setObjectName(u"cuadroAfirmacion")
        self.cuadroAfirmacion.setStyleSheet("background-color: white")

        self.horizontalLayout.addWidget(self.cuadroAfirmacion)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        PantallaEjercicio.setCentralWidget(self.centralwidget)
        
        #Aqui esta el label de la camara
        self.camara = QLabel(self.centralwidget)
        self.camara.setObjectName(u"Camara")
        self.camara.setGeometry(QRect(0, 0, 400, 400))
        self.camara.setScaledContents(True)
        
        self.retranslateUi(PantallaEjercicio)

        QMetaObject.connectSlotsByName(PantallaEjercicio)
    # setupUi

    def retranslateUi(self, PantallaEjercicio):
        PantallaEjercicio.setWindowTitle(QCoreApplication.translate("PantallaEjercicio", u"Ejercicio", None))
        self.rutinas.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Rutina 1:</span></p></body></html>", None))
        self.lbEjercicio1.setText(QCoreApplication.translate("PantallaEjercicio", u"Ejercicio 1: Sentadillas", None))
        self.lbEjercicioRecord1.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 1:", None))
        self.lbEjercicio2.setText(QCoreApplication.translate("PantallaEjercicio", u"Ejercicio 2: Peso Muerto", None))
        self.lbEjercicioRecord2.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 2:", None))
        self.lbEjercicio3.setText(QCoreApplication.translate("PantallaEjercicio", u"Ejercicio 3: Saltos de tijera", None))
        self.lbEjercicioRecord3.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 3:", None))
        self.lbEjercicio4.setText(QCoreApplication.translate("PantallaEjercicio", u"Ejercicio 4: Remo inclinado", None))
        self.lbEjercicioRecord4.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 4:", None))
        self.btnEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"Siguiente Ejercicio/Terminar rutina", None))
        self.label.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Repeticiones:</span></p></body></html>", None))
        self.contadorEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-align: center;\">0</span></p></body></html>", None))
        self.cuadroAfirmacion.setText(QCoreApplication.translate("PantallaEjercicio", None))
        
        self.btnEjercicio.clicked.connect(self.cambiarEjercicio)
        
    # retranslateUi

    def activarCamara(self):
        self.cap = cv2.VideoCapture(0)
        self.pose = mp_pose.Pose(static_image_mode=False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)
        
    def apagarCamara(self):
        self.timer.stop()
        self.cap.release()
        cv2.destroyAllWindows()
        
    def cambiarEjercicio(self):
        global ejercicio
        global aux
        ejercicio+=1
        print("cambio el ejercicio")
        aux=0
        self.contadorEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-align: center;\">0</span></p></body></html>", None))
        
        if ejercicio!=1:
            self.lbEjercicio1.setStyleSheet("background-color: green")
            self.lbEjercicioRecord1.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 1: "+str(sentadillas), None))
        if ejercicio!=2 and ejercicio>1:
            self.lbEjercicio2.setStyleSheet("background-color: green")
            self.lbEjercicioRecord2.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 2: "+str(pesoMuerto), None))
        if ejercicio!=3 and ejercicio>2:
            self.lbEjercicio3.setStyleSheet("background-color: green")
            self.lbEjercicioRecord3.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 3: "+str(saltoTijera), None))
        if ejercicio!=4 and ejercicio>3:
            self.lbEjercicio4.setStyleSheet("background-color: green")
            self.lbEjercicioRecord4.setText(QCoreApplication.translate("PantallaEjercicio", u"Record ejercicio 4: "+str(remoInclinado), None))
        
        #aqui quiero que cuando llegue al ejercicio 5 muestre la pantalla de felicitaciones y cierre la pantalla de ejercicio
        if ejercicio==5:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Felicidades")
            mensaje.setText("Has terminado la rutina")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.exec_()
            self.close()


    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.pose.process(frame_rgb)

            if results.pose_landmarks is not None:
                
                if ejercicio==1:
                    contarSentadillas(self,results, width, height)
                if ejercicio==2:
                    contarPesoMuerto(self,results, width, height)
                if ejercicio==3:
                    contarSaltosTijera(self,results, width, height)
                if ejercicio==4:
                    contarRemoInclinado(self,results, width, height)
                
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
                    mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
                 

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
            self.camara.setPixmap(QPixmap.fromImage(p))
            
            
#Aqui es donde esta el metodo donde se cuentan las sentadillas
def contarSentadillas(self,results,height,width):
    global sentadillas
    global aux
    global up
    global down
    
    
    x1 = int(results.pose_landmarks.landmark[24].x * width)
    y1 = int(results.pose_landmarks.landmark[24].y * height)
    x2 = int(results.pose_landmarks.landmark[26].x * width)
    y2 = int(results.pose_landmarks.landmark[26].y * height)
    x3 = int(results.pose_landmarks.landmark[28].x * width)
    y3 = int(results.pose_landmarks.landmark[28].y * height)
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    p3 = np.array([x3, y3])
    l1 = np.linalg.norm(p2 - p3)
    l2 = np.linalg.norm(p1 - p3)
    l3 = np.linalg.norm(p1 - p2)
    # Calcular el ángulo
    angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
    
    # print(round(angle))
    if angle >= 160:
        up = True
        self.cuadroAfirmacion.setStyleSheet("background-color: white")
        self.cuadroAfirmacion.setText(QCoreApplication.translate("PantallaEjercicio", u"", None))
    if up == True and down == False and angle <= 110:
        down = True
    if up == True and down == True and angle >= 160:
        sentadillas += 1
        up = False
        down = False
    if aux != sentadillas:
        aux = sentadillas
        print("sentadillas: ", sentadillas)
        self.contadorEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-align: center;\">"+str(sentadillas)+"</span></p></body></html>", None))
        self.cuadroAfirmacion.setStyleSheet("background-color: green")
        self.cuadroAfirmacion.setText(QCoreApplication.translate("PantallaEjercicio", u"¡Bien hecho!", None))
        


def contarPesoMuerto(self,results,height,width):
    global pesoMuerto
    global aux
    global up
    global down
    
    
    rodillaDer_y = int(results.pose_landmarks.landmark[26].y * height)
    manoDer_y = int(results.pose_landmarks.landmark[16].y * height)
    rodillaIzq_y = int(results.pose_landmarks.landmark[25].y * height)
    manoIzq_y = int(results.pose_landmarks.landmark[15].y * height)
    
    if manoDer_y > rodillaDer_y and manoIzq_y > rodillaIzq_y:
        up = True
        self.cuadroAfirmacion.setStyleSheet("background-color: white")
        self.cuadroAfirmacion.setText(QCoreApplication.translate("PantallaEjercicio", u"", None))
    if up == True and down == False and manoDer_y < rodillaDer_y and manoIzq_y < rodillaIzq_y:
        down = True
    if up == True and down == True and manoDer_y > rodillaDer_y and manoIzq_y > rodillaIzq_y:
        pesoMuerto += 1
        up = False
        down = False
    if aux != pesoMuerto:
        aux = pesoMuerto
        print("peso Muerto: ", pesoMuerto)
        self.contadorEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-align: center;\">"+str(pesoMuerto)+"</span></p></body></html>", None))
        self.cuadroAfirmacion.setStyleSheet("background-color: green")

def contarSaltosTijera(self,results,height,width):
    global saltoTijera
    global aux
    global separacion
    
    rodillaDer_X = int(results.pose_landmarks.landmark[26].x * width)
    rodillaIzq_X = int(results.pose_landmarks.landmark[25].x * width)
    
    if abs(rodillaDer_X - rodillaIzq_X) > 100:
        separacion = True
        self.cuadroAfirmacion.setStyleSheet("background-color: white")
        self.cuadroAfirmacion.setText(QCoreApplication.translate("PantallaEjercicio", u"", None))
    if separacion == True and abs(rodillaDer_X - rodillaIzq_X) < 100:
        saltoTijera += 1
        separacion = False
        
    if aux != saltoTijera:
        aux = saltoTijera
        print("Saltos de tijera: ", saltoTijera)
        self.contadorEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-align: center;\">"+str(saltoTijera)+"</span></p></body></html>", None))
        self.cuadroAfirmacion.setStyleSheet("background-color: green")

def contarRemoInclinado(self,results,height,width):
    global remoInclinado
    global aux
    global up
    global down
    
    x1=int(results.pose_landmarks.landmark[12].x*width)
    y1=int(results.pose_landmarks.landmark[12].y*height)
    x2=int(results.pose_landmarks.landmark[14].x*width)
    y2=int(results.pose_landmarks.landmark[14].y*height)
    x3=int(results.pose_landmarks.landmark[16].x*width)
    y3=int(results.pose_landmarks.landmark[16].y*height)
    p1=np.array([x1,y1])
    p2=np.array([x2,y2])
    p3=np.array([x3,y3])
    l1=np.linalg.norm(p2-p3)
    l2=np.linalg.norm(p1-p3)
    l3=np.linalg.norm(p1-p2)
    #Calcular el ángulo
    angle=degrees(acos((l1**2+l3**2-l2**2)/(2*l1*l3)))
    
    #print(round(angle))
    
    if angle>=150:
        up=True
        self.cuadroAfirmacion.setStyleSheet("background-color: white")
        self.cuadroAfirmacion.setText(QCoreApplication.translate("PantallaEjercicio", u"", None))
    if up==True and down==False and angle<=70:
        down=True
    if up==True and down==True and angle>=150:
        remoInclinado+=1
        up=False
        down=False
    if aux!=remoInclinado:
        aux=remoInclinado
        print("remos: ",remoInclinado)
        self.contadorEjercicio.setText(QCoreApplication.translate("PantallaEjercicio", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-align: center;\">"+str(remoInclinado)+"</span></p></body></html>", None))
        self.cuadroAfirmacion.setStyleSheet("background-color: green")
               