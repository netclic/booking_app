from db.db_connection import connect_to_db
from db.models.logements import Logement
from gui.liste_logements_ui import Ui_ListLogementsForm
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt


class ListLogementsWindow(QWidget, Ui_ListLogementsForm):
    """Fenêtre pour afficher la liste de tous les logements"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logement = None
        self.setupUi(self)

        # Connecter les boutons
        self.button_ok.clicked.connect(self.close)
        self.button_delete.clicked.connect(self.delete_selected_logement)

        # Créer une instance de la classe Logement
        self.logement = Logement()

        # Charger les données
        self.load_logements()

        # Ajuster la taille des colonnes
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def delete_selected_logement(self):
        """Supprime le logement sélectionné après confirmation"""
        # Vérifier qu'une ligne est sélectionnée
        selected_rows = self.tableWidget.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(
                self,
                "Aucune sélection",
                "Veuillez sélectionner un logement à supprimer."
            )
            return

        # Récupérer l'ID et le nom du logement sélectionné
        row = selected_rows[0].row()
        logement_id = self.tableWidget.item(row, 0).text()
        logement_nom = self.tableWidget.item(row, 1).text()

        # Demander confirmation
        reply = QMessageBox.question(
            self,
            "Confirmation de suppression",
            f"Êtes-vous sûr de vouloir supprimer le logement :\n\n"
            f"ID: {logement_id}\n"
            f"Nom: {logement_nom}\n\n"
            f"Cette action est irréversible.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:

            try:
                #Supprimer le logement via la méthode delete de la classe
                self.logement.delete(int(logement_id))

                # Supprimer la ligne du tableau
                self.tableWidget.removeRow(row)
                QMessageBox.information(
                    self,
                    "Suppression réussie",
                    f"Le logement '{logement_nom}' a été supprimé avec succès."
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur de suppression",
                    f"Une erreur s'est produite lors de la suppression : {str(e)}"
                )

    def load_logements(self):
        """Charge tous les logements depuis la base de données"""
        try:
            # Charger tous les logements via la méthode load_all de la classe Logement
            self.logements = Logement.load_all()

            if not self.logements:
                print("Aucun logement trouvé.")
                return

            # Désactiver le tri pendant le remplissage
            self.tableWidget.setSortingEnabled(False)

            # Configurer le tableau
            self.tableWidget.setRowCount(len(self.logements))

            # Remplir le tableau avec alignement approprié
            for row_idx, logement in enumerate(self.logements):
                for col_idx, value in enumerate(
                        [logement.id, logement.nom, logement.adresse, logement.code_postal, logement.ville,
                         logement.capacite, logement.classement]):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)

                    # Alignement : centré sauf pour nom (col 1) et adresse (col 2)
                    if col_idx == 1 or col_idx == 2:  # nom et adresse
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                    else:  # ID, code postal, ville, capacité, classement
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.tableWidget.setItem(row_idx, col_idx, item)
            print(f"Chargé {len(self.logements)} logement(s)")  # Message de debug

            # Réactiver le tri après le remplissage
            self.tableWidget.setSortingEnabled(True)

            # Trier par ID (colonne 0) par défaut
            self.tableWidget.sortItems(0, Qt.SortOrder.AscendingOrder)


        except Exception as e:
            print(f"Erreur lors du chargement des logements: {e}")
            import traceback
            traceback.print_exc()