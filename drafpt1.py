import sys, re, os
from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent
from draft1ui import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

#temp i think
from gtts import gTTS
# from io import BytesIO
# from pygame import mixer as pm, time as pt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


        self.repeatnobox.valueChanged.connect(self.repeatnofunc)
        self.enteredtxt.selectionChanged.connect(self.smthselected)
        self.resetbtn.clicked.connect(self.resetbtnfunc)
        self.savebtn.clicked.connect(self.savebtnfunc)
        self.clearbtn.clicked.connect(self.cleartxtfunc)
        self.playbtn.clicked.connect(self.playbtnfunc)
        self.replaybtn.clicked.connect(self.replaybtnfunc)
        self.positionmedia.sliderMoved.connect(self.set_audio_pos)

        self.temprepeatno = 0

    def smthselected(self):
        a=self.enteredtxt.textCursor().selectedText().split("**")
        print("here", a)
        if (len(a) > 1):
            a = a[1].split(">")[0].split("t")[1]
            print("heree again",a)
            self.repeatnobox.setValue(int(a))

    
    def repeatnofunc(self):
        self.temprepeatno = self.repeatnobox.value()
        print(self.temprepeatno)


    def savebtnfunc(self):
        print("savebtn clicked")
        a=self.enteredtxt.textCursor().selectedText()
        self.enteredtxt.textCursor().removeSelectedText()
        check = re.split(r'\*\*repeat\d\>', a)
        print("checc",check)
        if (check[0] != ""):
            print(self.temprepeatno)
            self.enteredtxt.textCursor().insertText(f"**repeat{self.temprepeatno}>{a}<repeat**")
        else:
            self.enteredtxt.textCursor().insertText(f"**repeat{self.temprepeatno}>{check[1].split("<repeat**")[0]}<repeat**")

    def resetbtnfunc(self):
        a = self.enteredtxt.textCursor().selectedText()
        b = re.split(r'\*\*repeat\d\>', a)[1].split("<repeat**")[0]
        print(b)
        self.enteredtxt.textCursor().removeSelectedText()
        self.enteredtxt.textCursor().insertText(b)
        self.repeatnobox.setValue(0)

    def cleartxtfunc(self):
        print("clear clciked")
        self.enteredtxt.clear()

    def playbtnfunc(self):
        print("playbtn clicked")
        if (os.path.exists("temp.mp3") == False):
            print(self.enteredtxt.toPlainText())
            wholetxt = self.enteredtxt.toPlainText().split("<repeat**")
            t = []
            print(wholetxt)
            tospeak = []
            for i in wholetxt:
                ele= re.findall(r'\A\*\*repeat\d\>', i)
                if (len(ele)>0):
                    n = int(ele[0].split("t")[1].replace(">", ""))
                    for x in range(n):
                        tospeak.append(re.sub(r'\*\*repeat\d\>', "", i))
                else:
                    elem = re.findall(r'\*\*repeat\d\>', i)
                    if (len(elem)>0):
                        toadd = i.split("**")
                        n = int(elem[0].split("t")[1].replace(">", ""))
                        tospeak.append(toadd[0])
                        for x in range(n):
                            tospeak.append(re.sub(r'repeat\d\>', "", toadd[1]))
                    else:
                        tospeak.append(i)
            print("plas word", " ".join(tospeak))
            txt = " ".join(tospeak)
            tts = gTTS(txt, lang="en")
            tts.save("temp.mp3")
            self.playaudio()
        else:
            self.playaudio()

    def playaudio(self):
        self.player = QMediaPlayer()
        self.audioop = QAudioOutput()
        self.player.setAudioOutput(self.audioop)
        self.player.positionChanged.connect(self.slider_pos_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.playbackStateChanged.connect(self.playerstatechanged)
        self.player.errorOccurred.connect(lambda error: print("Error:", error))
        src = QUrl.fromLocalFile('temp.mp3')
        if not src.isValid():
            print("invalid")
        else:
            print("this")
            self.player.setSource(src)
            self.audioop.setVolume(50)
            self.player.play()

    def playerstatechanged(self):
        print(self.player.isPlaying())
        if self.player.isPlaying():
            self.playbtn.setText("Pause")
        else:
            self.playbtn.setText("Play")

    def slider_pos_changed(self, position):
        self.positionmedia.setValue(position)

    def duration_changed(self, duration):
        self.positionmedia.setRange(0, duration)

    def set_audio_pos(self, position):
        self.player.setPosition(position)

    def closeEvent(self, event: QCloseEvent):
        os.remove('temp.mp3')

    def replaybtnfunc(self):
        print("replay ckciked")


app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")

window = MainWindow()
window.show()
app.exec()


# fixed -- when some is repeated and the full thing is selected to be repeated it gives error === i think better way is to just add a replay btn
#value of spinbox doesnt update when a simple text is chosen
#play doesnt do much now
#make an icon
#etc