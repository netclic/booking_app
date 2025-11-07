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
        self.actionClient = QAction(MainWindow)
        self.actionClient.setObjectName(u"actionClient")
        self.actionClientListe = QAction(MainWindow)
        self.actionClientListe.setObjectName(u"actionClientListe")
        self.actionEvent = QAction(MainWindow)
        self.actionEvent.setObjectName(u"actionEvent")
        self.actionEventListe = QAction(MainWindow)
        self.actionEventListe.setObjectName(u"actionEventListe")
        self.actionEventSupprimer = QAction(MainWindow)
        self.actionEventSupprimer.setObjectName(u"actionEventSupprimer")
        self.actionClientSupprimer = QAction(MainWindow)
        self.actionClientSupprimer.setObjectName(u"actionClientSupprimer")
        self.actionLogement = QAction(MainWindow)
        self.actionLogement.setObjectName(u"actionLogement")
        self.actionLogementListe = QAction(MainWindow)
        self.actionLogementListe.setObjectName(u"actionLogementListe")
        self.actionLogementSupprimer = QAction(MainWindow)
        self.actionLogementSupprimer.setObjectName(u"actionLogementSupprimer")
        self.actionExporter_le_calendrier = QAction(MainWindow)
        self.actionExporter_le_calendrier.setObjectName(u"actionExporter_le_calendrier")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(380, 0, 421, 25))
        font = QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(50, 0, 101, 26))
        self.spinBox.setFont(font)
        self.spinBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setFrame(True)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox.setAccelerated(False)
        self.spinBox.setProperty(u"showGroupSeparator", False)
        self.spinBox.setMinimum(2025)
        self.spinBox.setMaximum(2050)
        self.spinBox.setValue(2025)
        self.T_logement = QLabel(self.centralwidget)
        self.T_logement.setObjectName(u"T_logement")
        self.T_logement.setGeometry(QRect(280, 0, 91, 20))
        self.T_logement.setFont(font)
        self.T_logement.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 51, 17))
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 30, 801, 521))
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMinimumDate(QDate(2025, 1, 1))
        self.calendarWidget.setMaximumDate(QDate(2060, 12, 31))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.LongDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuLogements = QMenu(self.menubar)
        self.menuLogements.setObjectName(u"menuLogements")
        self.menuR_servations = QMenu(self.menubar)
        self.menuR_servations.setObjectName(u"menuR_servations")
        self.menuClients = QMenu(self.menubar)
        self.menuClients.setObjectName(u"menuClients")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuLogements.menuAction())
        self.menubar.addAction(self.menuR_servations.menuAction())
        self.menubar.addAction(self.menuClients.menuAction())
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionExporter_le_calendrier)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuLogements.addAction(self.actionLogement)
        self.menuLogements.addAction(self.actionLogementListe)
        self.menuLogements.addAction(self.actionLogementSupprimer)
        self.menuR_servations.addAction(self.actionEvent)
        self.menuR_servations.addAction(self.actionEventListe)
        self.menuR_servations.addAction(self.actionEventSupprimer)
        self.menuClients.addAction(self.actionClient)
        self.menuClients.addAction(self.actionClientListe)
        self.menuClients.addAction(self.actionClientSupprimer)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionClient.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.actionClientListe.setText(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.actionEvent.setText(QCoreApplication.translate("MainWindow", u"Nouvelle", None))
        self.actionEventListe.setText(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.actionEventSupprimer.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actionClientSupprimer.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actionLogement.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.actionLogementListe.setText(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.actionLogementSupprimer.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actionExporter_le_calendrier.setText(QCoreApplication.translate("MainWindow", u"Exporter le calendrier", None))
        self.T_logement.setText(QCoreApplication.translate("MainWindow", u"Logement :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e :", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuLogements.setTitle(QCoreApplication.translate("MainWindow", u"Logements", None))
        self.menuR_servations.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9servations", None))
        self.menuClients.setTitle(QCoreApplication.translate("MainWindow", u"Clients", None))
    # retranslateUi

