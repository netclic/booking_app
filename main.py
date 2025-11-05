import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTranslator, QLibraryInfo
from gui.main_gui import Ui_MainWindow
from gui.new_event import NewEventForm
from gui.new_logement import NewLogementForm
from db.db_setup import setup_db
from db.db_connection import connect_to_db


def handle_quit():
    """Afficher une boîte de dialogue de confirmation avant de quitter."""
    reply = QMessageBox.question(
        None,
        "Quitter l'application",
        "Êtes-vous sûr de vouloir quitter l'application ?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )

    if reply == QMessageBox.StandardButton.Yes:
        QApplication.quit()


def main():
    # Initialiser l'application Qt
    app = QApplication(sys.argv)

    # Charge manuellement le fichier de traduction
    translator = QTranslator()
    if translator.load("translations/qtbase_fr.qm"):
        app.installTranslator(translator)

    # Connecter à la base de données
    connect_to_db()

    # Initialiser ou créer les tables SQLite
    setup_db()

    # Lancer la fenêtre principale
    main_window = QMainWindow()

    # Charger l'interface utilisateur
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    # Ajouter une référence pour pouvoir afficher NewEventForm dans le futur
    def open_new_event_form():
        # Conserver la référence pour ne pas perdre l'objet
        new_event_window = NewEventForm()
        main_window.new_event_window = new_event_window
        new_event_window.show()

    # Ajouter une référence pour pouvoir afficher NewLogementForm dans le futur
    def open_new_logements_form():
        # Conserver la référence pour ne pas perdre l'objet
        new_logement_window = NewLogementForm()
        main_window.new_logement_window = new_logement_window
        new_logement_window.show()

    # Connecter le menu "Réservations" à l'ouverture de NewEventForm
    ui.actionEvent.triggered.connect(open_new_event_form)
    ui.actionLogement.triggered.connect(open_new_logements_form)

    # Connecter le menu "Quitter" à la méthode handle_quit
    ui.actionQuitter.triggered.connect(handle_quit)

    # Afficher la fenêtre principale
    main_window.show()

    # Exécuter la boucle de l'application Qt
    sys.exit(app.exec())

if __name__ == "__main__":
    main()