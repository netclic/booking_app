from PySide6.QtSql import QSqlDatabase, QSqlError
import sys

def connect_to_db():
    """Configurer et retourner une connexion SQLite."""
    # Vérifiez si une connexion existe déjà avec ce nom
    connection_name = "default_connection"
    if QSqlDatabase.contains(connection_name):
        return QSqlDatabase.database(connection_name)

    # Créez une nouvelle connexion nommée
    db = QSqlDatabase.addDatabase("QSQLITE", connection_name)
    db.setDatabaseName("booking_app.db")  # Nom de la base de données SQLite

    if not db.open():
        print(f"Erreur de connexion à la base de données : {db.lastError().text()}")
        sys.exit(1)

    print("Connexion réussie à la base de données !")
    return db