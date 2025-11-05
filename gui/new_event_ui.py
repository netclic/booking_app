# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_event.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_NewEventForm(object):
    def setupUi(self, NewEventForm):
        if not NewEventForm.objectName():
            NewEventForm.setObjectName(u"NewEventForm")
        NewEventForm.resize(500, 450)
        self.verticalLayout = QVBoxLayout(NewEventForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(NewEventForm)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_client = QLabel(NewEventForm)
        self.label_client.setObjectName(u"label_client")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_client)

        self.comboBox_client = QComboBox(NewEventForm)
        self.comboBox_client.setObjectName(u"comboBox_client")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_client)

        self.label_logement = QLabel(NewEventForm)
        self.label_logement.setObjectName(u"label_logement")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_logement)

        self.comboBox_logement = QComboBox(NewEventForm)
        self.comboBox_logement.setObjectName(u"comboBox_logement")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_logement)

        self.label_status = QLabel(NewEventForm)
        self.label_status.setObjectName(u"label_status")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_status)

        self.comboBox_statut = QComboBox(NewEventForm)
        self.comboBox_statut.addItem("")
        self.comboBox_statut.addItem("")
        self.comboBox_statut.addItem("")
        self.comboBox_statut.addItem("")
        self.comboBox_statut.setObjectName(u"comboBox_statut")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_statut)

        self.label_date_debut = QLabel(NewEventForm)
        self.label_date_debut.setObjectName(u"label_date_debut")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_date_debut)

        self.dateEdit_debut = QDateEdit(NewEventForm)
        self.dateEdit_debut.setObjectName(u"dateEdit_debut")
        self.dateEdit_debut.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateEdit_debut)

        self.label_date_fin = QLabel(NewEventForm)
        self.label_date_fin.setObjectName(u"label_date_fin")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_date_fin)

        self.dateEdit_fin = QDateEdit(NewEventForm)
        self.dateEdit_fin.setObjectName(u"dateEdit_fin")
        self.dateEdit_fin.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dateEdit_fin)

        self.label_description = QLabel(NewEventForm)
        self.label_description.setObjectName(u"label_description")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_description)

        self.textEdit_description = QTextEdit(NewEventForm)
        self.textEdit_description.setObjectName(u"textEdit_description")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.textEdit_description)

        self.label_adultes = QLabel(NewEventForm)
        self.label_adultes.setObjectName(u"label_adultes")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_adultes)

        self.spinBox_adultes = QSpinBox(NewEventForm)
        self.spinBox_adultes.setObjectName(u"spinBox_adultes")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.spinBox_adultes)

        self.label_enfants = QLabel(NewEventForm)
        self.label_enfants.setObjectName(u"label_enfants")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_enfants)

        self.spinBox_enfants = QSpinBox(NewEventForm)
        self.spinBox_enfants.setObjectName(u"spinBox_enfants")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.spinBox_enfants)

        self.label_type = QLabel(NewEventForm)
        self.label_type.setObjectName(u"label_type")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_type)

        self.comboBox_type = QComboBox(NewEventForm)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.comboBox_type)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.button_save = QPushButton(NewEventForm)
        self.button_save.setObjectName(u"button_save")

        self.horizontalLayout_buttons.addWidget(self.button_save)

        self.button_cancel = QPushButton(NewEventForm)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout_buttons.addWidget(self.button_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)


        self.retranslateUi(NewEventForm)

        QMetaObject.connectSlotsByName(NewEventForm)
    # setupUi

    def retranslateUi(self, NewEventForm):
        NewEventForm.setWindowTitle(QCoreApplication.translate("NewEventForm", u"Nouveau \u00c9v\u00e8nement", None))
        self.label_title.setText(QCoreApplication.translate("NewEventForm", u"Cr\u00e9er un nouvel \u00e9v\u00e8nement", None))
        self.label_client.setText(QCoreApplication.translate("NewEventForm", u"Client :", None))
        self.label_logement.setText(QCoreApplication.translate("NewEventForm", u"Logement :", None))
        self.label_status.setText(QCoreApplication.translate("NewEventForm", u"Statut :", None))
        self.comboBox_statut.setItemText(0, QCoreApplication.translate("NewEventForm", u"Demande", None))
        self.comboBox_statut.setItemText(1, QCoreApplication.translate("NewEventForm", u"En attente", None))
        self.comboBox_statut.setItemText(2, QCoreApplication.translate("NewEventForm", u"Confirm\u00e9e", None))
        self.comboBox_statut.setItemText(3, QCoreApplication.translate("NewEventForm", u"Annul\u00e9e", None))

        self.label_date_debut.setText(QCoreApplication.translate("NewEventForm", u"Date D\u00e9but :", None))
        self.label_date_fin.setText(QCoreApplication.translate("NewEventForm", u"Date Fin :", None))
        self.label_description.setText(QCoreApplication.translate("NewEventForm", u"Description :", None))
        self.label_adultes.setText(QCoreApplication.translate("NewEventForm", u"Nombre d'Adultes :", None))
        self.label_enfants.setText(QCoreApplication.translate("NewEventForm", u"Nombre d'Enfants :", None))
        self.label_type.setText(QCoreApplication.translate("NewEventForm", u"Type :", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("NewEventForm", u"Fermeture", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("NewEventForm", u"R\u00e9servation", None))

        self.button_save.setText(QCoreApplication.translate("NewEventForm", u"Sauvegarder", None))
        self.button_cancel.setText(QCoreApplication.translate("NewEventForm", u"Annuler", None))
    # retranslateUi

