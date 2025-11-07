# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_liste_clients.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore, QtGui, QtWidgets


class Ui_ListClientsForm(object):
    def setupUi(self, ListClientsForm):
        ListClientsForm.setObjectName("ListClientsForm")
        ListClientsForm.resize(900, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListClientsForm)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_title = QtWidgets.QLabel(ListClientsForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)

        self.tableWidget = QtWidgets.QTableWidget(ListClientsForm)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_buttons.addItem(spacerItem)
        self.button_delete = QtWidgets.QPushButton(ListClientsForm)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout_buttons.addWidget(self.button_delete)
        self.button_ok = QtWidgets.QPushButton(ListClientsForm)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_buttons.addWidget(self.button_ok)
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        self.retranslateUi(ListClientsForm)
        QtCore.QMetaObject.connectSlotsByName(ListClientsForm)

    def retranslateUi(self, ListClientsForm):
        _translate = QtCore.QCoreApplication.translate
        ListClientsForm.setWindowTitle(_translate("ListClientsForm", "Liste des Clients"))
        self.label_title.setText(_translate("ListClientsForm", "Liste des Clients"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ListClientsForm", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ListClientsForm", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ListClientsForm", "Prénom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ListClientsForm", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ListClientsForm", "Téléphone"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ListClientsForm", "Adresse"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ListClientsForm", "Code Postal"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ListClientsForm", "Ville"))
        self.button_delete.setText(_translate("ListClientsForm", "Supprimer"))
        self.button_ok.setText(_translate("ListClientsForm", "OK"))