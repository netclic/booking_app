from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt
from gui.liste_clients_ui import Ui_ListClientsForm
from db.db_connection import connect_to_db


class ListClientsWindow(QWidget, Ui_ListClientsForm):
    """Fenêtre pour afficher la liste de tous les clients"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Connecter les boutons
        self.button_ok.clicked.connect(self.close)
        self.button_delete.clicked.connect(self.delete_selected_client)

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
            # Supprimer de la base de données
            try:
                db = connect_to_db()
                query = QSqlQuery(db)
                query.prepare("DELETE FROM clients WHERE id = ?")
                query.addBindValue(int(client_id))

                if query.exec():
                    # Supprimer la ligne du tableau
                    self.tableWidget.removeRow(row)
                    QMessageBox.information(
                        self,
                        "Suppression réussie",
                        f"Le client '{client_nom} {client_prenom}' a été supprimé avec succès."
                    )
                else:
                    QMessageBox.critical(
                        self,
                        "Erreur de suppression",
                        f"Erreur lors de la suppression : {query.lastError().text()}"
                    )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Une erreur s'est produite : {str(e)}"
                )

    def load_clients(self):
        """Charge tous les clients depuis la base de données"""
        try:
            # Connexion avec QSqlDatabase
            db = connect_to_db()

            if not db.isOpen():
                print("Erreur: La base de données n'est pas ouverte")
                return

            # Créer une requête SQL avec QSqlQuery
            query = QSqlQuery(db)

            # Préparer et exécuter la requête - tri par ID
            query.prepare("""
                          SELECT id, nom, prenom, email, telephone, adresse, code_postal, ville
                          FROM clients
                          ORDER BY id
                          """)

            if not query.exec():
                print(f"Erreur lors de l'exécution de la requête: {query.lastError().text()}")
                return

            # Désactiver le tri pendant le remplissage
            self.tableWidget.setSortingEnabled(False)

            # Récupérer les résultats et remplir le tableau
            clients = []
            while query.next():
                client = []
                for i in range(8):  # 8 colonnes
                    value = query.value(i)
                    client.append(value)
                clients.append(client)

            # Configurer le tableau
            self.tableWidget.setRowCount(len(clients))

            # Remplir le tableau avec alignement approprié
            for row_idx, client in enumerate(clients):
                for col_idx, value in enumerate(client):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)

                    # Alignement : centré sauf pour email (col 3) et adresse (col 5)
                    if col_idx == 3 or col_idx == 5:  # email et adresse
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                    else:  # ID, nom, prénom, téléphone, code postal, ville
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.tableWidget.setItem(row_idx, col_idx, item)

            # Réactiver le tri après le remplissage
            self.tableWidget.setSortingEnabled(True)

            # Trier par ID (colonne 0) par défaut
            self.tableWidget.sortItems(0, Qt.SortOrder.AscendingOrder)

            print(f"Chargé {len(clients)} client(s)")  # Message de debug

        except Exception as e:
            print(f"Erreur lors du chargement des clients: {e}")
            import traceback
            traceback.print_exc()