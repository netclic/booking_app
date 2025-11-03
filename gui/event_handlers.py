from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlQuery

def handle_add_client(ui):
    """Insère un client basé sur les données fournies dans l'interface utilisateur."""
    nom = ui.spinBox.text()
    email = ui.comboBox.currentText()

    if not nom or not email:
        QMessageBox.warning(None, "Erreur", "Entrez un nom et un email valides.")
        return

    query = QSqlQuery()
    query.prepare("INSERT INTO clients (nom, email) VALUES (:nom, :email)")
    query.bindValue(":nom", nom)
    query.bindValue(":email", email)

    if not query.exec():
        QMessageBox.critical(None, "Erreur", f"Échec de l'ajout : {query.lastError().text()}")
    else:
        QMessageBox.information(None, "Succès", "Client ajouté avec succès.")