from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PySide6.QtSql import QSqlQuery
from gui.liste_logements_ui import Ui_ListLogementsForm
from db.db_connection import connect_to_db


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
            # Connexion avec QSqlDatabase
            db = connect_to_db()

            if not db.isOpen():
                print("Erreur: La base de données n'est pas ouverte")
                return

            # Créer une requête SQL avec QSqlQuery
            query = QSqlQuery(db)

            # Préparer et exécuter la requête
            query.prepare("""
                          SELECT id, nom, adresse, code_postal, ville, capacite, classement
                          FROM logements
                          ORDER BY nom
                          """)

            if not query.exec():
                print(f"Erreur lors de l'exécution de la requête: {query.lastError().text()}")
                return

            # Désactiver le tri pendant le remplissage
            self.tableWidget.setSortingEnabled(False)

            # Récupérer les résultats et remplir le tableau
            logements = []
            while query.next():
                logement = []
                for i in range(7):  # 7 colonnes
                    value = query.value(i)
                    logement.append(value)
                logements.append(logement)

            # Configurer le tableau
            self.tableWidget.setRowCount(len(logements))

            # Remplir le tableau
            for row_idx, logement in enumerate(logements):
                for col_idx, value in enumerate(logement):
                    # Convertir None en chaîne vide
                    display_value = "" if value is None else str(value)
                    item = QTableWidgetItem(display_value)
                    self.tableWidget.setItem(row_idx, col_idx, item)

            # Réactiver le tri après le remplissage
            self.tableWidget.setSortingEnabled(True)

            print(f"Chargé {len(logements)} logement(s)")  # Message de debug

        except Exception as e:
            print(f"Erreur lors du chargement des logements: {e}")
            import traceback
            traceback.print_exc()