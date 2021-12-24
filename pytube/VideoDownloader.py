from pytube import YouTube
import time
import urllib.request
import pytube
from pytube.cli import on_progress
import os
from PyQt5.QtCore import* # QApplication oluşturmak için
import sys # sayfanın oluşması ve kapatılması için
from PyQt5 import*
from PyQt5.QtWidgets import*  # tableWidgetin kullanılması için
from PyQt5.QtGui import*

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()

        self.left = 20
        self.top = 20
        self.width = 751
        self.height = 243
        self.qtRectangle = self.frameGeometry()
        self.centerPoint=QDesktopWidget().availableGeometry().center()
        self.msg= QMessageBox()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Video and Audio Downloader")
        self.setFixedSize(self.width, self.height)

        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 93, 165, 255), stop:1 rgba(255, 255, 255, 255))")

        self.setWindowIcon(QIcon('320px-YouTube_full-color_icon_(2017).svg.png'))

        self.Download = QPushButton('Download',self)
        self.Download.setFixedSize(111,28)
        self.Download.move(240,160)
        self.Download.clicked.connect(self.StartDownload)
        self.Download.setStyleSheet("""background-color: white;
                                       border-style: outset;
                                       border-radius: 5px; border: 2px groove gray;
                                    """)

        self.combox_1 = QComboBox(self)
        self.combox_1.addItem("480p")
        self.combox_1.addItem("720p")
        self.combox_1.addItem("1080p")
        self.combox_1.setFixedSize(111,22)
        self.combox_1.move(240,100)
        self.combox_1.setStyleSheet("""background-color: white;
                                       border-style: outset;
                                       border-radius: 5px; border: 2px groove gray;
                                    """)

        self.combox_2 = QComboBox(self)
        self.combox_2.addItem("Video")
        self.combox_2.addItem("Audio")
        self.combox_2.setFixedSize(111,22)
        self.combox_2.move(370,100)
        self.combox_2.setStyleSheet("""background-color: white;
                                       border-style: outset;
                                       border-radius: 5px; border: 2px groove gray;
                                    """)

        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Video Url Here")
        self.textbox.setFixedSize(481,31)
        self.textbox.move(240,50)
        self.textbox.setStyleSheet(""" background-color: white;
                                       border-style: outset;
                                       border-radius: 5px; border: 2px groove gray;
                                   """)

        self.myFont=QFont()
        self.myFont.setBold(True)

        self.label_1= QLabel(self)
        self.label_1.setText("Paste Video Url:")
        self.label_1.setFont(self.myFont)
        self.label_1.setFixedSize(111,21)
        self.label_1.move(100,50)
        self.label_1.setStyleSheet("background-color: rgba(0,0,0,0%)")

        self.label_2= QLabel(self)
        self.label_2.setText("Choose resolution and Type:")
        self.label_2.setFont(self.myFont)
        self.label_2.setFixedSize(191,20)
        self.label_2.move(30,100)
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0%)")

        self.show()

    def ConnectionCheck(self):

        try:
            urllib.request.urlopen('http://google.com')
            return 1
        except:
            return 0

    def DisplayMessage(self,title,text,Icon):

        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.setIcon(Icon)

        x = self.msg.exec_()

    def StartDownload(self):

        Resolution = self.combox_1.currentText()

        Types= self.combox_2.currentText()

        URL = self.textbox.text()

        status=self.ConnectionCheck()

        if status == 0:

            self.DisplayMessage("No Connection!","No Internet Connection",QMessageBox.Critical)
            return 0

        else:

            if Types=='Audio':

                try:

                    yt = YouTube(URL,on_progress_callback=on_progress)

                except pytube.exceptions.RegexMatchError:

                    self.DisplayMessage("Not Connected","Not Connected to the URL",QMessageBox.Critical)
                    return 0

                download = yt.streams.filter(file_extension = "mp4",type="audio")

                if len(download)!=0:

                    download = yt.streams.filter(file_extension = "mp4",type="audio").first()

                    title =download.title

                    self.msg.setWindowTitle("Downloading")
                    self.msg.setText("{} is downloading as a audio...".format(title))
                    self.msg.setIcon(QMessageBox.Information)

                    x = self.msg.exec_()
                    download.download() # save current working directory
                    x=self.msg.done(1)

                    self.DisplayMessage("Downloaded!","{} is downloaded.".format(title),QMessageBox.Information)

                    return 1

                else:
                    self.DisplayMessage("No desirable version","There is no desirable version available",QMessageBox.Information)

                    return 0

            if Types=="Video":

                try:

                    yt = YouTube(URL,on_progress_callback=on_progress)

                except pytube.exceptions.RegexMatchError:

                    self.DisplayMessage("Not Connected","Not Connected to the URL",QMessageBox.Critical)

                    return 0

                download = yt.streams.filter(file_extension = "mp4",type="video",res=Resolution)

                if len(download)!=0:

                    download = yt.streams.filter(file_extension = "mp4",type="video",res=Resolution).first()

                    title =download.title

                    self.msg.setWindowTitle("Downloading")
                    self.msg.setText("{} is downloading as a video...".format(title))
                    self.msg.setIcon(QMessageBox.Information)

                    x = self.msg.exec_()
                    download.download() # save current working directory
                    x=self.msg.done(1)

                    self.DisplayMessage("Downloaded!","{} is downloaded.".format(title),QMessageBox.Information)

                    return 1

                else:
                    self.DisplayMessage("No desirable version","There is no desirable version available",QMessageBox.Information)

                    return 0


def main():
    app = QApplication(sys.argv)
    ary = Arayuz()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
