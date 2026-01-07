from db.db_connection import connect_to_db
from db.models.events import Event
from db.models.logements import Logement
from gui.liste_events_ui import Ui_ListEventsForm
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt


class ListEventsWindow(QWidget, Ui_ListEventsForm):
    """Fenêtre pour afficher la liste de toutes les réservations"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.events = None
        self.setupUi(self)

        # Connecter les boutons
        self.button_ok.clicked.connect(self.close)
        self.button_delete.clicked.connect(self.delete_selected_event)

        # Créer une instance de la classe Client
        self.event = Event()

        # Charger les données
        self.load_events()

        # Ajuster la taille des colonnes
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def delete_selected_event(self):
        """Supprime la réservation sélectionnée après confirmation"""
        # Vérifier qu'une ligne est sélectionnée
        selected_rows = self.tableWidget.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(
                self,
                "Aucune sélection",
                "Veuillez sélectionner une réservation à supprimer."
            )
            return

        # Récupérer les informations de la réservation sélectionnée
        row = selected_rows[0].row()
        event_id = self.tableWidget.item(row, 0).text()
        client_name = self.tableWidget.item(row, 2).text()
        logement_name = self.tableWidget.item(row, 4).text()
        date_debut = self.tableWidget.item(row, 5).text()
        date_fin = self.tableWidget.item(row, 6).text()

        # Demander confirmation
        reply = QMessageBox.question(
            self,
            "Confirmation de suppression",
            f"Êtes-vous sûr de vouloir supprimer la réservation :\n\n"
            f"ID: {event_id}\n"
            f"Client: {client_name}\n"
            f"Logement: {logement_name}\n"
            f"Du {date_debut} au {date_fin}\n\n"
            f"Cette action est irréversible.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Supprimer de la base de données
            try:
                # Supprimer le client via la méthode delete de la classe Client
                self.event.delete(int(event_id))

                # Supprimer la ligne du tableau
                self.tableWidget.removeRow(row)
                QMessageBox.information(
                    self,
                    "Suppression réussie",
                    f"La réservation pour '{client_name}' a été supprimée avec succès."
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur de suppression",
                    f"Une erreur s'est produite lors de la suppression : {str(e)}"
                )

    def load_events(self):
        """Charge toutes les réservations depuis la base de données"""
        try:
            # Connexion avec QSqlDatabase
            db = connect_to_db()
            if not db.isOpen():
                print("Erreur: La base de données n'est pas ouverte")
                return

            self.events = Event().load_all()

            if not self.events:
                print("Aucun client trouvé.")
                return

           # Désactiver le tri pendant le remplissage
            self.tableWidget.setSortingEnabled(False)

            # Configurer le tableau
            self.tableWidget.setRowCount(len(self.events))

            # Remplir le tableau avec alignement approprié
            for row_idx, event in enumerate(self.events):
                for col_idx, value in enumerate(
                        [event.id, event.client_id, event.nom, event.logement_id, event.logement_name, event.date_debut,
                         event.date_fin]):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)
                    # Alignement : centré
                    if col_idx == 3 or col_idx == 5:  #
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                    else:  # ID, nom, prénom, téléphone, code postal, ville
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)
            print(f"Chargé {len(self.events)} réservation(s)")  # Message de debug

            # Réactiver le tri après le remplissage
            self.tableWidget.setSortingEnabled(True)

            # Trier par ID (colonne 0) par défaut, ordre décroissant (plus récent en premier)
            self.tableWidget.sortItems(0, Qt.SortOrder.DescendingOrder)

        except Exception as e:
            print(f"Erreur lors du chargement des réservations: {e}")
            import traceback
            traceback.print_exc()