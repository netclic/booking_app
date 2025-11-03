import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.main_gui import Ui_MainWindow
from db.db_setup import setup_db
from db.db_connection import connect_to_db

def main():
    # Initialiser la base de données (création de tables si nécessaire)
    setup_db()

    # Lancer l'application PySide6
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    # Charger l'interface utilisateur
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    # Connecter à la base de données (via QSqlDatabase)
    connect_to_db()

    # Afficher la fenêtre principale
    main_window.show()

    # Exécuter l'application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()