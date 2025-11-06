from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QMessageBox  # Remplace QMainWindow par QWidget
from gui.new_event_ui import Ui_NewEventForm
from db.models.events import Event


class NewEventForm(QWidget):  # Change la classe de base à QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewEventForm()

        # Configure l'UI définie via le fichier .ui
        self.ui.setupUi(self)

        # Centrer la fenêtre sur l'écran
        self.center_on_screen()

        # Connecter les boutons aux actions
        self.ui.button_save.clicked.connect(self.save_event)
        self.ui.button_cancel.clicked.connect(self.close)

        # Charger les clients et logements dans les ComboBox
        self.load_clients()
        self.load_logements()

    def load_clients(self):
        """Charge les clients dans la liste déroulante (ComboBox)."""
        from db.models.clients import Client  # Importation locale pour éviter les dépendances croisées
        clients = Client.load_all()
        for client in clients:
            self.ui.comboBox_client.addItem(f"{client.id}: {client.nom}", client.id)

    def load_logements(self):
        """Charge les logements dans la liste déroulante (ComboBox)."""
        from db.models.logements import Logement  # Importation locale pour éviter les dépendances croisées
        logements = Logement.load_all()
        for logement in logements:
            self.ui.comboBox_logement.addItem(f"{logement.id}: {logement.nom}", logement.id)

    def center_on_screen(self):
        """Centrer la fenêtre sur l'écran."""
        screen = QGuiApplication.primaryScreen().geometry()
        window_size = self.frameGeometry()
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        self.move(x, y)

    def save_event(self):
        """Sauvegarde un nouvel événement en fonction des données saisies."""
        # Récupérer les valeurs des champs
        client_id = self.ui.comboBox_client.currentData()
        logement_id = self.ui.comboBox_logement.currentData()
        status = self.ui.comboBox_statut.currentText()
        date_debut = self.ui.dateEdit_debut.date().toString("yyyy-MM-dd")
        date_fin = self.ui.dateEdit_fin.date().toString("yyyy-MM-dd")
        description = self.ui.textEdit_description.toPlainText()
        nombre_adultes = self.ui.spinBox_adultes.value()
        nombre_enfants = self.ui.spinBox_enfants.value()
        type_event = self.ui.comboBox_type.currentText()

        # Validation des champs obligatoires
        if not client_id or not logement_id or not date_debut:
            QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        # Créer et enregistrer un nouvel objet Event
        event = Event(
            client_id=client_id,
            logement_id=logement_id,
            status=status,
            date_debut=date_debut,
            date_fin=date_fin,
            description=description,
            nombre_adultes=nombre_adultes,
            nombre_enfants=nombre_enfants,
            type=type_event,
        )
        if event.save():
            QMessageBox.information(self, "Succès", "L'évènement a été enregistré avec succès.")
            self.close()
        else:
            QMessageBox.critical(self, "Erreur", "Impossible d'enregistrer l'évènement.")