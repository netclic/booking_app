from PySide6.QtWidgets import QWidget, QMessageBox
from gui.new_logement_ui import Ui_NewLogementForm
from db.models.logements import Logement


class NewLogementForm(QWidget):  # Base modifiée à QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewLogementForm()
        self.ui.setupUi(self)

        # Connecter les boutons aux actions
        self.ui.button_save.clicked.connect(self.save_logement)
        self.ui.button_cancel.clicked.connect(self.close)

    def save_logement(self):
        # Récupérer les valeurs du formulaire
        nom = self.ui.input_nom.text()
        adresse = self.ui.input_adresse.text()
        code_postal = self.ui.input_code_postal.text()
        ville = self.ui.input_ville.text()
        capacite = self.ui.input_capacite.value()
        classement = self.ui.input_classement.text()

        # Vérifier que les champs nécessaires sont renseignés
        if not nom or not adresse or not code_postal or not ville or not classement:
            QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        # Créer et enregistrer un nouvel objet Logement
        logement = Logement(
            nom=nom,
            adresse=adresse,
            code_postal=code_postal,
            ville=ville,
            capacite=capacite,
            classement=classement,
        )
        if logement.save():
            QMessageBox.information(self, "Succès", "Le logement a été enregistré avec succès.")
            self.close()
        else:
            QMessageBox.critical(self, "Erreur", "Impossible d'enregistrer le logement.")