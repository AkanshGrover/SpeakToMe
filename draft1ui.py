# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'draft1cBxuiE.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toplabel = QLabel(self.centralwidget)
        self.toplabel.setObjectName(u"toplabel")

        self.verticalLayout.addWidget(self.toplabel)

        self.enteredtxt = QTextEdit(self.centralwidget)
        self.enteredtxt.setObjectName(u"enteredtxt")
        self.enteredtxt.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.enteredtxt)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.rlabel = QLabel(self.centralwidget)
        self.rlabel.setObjectName(u"rlabel")

        self.verticalLayout_2.addWidget(self.rlabel)

        self.r1label = QLabel(self.centralwidget)
        self.r1label.setObjectName(u"r1label")
        self.r1label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.r1label)

        self.repeatnobox = QSpinBox(self.centralwidget)
        self.repeatnobox.setObjectName(u"repeatnobox")

        self.verticalLayout_2.addWidget(self.repeatnobox)

        self.resetbtn = QPushButton(self.centralwidget)
        self.resetbtn.setObjectName(u"resetbtn")

        self.verticalLayout_2.addWidget(self.resetbtn)

        self.savebtn = QPushButton(self.centralwidget)
        self.savebtn.setObjectName(u"savebtn")

        self.verticalLayout_2.addWidget(self.savebtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.clearbtn = QPushButton(self.centralwidget)
        self.clearbtn.setObjectName(u"clearbtn")

        self.verticalLayout_3.addWidget(self.clearbtn)

        self.playbtn = QPushButton(self.centralwidget)
        self.playbtn.setObjectName(u"playbtn")

        self.verticalLayout_3.addWidget(self.playbtn)

        self.replaybtn = QPushButton(self.centralwidget)
        self.replaybtn.setObjectName(u"replaybtn")

        self.verticalLayout_3.addWidget(self.replaybtn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Speak for me", None))
        self.toplabel.setText(QCoreApplication.translate("MainWindow", u"Enter text", None))
        self.rlabel.setText(QCoreApplication.translate("MainWindow", u"Repeat info:", None))
        self.r1label.setText(QCoreApplication.translate("MainWindow", u"Selection to be repeaten:", None))
        self.resetbtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.savebtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.clearbtn.setText(QCoreApplication.translate("MainWindow", u"Clear text", None))
        self.playbtn.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.replaybtn.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
    # retranslateUi
