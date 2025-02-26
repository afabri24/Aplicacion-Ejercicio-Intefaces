from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer, QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QImage, QPixmap)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget,QLabel,QMainWindow)

import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
sentadillas = 0
pesoMuerto=0
saltosTijera=0
remoInclinado=0
separacion=False
aux=0
up = False
down = False

class Ui_CamaraEjercicio(object):
      
 
      
    def setupUi(self, CamaraEjercicio):
        if not CamaraEjercicio.objectName():
            CamaraEjercicio.setObjectName(u"CamaraEjercicio")
        CamaraEjercicio.resize(700, 700)
        self.btnInicio = QPushButton(CamaraEjercicio)
        self.btnInicio.setObjectName(u"botonRegresar")
        self.btnInicio.setGeometry(QRect(20, 10, 93, 28))
        self.lbDescripcion = QLabel(CamaraEjercicio)
        self.lbDescripcion.setObjectName(u"lbDescripcion")
        self.lbDescripcion.setGeometry(QRect(120, 10,400, 28))
        self.camara = QLabel(CamaraEjercicio)
        self.camara.setGeometry(QRect(100, 100, 600, 600))
        self.camara.setScaledContents(True)
        
        
        

        self.retranslateUi(CamaraEjercicio)
        QMetaObject.connectSlotsByName(CamaraEjercicio)
    # setupUi

    def retranslateUi(self, CamaraEjercicio):
        CamaraEjercicio.setWindowTitle(QCoreApplication.translate("CamaraEjercicio", u"Camara", None))
        self.btnInicio.setText(QCoreApplication.translate("CamaraEjercicio", u"Regresar Inicio", None))
        self.lbDescripcion.setText(QCoreApplication.translate("CamaraEjercicio", u"Aqui podras ver la camara para saber cuanto espacio tienes\n y ver si todo tu esqueleto se ve completo ", None))
    # retranslateUi
    
    def activarCamara(self):
        self.cap = cv2.VideoCapture(0)
        self.pose = mp_pose.Pose(static_image_mode=False)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)
    
    def apagarCamara(self):
        self.timer.stop()
        self.cap.release()
        cv2.destroyAllWindows()
        
        
    def update_frame(self): 
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.pose.process(frame_rgb)

        if results.pose_landmarks is not None:
            #Prueba de contar sentadillas
            # contarSentadillas(results, height, width)
            #Prueba para contar peso muerto
            #contarPesoMuerto(results, height, width)
            #Prueba para contar saltos de tijera
            #contarSaltosTijera(results, height, width)
            #Prueba para contar remo inclinado
            #contarRemoInclinado(results, height, width)
            
                
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
        
        
def contarSentadillas(results,height,width):
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
    if up == True and down == False and angle <= 90:
        down = True
    if up == True and down == True and angle >= 160:
        sentadillas += 1
        up = False
        down = False
    if aux != sentadillas:
        aux = sentadillas
        print("count: ", sentadillas)
    
def contarPesoMuerto(results,height,width):
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
    if up == True and down == False and manoDer_y < rodillaDer_y and manoIzq_y < rodillaIzq_y:
        down = True
    if up == True and down == True and manoDer_y > rodillaDer_y and manoIzq_y > rodillaIzq_y:
        pesoMuerto += 1
        up = False
        down = False
    if aux != pesoMuerto:
        aux = pesoMuerto
        print("count: ", pesoMuerto)
        
def contarSaltosTijera(results,height,width):
    global saltosTijera
    global aux
    global separacion
    
    rodillaDer_X = int(results.pose_landmarks.landmark[26].x * width)
    rodillaIzq_X = int(results.pose_landmarks.landmark[25].x * width)
    
    if abs(rodillaDer_X - rodillaIzq_X) > 100:
        separacion = True
        
    if separacion == True and abs(rodillaDer_X - rodillaIzq_X) < 100:
        saltosTijera += 1
        separacion = False
        
    if aux != saltosTijera:
        aux = saltosTijera
        print("Saltos de tijera: ", saltosTijera)

def contarRemoInclinado(results,height,width):
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
    if up==True and down==False and angle<=70:
        down=True
    if up==True and down==True and angle>=150:
        remoInclinado+=1
        up=False
        down=False
    if aux!=remoInclinado:
        aux=remoInclinado
        print("remos: ",remoInclinado)
    
    
            
    

        

