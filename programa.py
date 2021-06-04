from PyQt5.QtCore import  QDir, Qt, QUrl, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolButton, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QHBoxLayout, QVBoxLayout, QLayout, QSlider)
import sys
import serial
import time 
 
class VideoPlayer(QMainWindow):
    
    def __init__(self):
        #Variables de clase
        play = pyqtSignal()          
        pause = pyqtSignal()
        stop = pyqtSignal()
        next = pyqtSignal()
        previous = pyqtSignal()
        changeVolume = pyqtSignal(int)
        changeMuting = pyqtSignal(bool)
            
        super().__init__()
        self.setWindowTitle("AutoD")
        # ======================= SEÑALES =============================
        
        #self.playerState = QMediaPlayer.StoppedState   #Inicializa el valor en 0 
        #self.playerMuted = False # iniciailiza el valor como no silenciado

        # Configuración de video 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.setContentsMargins(0, 0, 0, 0)
        
         # Creación de boton para reproducir música 
        self.playButton = QToolButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.setPlayPause)
        
        #Creaciónn de boton para pausar la música
#         self.pauseButton = QToolButton()
#         self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
#         self.pauseButton.clicked.connect(self.stop)
         
         #Creación del boton de siguiente 
        self.nextButton = QToolButton()
        self.nextButton.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.nextButton.clicked.connect(self.setNext)
        
        #Creación del boton de retroceder
        self.previousButton = QToolButton()
        self.previousButton.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.previousButton.clicked.connect(self.setPrevious)
        
        #Creación del boton de mute
        self.muteButton = QToolButton()
        self.muteButton.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.muteButton.clicked.connect(self.setMute)
        
        #Esto se cambiará 
        self.openButton = QPushButton("Open Video")   
        self.openButton.clicked.connect(self.openFile)
        
 # ================= Configuración de la pantalla ===============================
        widget = QWidget(self)
        self.setCentralWidget(widget)
        self.volumeSlider = QSlider(Qt.Horizontal, sliderMoved=self.changeVolume)
        self.volumeSlider.setRange(0, 100)
        
#                       ******************** Diseño Horizontal de las pantalla **********************
        displayLayout = QHBoxLayout()
        displayLayout.addWidget(videoWidget, 2)
        
#                       ******************** Diseño Horizontal de los botones **********************
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.openButton)
        controlLayout.addStretch(1)
        controlLayout.addWidget(self.previousButton)
        controlLayout.addWidget(self.playButton)
        #controlLayout.addWidget(self.pauseButton)
        controlLayout.addWidget(self.nextButton)
        controlLayout.addWidget(self.muteButton)
        controlLayout.addStretch(1)
        controlLayout.addWidget(self.volumeSlider)
        
#      ******************** Diseño Horizontal y vertical de pantalla y botones **********************
        layout = QVBoxLayout()
        layout.addLayout(displayLayout)
        hLayout = QHBoxLayout()
        layout.addLayout(hLayout)
        layout.addLayout(controlLayout)
        
        widget.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
 
#    ================= Conexión de estados con los botones =======================
            
    def setPlayPause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

        
    def setNext(self):
        print("Funciono: NEXT")
        
    def setPrevious(self):
        print("Funciono: PREVIOUS")
        
    def setMute(self, mute):
           print("Funciono: MUTE")
    
    def volume(self):
        return self.volumeSlider.value()

    def changeVolume(self, volume):
        self.volumeSlider.changeVolume(volume)
            
# # ================= Conexion Arduino  ===============================
    def conexionArduino(self):
        contador_play_pause = 0
        contador_boton_on_off = 0
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
        ser.flush()
        while True:
            if ser.in_waiting > 0:
                 line = ser.readline().decode('utf-8').rstrip()
#                 if (line == "0xFFE21D"):
#                     self.estado = "silenciar"
                 if (line == "0xFF22DD"):
                    contador_play_pause += 1 
                    if  contador_play_pause%2 == 0:
                        self.mediaPlayer = 1
                    else:
                        self.mediaPlayer = 0
                    self.setPlayPause()
#                 elif (line == "0xFF02FD"):
#                     self.estado = "rebobinar"
#                 elif (line == "0xFFC23D"):
#                     self.estado = "adelantar"
#                 elif (line == "0xFF906F"):
#                     self.estado = "subir_volumen"
#                 elif (line == "0xFFA857"):
#                     self.estado = "bajar_volumen"
#                 elif (line == "0xFF9867"):
#                     self.estado = "shuffle"
#                 else:
#                     print (" Intenta nuevamente")

    def comuicacionMemExterna(self):
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
        ser.flush()
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                break
            
        def playlist():
            pass
        
            

 
app = QApplication(sys.argv)
videoplayer = VideoPlayer()
videoplayer.conexionArduino()
videoplayer.resize(640, 480)
videoplayer.show()
sys.exit(app.exec_())