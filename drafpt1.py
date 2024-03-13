import sys, re
from PySide6 import QtWidgets
from draft1ui import Ui_MainWindow


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
        print(self.enteredtxt.toPlainText())
        wholetxt = self.enteredtxt.toPlainText()
        temptxt = ""

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