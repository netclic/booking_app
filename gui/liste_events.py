from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt
from gui.liste_events_ui import Ui_ListEventsForm
from db.db_connection import connect_to_db


class ListEventsWindow(QWidget, Ui_ListEventsForm):
    """Fenêtre pour afficher la liste de toutes les réservations"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Connecter les boutons
        self.button_ok.clicked.connect(self.close)
        self.button_delete.clicked.connect(self.delete_selected_event)

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
                db = connect_to_db()
                query = QSqlQuery(db)
                query.prepare("DELETE FROM events WHERE id = ?")
                query.addBindValue(int(event_id))

                if query.exec():
                    # Supprimer la ligne du tableau
                    self.tableWidget.removeRow(row)
                    QMessageBox.information(
                        self,
                        "Suppression réussie",
                        f"La réservation pour '{client_name}' a été supprimée avec succès."
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

    def load_events(self):
        """Charge toutes les réservations depuis la base de données"""
        try:
            # Connexion avec QSqlDatabase
            db = connect_to_db()

            if not db.isOpen():
                print("Erreur: La base de données n'est pas ouverte")
                return

            # Créer une requête SQL avec QSqlQuery avec jointures pour récupérer les noms
            query = QSqlQuery(db)

            # Préparer et exécuter la requête - tri par ID
            query.prepare("""
                          SELECT 
                              e.id,
                              e.client_id,
                              c.nom || ' ' || c.prenom as client_name,
                              e.logement_id,
                              l.nom as logement_name,
                              e.date_debut,
                              e.date_fin,
                              e.prix_total,
                              e.statut
                          FROM events e
                          LEFT JOIN clients c ON e.client_id = c.id
                          LEFT JOIN logements l ON e.logement_id = l.id
                          ORDER BY e.id DESC
                          """)

            if not query.exec():
                print(f"Erreur lors de l'exécution de la requête: {query.lastError().text()}")
                return

            # Désactiver le tri pendant le remplissage
            self.tableWidget.setSortingEnabled(False)

            # Récupérer les résultats et remplir le tableau
            events = []
            while query.next():
                event = []
                for i in range(9):  # 9 colonnes
                    value = query.value(i)
                    event.append(value)
                events.append(event)

            # Configurer le tableau
            self.tableWidget.setRowCount(len(events))

            # Remplir le tableau avec alignement approprié
            for row_idx, event in enumerate(events):
                for col_idx, value in enumerate(event):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)

                    # Alignement : centré pour tout sauf les noms (client et logement)
                    if col_idx == 2 or col_idx == 4:  # client_name et logement_name
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                    else:  # Tous les autres champs centrés
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.tableWidget.setItem(row_idx, col_idx, item)

            # Réactiver le tri après le remplissage
            self.tableWidget.setSortingEnabled(True)

            # Trier par ID (colonne 0) par défaut, ordre décroissant (plus récent en premier)
            self.tableWidget.sortItems(0, Qt.SortOrder.DescendingOrder)

            print(f"Chargé {len(events)} réservation(s)")  # Message de debug

        except Exception as e:
            print(f"Erreur lors du chargement des réservations: {e}")
            import traceback
            traceback.print_exc()