# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCalendarWidget, QComboBox,
    QFrame, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionLogement = QAction(MainWindow)
        self.actionLogement.setObjectName(u"actionLogement")
        self.actionEvent = QAction(MainWindow)
        self.actionEvent.setObjectName(u"actionEvent")
        self.actionVoir_le_calendrier = QAction(MainWindow)
        self.actionVoir_le_calendrier.setObjectName(u"actionVoir_le_calendrier")
        self.actionClient = QAction(MainWindow)
        self.actionClient.setObjectName(u"actionClient")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(380, 0, 421, 25))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(50, 0, 71, 26))
        self.spinBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBox.setAccelerated(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 0, 71, 17))
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 51, 17))
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 30, 801, 521))
        self.calendarWidget.setGridVisible(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionLogement)
        self.menuFichier.addAction(self.actionEvent)
        self.menuFichier.addAction(self.actionClient)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionLogement.setText(QCoreApplication.translate("MainWindow", u"R\u00e9sidence", None))
        self.actionEvent.setText(QCoreApplication.translate("MainWindow", u"R\u00e9servation", None))
        self.actionVoir_le_calendrier.setText(QCoreApplication.translate("MainWindow", u"Calendrier", None))
        self.actionClient.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"R\u00e9sidence :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e :", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
    # retranslateUi