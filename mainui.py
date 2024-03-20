from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        basedir = os.path.dirname(__file__)
        icon = QIcon(os.path.join(basedir, 'mainicon.png'))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toplabel = QLabel(self.centralwidget)
        self.toplabel.setObjectName(u"toplabel")

        self.verticalLayout_3.addWidget(self.toplabel)

        self.enteredtxt = QTextEdit(self.centralwidget)
        self.enteredtxt.setObjectName(u"enteredtxt")
        self.enteredtxt.setFrameShadow(QFrame.Plain)

        self.verticalLayout_3.addWidget(self.enteredtxt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playbtn = QPushButton(self.centralwidget)
        self.playbtn.setObjectName(u"playbtn")

        self.horizontalLayout.addWidget(self.playbtn)

        self.positionmedia = QSlider(self.centralwidget)
        self.positionmedia.setObjectName(u"positionmedia")
        self.positionmedia.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.positionmedia)

        self.importtxt = QPushButton(self.centralwidget)
        self.importtxt.setObjectName(u"importtxt")

        self.horizontalLayout.addWidget(self.importtxt)

        self.clearbtn = QPushButton(self.centralwidget)
        self.clearbtn.setObjectName(u"clearbtn")

        self.horizontalLayout.addWidget(self.clearbtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rlabel = QLabel(self.centralwidget)
        self.rlabel.setObjectName(u"rlabel")

        self.verticalLayout.addWidget(self.rlabel)

        self.r1label = QLabel(self.centralwidget)
        self.r1label.setObjectName(u"r1label")
        self.r1label.setWordWrap(False)

        self.verticalLayout.addWidget(self.r1label)

        self.repeatnobox = QSpinBox(self.centralwidget)
        self.repeatnobox.setObjectName(u"repeatnobox")

        self.verticalLayout.addWidget(self.repeatnobox)

        self.savebtn = QPushButton(self.centralwidget)
        self.savebtn.setObjectName(u"savebtn")

        self.verticalLayout.addWidget(self.savebtn)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName(u"resetbtn")

        self.verticalLayout.addWidget(self.resetbtn)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.voiceinfolabel = QLabel(self.centralwidget)
        self.voiceinfolabel.setObjectName(u"voiceinfolabel")

        self.verticalLayout_2.addWidget(self.voiceinfolabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.vlabel1 = QLabel(self.centralwidget)
        self.vlabel1.setObjectName(u"vlabel1")

        self.gridLayout.addWidget(self.vlabel1, 0, 0, 1, 1)

        self.voicegendercombobox = QComboBox(self.centralwidget)
        self.voicegendercombobox.setObjectName(u"voicegendercombobox")

        self.gridLayout.addWidget(self.voicegendercombobox, 0, 1, 1, 1)

        self.vlabel2 = QLabel(self.centralwidget)
        self.vlabel2.setObjectName(u"vlabel2")

        self.gridLayout.addWidget(self.vlabel2, 1, 0, 1, 1)

        self.voiceratespinbox = QSpinBox(self.centralwidget)
        self.voiceratespinbox.setObjectName(u"voiceratespinbox")
        self.voiceratespinbox.setMaximum(1000)
        self.voiceratespinbox.setSingleStep(5)

        self.gridLayout.addWidget(self.voiceratespinbox, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.applyvoicebtn = QPushButton(self.centralwidget)
        self.applyvoicebtn.setObjectName(u"applyvoicebtn")

        self.verticalLayout_2.addWidget(self.applyvoicebtn)

        self.resetvoicebtn = QPushButton(self.centralwidget)
        self.resetvoicebtn.setObjectName(u"resetvoicebtn")

        self.verticalLayout_2.addWidget(self.resetvoicebtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Speak to me", None))
        self.toplabel.setText(QCoreApplication.translate("MainWindow", u"Enter text", None))
        self.playbtn.setText(QCoreApplication.translate("MainWindow", u"Play", None))
#if QT_CONFIG(tooltip)
        self.importtxt.setToolTip(QCoreApplication.translate("MainWindow", u"Only PDF files are supported", None))
#endif // QT_CONFIG(tooltip)
        self.importtxt.setText(QCoreApplication.translate("MainWindow", u"Import Text", None))
        self.clearbtn.setText(QCoreApplication.translate("MainWindow", u"Clear text", None))
        self.rlabel.setText(QCoreApplication.translate("MainWindow", u"Repeat info:", None))
        self.r1label.setText(QCoreApplication.translate("MainWindow", u"Selection to be repeaten:", None))
        self.savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.resetbtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.voiceinfolabel.setText(QCoreApplication.translate("MainWindow", u"Voice info:", None))
        self.vlabel1.setText(QCoreApplication.translate("MainWindow", u"Voice type:", None))
        self.vlabel2.setText(QCoreApplication.translate("MainWindow", u"Voice rate:", None))
        self.applyvoicebtn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.resetvoicebtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

