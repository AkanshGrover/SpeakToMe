import sys, re, os, pyttsx3
from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent
from mainui import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from pypdf import PdfReader


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
        self.positionmedia.sliderMoved.connect(self.set_audio_pos)
        self.importtxt.clicked.connect(self.importtextfunc)

        self.engine = pyttsx3.init()
        self.voicegendercombobox.addItems(["0", "1"])
        self.voiceratespinbox.setValue(self.engine.getProperty('rate'))
        self.applyvoicebtn.clicked.connect(self.applyvoicefunc)
        self.resetvoicebtn.clicked.connect(self.resetvoicefunc)

        self.temprepeatno = 0

        self.player = QMediaPlayer()
        self.audioop = QAudioOutput()
        self.player.setAudioOutput(self.audioop)
        self.player.positionChanged.connect(self.slider_pos_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.playbackStateChanged.connect(self.playerstatechanged)
        self.player.errorOccurred.connect(lambda error: print("Error:", error))
        if sys.platform == "win32":
            path = os.path.expanduser('~').replace("\\", r"\\") + r"\\" + "Documents" + r"\\" + "STM" + r"\\"
            if not os.path.exists(path):
                os.mkdir(path)
            self.src = path + "temp.mp3"
        self.audioop.setVolume(50)

    def applyvoicefunc(self):
        self.engine.setProperty('rate', self.voiceratespinbox.value())
        self.engine.setProperty('voice', self.engine.getProperty('voices')[int(self.voicegendercombobox.currentText())].id)
        if os.path.isfile(self.src):
            self.delete_file()

    def resetvoicefunc(self):
        self.voicegendercombobox.setCurrentIndex(0)
        self.voiceratespinbox.setValue(200)
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[0].id)
        if os.path.isfile(self.src):
            self.delete_file()

    def smthselected(self):
        a=self.enteredtxt.textCursor().selectedText().split("**")
        if (len(a) > 1):
            a = a[1].split(">")[0].split("t")[1]
            self.repeatnobox.setValue(int(a))

    
    def repeatnofunc(self):
        self.temprepeatno = self.repeatnobox.value()


    def savebtnfunc(self):
        a=self.enteredtxt.textCursor().selectedText()
        self.enteredtxt.textCursor().removeSelectedText()
        check = re.split(r'\*\*repeat\d\>', a)
        if (check[0] != ""):
            self.enteredtxt.textCursor().insertText(f"**repeat{self.temprepeatno}>{a}<repeat**")
        else:
            self.enteredtxt.textCursor().insertText(f"**repeat{self.temprepeatno}>{check[1].split("<repeat**")[0]}<repeat**")

    def resetbtnfunc(self):
        a = self.enteredtxt.textCursor().selectedText()
        b = re.split(r'\*\*repeat\d\>', a)[1].split("<repeat**")[0]
        self.enteredtxt.textCursor().removeSelectedText()
        self.enteredtxt.textCursor().insertText(b)
        self.repeatnobox.setValue(0)

    def cleartxtfunc(self):
        self.enteredtxt.clear()
        if os.path.isfile(self.src):
            self.delete_file()

    def playbtnfunc(self):
        if self.playbtn.text() == "Play":
            if self.positionmedia.value() == 0:
                self.wholetxt = self.enteredtxt.toPlainText().split("<repeat**")
                t = []
                tospeak = []
                for i in self.wholetxt:
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
                txt = " ".join(tospeak)
                if os.path.isfile(self.src):
                    self.delete_file()
                self.engine.save_to_file(txt, self.src)
                self.engine.runAndWait()
                self.engine.stop()
                self.playaudio()
                self.playbtn.setText("Pause")
            else:
                if self.enteredtxt.toPlainText().split("<repeat**") == self.wholetxt:
                    self.player.play()
                    self.playbtn.setText("Pause")
                else:
                    self.positionmedia.setValue(0)
                    self.playbtnfunc()
        else:
            self.player.pause()
            self.playbtn.setText("Play")

    def playaudio(self):
        if not os.path.isfile(self.src):
            print("error") #make an error window pop up here
        else:
            self.player.setSource(QUrl.fromLocalFile(self.src))
            self.player.play()

    def playerstatechanged(self):
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

    def delete_file(self):
        self.player.setSource(QUrl(None))
        os.remove(self.src)

    def closeEvent(self, event: QCloseEvent):
        if os.path.isfile(self.src):
            self.delete_file()

    def importtextfunc(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setNameFilter("Files (*.pdf)")
        dialog.setViewMode(QtWidgets.QFileDialog.List)
        file = ""
        if dialog.exec_():
            file = dialog.selectedFiles()[0]
        if file!="":
            reader = PdfReader(file)
            noofpgs = len(reader.pages)
            importedtxt = ""
            for i in range(noofpgs):
                page = reader.pages[i]
                importedtxt = importedtxt + page.extract_text()
            self.enteredtxt.setText(importedtxt)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()