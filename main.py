
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTranslator, QLibraryInfo
from gui.main_gui import Ui_MainWindow
from gui.new_client import NewClientForm
from PySide6.QtGui import QGuiApplication
from gui.new_event import NewEventForm
from gui.new_logement import NewLogementForm
from gui.liste_logements import ListLogementsWindow
from gui.liste_clients import ListClientsWindow
from gui.liste_events import ListEventsWindow
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

    # Appliquer le thème pastel à toute l'application
    app.setStyleSheet("""
        QMainWindow {
            background-color: #F8F9FA;
        }

        QPushButton {
            background-color: #A8D8EA;
            color: #495057;
            border: 1px solid #E9ECEF;
            border-radius: 5px;
            padding: 8px 15px;
            font-weight: 500;
        }

        QPushButton:hover {
            background-color: #E6E6FA;
        }

        QPushButton:pressed {
            background-color: #DDA0DD;
        }

        QLineEdit, QTextEdit {
            background-color: #FFFFFF;
            border: 2px solid #E9ECEF;
            border-radius: 5px;
            padding: 5px;
            color: #495057;
        }

        QLineEdit:focus, QTextEdit:focus {
            border: 2px solid #A8D8EA;
        }

        QLabel {
            color: #495057;
        }

        QComboBox {
            background-color: #FFFFFF;
            border: 2px solid #E9ECEF;
            border-radius: 5px;
            padding: 5px;
            color: #495057;
        }

        QComboBox:focus {
            border: 2px solid #A8D8EA;
        }

        QComboBox::drop-down {
            border: none;
            background-color: #E6E6FA;
        }

        QTableWidget {
            background-color: #FFFFFF;
            alternate-background-color: #F8F9FA;
            selection-background-color: #B8E6F0;
            selection-color: #2C3E50;
            gridline-color: #E9ECEF;
            border: 1px solid #E9ECEF;
        }

        QTableWidget::item:hover {
            background-color: #D4F1F9;
            color: #2C3E50;
        }

        QTableWidget::item:selected {
            background-color: #A8D8EA;
            color: #2C3E50;
        }

        QHeaderView::section {
            background-color: #E6E6FA;
            color: #495057;
            padding: 5px;
            border: 1px solid #D1D1E0;
            font-weight: bold;
        }

        QMenuBar {
            background-color: #A8D8EA;
            color: #495057;
        }

        QMenuBar::item:selected {
            background-color: #E6E6FA;
        }

        QMenu {
            background-color: #FFFFFF;
            border: 1px solid #E9ECEF;
        }

        QMenu::item:selected {
            background-color: #FFB6C1;
        }
    """)

    # Connecter à la base de données
    connect_to_db()

    # Initialiser ou créer les tables SQLite
    setup_db()

    # Lancer la fenêtre principale
    main_window = QMainWindow()

    # Charger l'interface utilisateur
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    # Centrer la fenêtre principale sur l'écran
    screen = QGuiApplication.primaryScreen().geometry()
    window_size = main_window.frameGeometry()
    x = (screen.width() - window_size.width()) // 2
    y = (screen.height() - window_size.height()) // 2
    main_window.move(x, y)

    # Ajouter une référence pour pouvoir afficher NewClientForm dans le futur
    def open_new_client_form():
        # Conserver la référence pour ne pas perdre l'objet
        new_client_window = NewClientForm()
        main_window.new_client_window = new_client_window
        new_client_window.show()

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

    # Ajouter une référence pour pouvoir afficher la liste des logements
    def open_list_logements():
        # Conserver la référence pour ne pas perdre l'objet
        list_logements_window = ListLogementsWindow()
        main_window.list_logements_window = list_logements_window
        list_logements_window.show()

    # Ajouter une référence pour pouvoir afficher la liste des clients
    def open_list_clients():
        # Conserver la référence pour ne pas perdre l'objet
        list_clients_window = ListClientsWindow()
        main_window.list_clients_window = list_clients_window
        list_clients_window.show()

    # Ajouter une référence pour pouvoir afficher la liste des réservations
    def open_list_events():
        # Conserver la référence pour ne pas perdre l'objet
        list_events_window = ListEventsWindow()
        main_window.list_events_window = list_events_window
        list_events_window.show()

    # Connecter le menu "Réservations" à l'ouverture de NewEventForm
    ui.actionClient.triggered.connect(open_new_client_form)
    ui.actionEvent.triggered.connect(open_new_event_form)
    ui.actionLogement.triggered.connect(open_new_logements_form)
    ui.actionLogementListe.triggered.connect(open_list_logements)
    ui.actionClientListe.triggered.connect(open_list_clients)
    ui.actionEventListe.triggered.connect(open_list_events)

    # Connecter le menu "Quitter" à la méthode handle_quit
    ui.actionQuitter.triggered.connect(handle_quit)

    # Afficher la fenêtre principale
    main_window.show()

    # Exécuter la boucle de l'application Qt
    sys.exit(app.exec())

if __name__ == "__main__":
    main()