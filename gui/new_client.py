from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QMessageBox
from gui.new_client_ui import Ui_NewClientForm
from db.models.clients import Client


class NewClientForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewClientForm()
        self.ui.setupUi(self)

        # Centrer la fenêtre sur l'écran
        self.center_on_screen()

        # Connecter les boutons
        self.ui.button_save.clicked.connect(self.save_client)
        self.ui.button_cancel.clicked.connect(self.close)

    def center_on_screen(self):
        """Centrer la fenêtre sur l'écran."""
        screen = QGuiApplication.primaryScreen().geometry()
        window_size = self.frameGeometry()
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        self.move(x, y)

    def save_client(self):
        """Récupérer les données du formulaire et sauvegarder un nouveau client."""
        # Récupérer les valeurs du formulaire
        nom = self.ui.input_nom.text()
        prenom = self.ui.input_prenom.text()
        email = self.ui.input_email.text()
        telephone = self.ui.input_telephone.text()
        adresse = self.ui.input_adresse.toPlainText()
        code_postal = self.ui.input_code_postal.text()
        ville = self.ui.input_ville.text()
        adresse_complement = self.ui.input_adresse_complement.toPlainText()

        # Validation des champs obligatoires
        if not nom or not email:
            QMessageBox.warning(self, "Erreur", "Les champs Nom et Email sont obligatoires.")
            return

        # Validation des champs numériques
        if code_postal and not code_postal.isdigit():
            QMessageBox.warning(self, "Erreur", "Le champ Code Postal doit être un nombre valide.")
            return

        # Créer et sauvegarder un objet Client
        client = Client(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            adresse=adresse,
            code_postal=int(code_postal) if code_postal else None,
            ville=ville,
            adresse_complement=adresse_complement
        )

        if client.save():
            QMessageBox.information(self, "Succès", "Le client a été enregistré avec succès.")
            self.close()
        else:
            QMessageBox.critical(self, "Erreur", "Impossible d'enregistrer le client.")