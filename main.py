import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filePath = "/home/raviranjan/Documents/codes/python/pyqt/video.mp4"
        self.isplaying = False
        self.setWindowTitle("Mr Player")
        self.videoWidget = QVideoWidget()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.videoString = QLineEdit()
        self.search = QPushButton("Play", self)
        self.playButton = QPushButton(">", self)
        self.setGeometry(500, 500, 1000, 500)
        self.initUI()

    def initUI(self):
        MainWidget = QWidget()
        self.setCentralWidget(MainWidget)
        layout = QGridLayout()

        self.playButton.setGeometry(10, 10, 30, 30)
        self.playButton.setStyleSheet("background-color: blue; padding: 2px")
        self.videoString.setPlaceholderText("Enter video path : ")
        self.videoString.setStyleSheet("border: 1px solid black; padding: 10px;")
        self.search.clicked.connect(self.setPath)
        self.search.setStyleSheet(
            "font: monospace; border: none; padding: 5px; background-color: blue; color: white; font-weight: bolder;"
        )
        layout.addWidget(self.search, 0, 1)
        layout.addWidget(self.videoString, 0, 0)
        layout.addWidget(self.videoWidget, 1, 0)
        layout.addWidget(self.playButton, 2, 0)
        MainWidget.setLayout(layout)
        self.playButton.clicked.connect(self.play)
        self.mediaContent = QMediaContent(QUrl.fromLocalFile(self.filePath))
        self.mediaPlayer.setMedia(self.mediaContent)

    def play(self):
        if self.isplaying:
            self.mediaPlayer.pause()
            self.playButton.setText(">")
            self.isplaying = False
            # print("Pause")
        else:
            self.mediaPlayer.play()
            self.playButton.setText("||")
            self.isplaying = True
            # print("Play")

    def setPath(self):
        if self.videoString.text() != "":
            self.filePath = self.videoString.text()
            self.QMediaContent = QMediaContent(QUrl.fromLocalFile(self.filePath))
            self.mediaPlayer.setMedia(self.mediaContent)
            self.isplaying = False
            self.playButton.setText(">")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
