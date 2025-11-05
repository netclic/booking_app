# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_logement.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_NewLogementForm(object):
    def setupUi(self, NewLogementForm):
        if not NewLogementForm.objectName():
            NewLogementForm.setObjectName(u"NewLogementForm")
        NewLogementForm.resize(400, 300)
        self.verticalLayout = QVBoxLayout(NewLogementForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeft)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_nom = QLabel(NewLogementForm)
        self.label_nom.setObjectName(u"label_nom")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_nom)

        self.input_nom = QLineEdit(NewLogementForm)
        self.input_nom.setObjectName(u"input_nom")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_nom)

        self.label_adresse = QLabel(NewLogementForm)
        self.label_adresse.setObjectName(u"label_adresse")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_adresse)

        self.input_adresse = QLineEdit(NewLogementForm)
        self.input_adresse.setObjectName(u"input_adresse")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_adresse)

        self.label_code_postal = QLabel(NewLogementForm)
        self.label_code_postal.setObjectName(u"label_code_postal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_code_postal)

        self.input_code_postal = QLineEdit(NewLogementForm)
        self.input_code_postal.setObjectName(u"input_code_postal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_code_postal)

        self.label_ville = QLabel(NewLogementForm)
        self.label_ville.setObjectName(u"label_ville")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_ville)

        self.input_ville = QLineEdit(NewLogementForm)
        self.input_ville.setObjectName(u"input_ville")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_ville)

        self.label_capacite = QLabel(NewLogementForm)
        self.label_capacite.setObjectName(u"label_capacite")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_capacite)

        self.input_capacite = QSpinBox(NewLogementForm)
        self.input_capacite.setObjectName(u"input_capacite")
        self.input_capacite.setMinimum(1)
        self.input_capacite.setMaximum(50)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.input_capacite)

        self.label_classement = QLabel(NewLogementForm)
        self.label_classement.setObjectName(u"label_classement")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_classement)

        self.input_classement = QLineEdit(NewLogementForm)
        self.input_classement.setObjectName(u"input_classement")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.input_classement)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.button_save = QPushButton(NewLogementForm)
        self.button_save.setObjectName(u"button_save")

        self.buttonLayout.addWidget(self.button_save)

        self.button_cancel = QPushButton(NewLogementForm)
        self.button_cancel.setObjectName(u"button_cancel")

        self.buttonLayout.addWidget(self.button_cancel)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(NewLogementForm)

        QMetaObject.connectSlotsByName(NewLogementForm)
    # setupUi

    def retranslateUi(self, NewLogementForm):
        NewLogementForm.setWindowTitle(QCoreApplication.translate("NewLogementForm", u"Saisir un nouveau logement", None))
        self.label_nom.setText(QCoreApplication.translate("NewLogementForm", u"Nom :", None))
        self.label_adresse.setText(QCoreApplication.translate("NewLogementForm", u"Adresse :", None))
        self.label_code_postal.setText(QCoreApplication.translate("NewLogementForm", u"Code postal :", None))
        self.label_ville.setText(QCoreApplication.translate("NewLogementForm", u"Ville :", None))
        self.label_capacite.setText(QCoreApplication.translate("NewLogementForm", u"Capacit\u00e9 :", None))
        self.label_classement.setText(QCoreApplication.translate("NewLogementForm", u"Classement :", None))
        self.button_save.setText(QCoreApplication.translate("NewLogementForm", u"Enregistrer", None))
        self.button_cancel.setText(QCoreApplication.translate("NewLogementForm", u"Annuler", None))
    # retranslateUi

