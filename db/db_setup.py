from db.db_connection import connect_to_db

def setup_db():
    """Créer les tables nécessaires dans la base SQLite."""
    db = connect_to_db()
    if db.isOpen():
        query = db.exec()  # Utilisation d'un QSqlQuery

        # Table clients
        query.exec("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                telephone TEXT
            )
        """)

        # Table réservations
        query.exec("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                date_reservation TEXT NOT NULL,
                status TEXT DEFAULT 'PENDING',
                FOREIGN KEY(client_id) REFERENCES clients(id)
            )
        """)

        print("Les tables ont été créées ou existent déjà.")

if __name__ == "__main__":
    setup_db()