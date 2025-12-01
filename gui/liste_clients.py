from db.db_connection import connect_to_db
from db.models.clients import Client
from gui.liste_clients_ui import Ui_ListClientsForm
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox


class ListClientsWindow(QWidget, Ui_ListClientsForm):
    """Fenêtre pour afficher la liste de tous les clients"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clients = None
        self.setupUi(self)

        # Connecter les boutons
        self.button_ok.clicked.connect(self.close)
        self.button_delete.clicked.connect(self.delete_selected_client)

        # Créer une instance de la classe Client
        self.client = Client()

        # Charger les données
        self.load_clients()

        # Ajuster la taille des colonnes
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def delete_selected_client(self):
        """Supprime le client sélectionné après confirmation"""
        # Vérifier qu'une ligne est sélectionnée
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(
                self,
                "Aucune sélection",
                "Veuillez sélectionner un client à supprimer."
            )
            return
        # Récupérer l'ID, le nom et le prénom du client sélectionné
        row = selected_rows[0].row()
        client_id = self.tableWidget.item(row, 0).text()
        client_nom = self.tableWidget.item(row, 1).text()
        client_prenom = self.tableWidget.item(row, 2).text()

        # Demander confirmation
        reply = QMessageBox.question(
            self,
            "Confirmation de suppression",
            f"Êtes-vous sûr de vouloir supprimer le client :\n\n"
            f"ID: {client_id}\n"
            f"Nom: {client_nom} {client_prenom}\n\n"
            f"Cette action est irréversible.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Supprimer le client via la méthode delete de la classe Client
                self.client.delete(int(client_id))
                # Supprimer la ligne du tableau
                self.tableWidget.removeRow(row)
                QMessageBox.information(
                    self,
                    "Suppression réussie",
                    f"Le client '{client_nom} {client_prenom}' a été supprimé avec succès."
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur de suppression",
                    f"Erreur lors de la suppression : {str(e)}"
                )

    def load_clients(self):
        """Charge tous les clients depuis la base de données"""
        try:
            # Connexion avec QSqlDatabase
            db = connect_to_db()
            if not db.isOpen():
                print("Erreur: La base de données n'est pas ouverte")
                return

            # Charger tous les clients via la méthode load_all de la classe Client
            self.clients = Client.load_all()

            if not self.clients:
                print("Aucun client trouvé.")
                return

            # Désactiver le tri pendant le remplissage
            self.tableWidget.setSortingEnabled(False)

            # Configurer le tableau
            self.tableWidget.setRowCount(len(self.clients))

            # Remplir le tableau avec alignement approprié
            for row_idx, client in enumerate(self.clients):
                for col_idx, value in enumerate(
                        [client.id, client.nom, client.prenom, client.email, client.telephone, client.adresse,
                         client.code_postal, client.ville]):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)
                    # Alignement : centré sauf pour email (col 3) et adresse (col 5)
                    if col_idx == 3 or col_idx == 5:  # email et adresse
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                    else:  # ID, nom, prénom, téléphone, code postal, ville
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)
            print(f"Chargé {len(self.clients)} client(s)")  # Message de debug

            # Réactiver le tri après le remplissage
            self.tableWidget.setSortingEnabled(True)

            # Trier par ID (colonne 0) par défaut
            self.tableWidget.sortItems(0, Qt.SortOrder.AscendingOrder)


        except Exception as e:
            print(f"Erreur lors du chargement des clients: {e}")
            import traceback
            traceback.print_exc()