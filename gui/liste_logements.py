from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from gui.list_logements_ui import Ui_ListLogementsForm
from db.db_connection import get_connection


class ListLogementsWindow(QWidget, Ui_ListLogementsForm):
    """Fenêtre pour afficher la liste de tous les logements"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Connecter le bouton OK
        self.button_ok.clicked.connect(self.close)

        # Charger les données
        self.load_logements()

        # Ajuster la taille des colonnes
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def load_logements(self):
        """Charge tous les logements depuis la base de données"""
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Récupérer tous les logements
            cursor.execute("""
                           SELECT id, nom, adresse, code_postal, ville, capacite, classement
                           FROM logements
                           ORDER BY nom
                           """)

            logements = cursor.fetchall()

            # Configurer le tableau
            self.tableWidget.setRowCount(len(logements))

            # Remplir le tableau
            for row_idx, logement in enumerate(logements):
                for col_idx, value in enumerate(logement):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)
                    self.tableWidget.setItem(row_idx, col_idx, item)

            conn.close()

        except Exception as e:
            print(f"Erreur lors du chargement des logements: {e}")