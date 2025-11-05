from db.db_connection import connect_to_db


def setup_db():
    """Créer les tables nécessaires dans la base SQLite."""
    db = connect_to_db()  # Connexion à la base de données
    if db.isOpen():
        query = db.exec()  # Création d'une instance QSqlQuery

        if not query:
            print("Erreur : Impossible d'initialiser la requête.")
            return

        # Création de la table clients
        if not query.exec("""
                          CREATE TABLE IF NOT EXISTS clients
                          (
                              id                 INTEGER PRIMARY KEY AUTOINCREMENT,
                              nom                TEXT        NOT NULL,
                              email              TEXT UNIQUE NOT NULL,
                              telephone          TEXT,
                              prenom             TEXT,
                              adresse            TEXT,
                              code_postal        INTEGER,
                              ville              TEXT,
                              adresse_complement TEXT
                          )
                          """):
            print("Erreur lors de la création de la table clients : ", query.lastError().text())
            return

        # Création de la table logements
        if not query.exec("""
                          CREATE TABLE IF NOT EXISTS logements
                          (
                              id          INTEGER PRIMARY KEY AUTOINCREMENT,
                              nom         TEXT,
                              adresse     TEXT,
                              code_postal TEXT,
                              ville       TEXT,
                              capacite    INTEGER,
                              classement  INTEGER
                          )
                          """):
            print("Erreur lors de la création de la table logements : ", query.lastError().text())
            return

        # Création de la table events
        if not query.exec("""
                          CREATE TABLE IF NOT EXISTS events
                          (
                              id             INTEGER PRIMARY KEY AUTOINCREMENT,
                              client_id      INTEGER NOT NULL REFERENCES clients (id) ON DELETE CASCADE,
                              logement_id    INTEGER NOT NULL REFERENCES logements (id) ON DELETE CASCADE,
                              status         TEXT,
                              date_debut     TEXT    NOT NULL,
                              date_fin       TEXT,
                              description    TEXT,
                              nombre_adultes INTEGER,
                              nombre_enfants INTEGER,
                              type           TEXT,
                              CONSTRAINT check_status CHECK (status IN ('Demande', 'En attente', 'Confirmée', 'Annulée')),
                              CONSTRAINT check_type CHECK (type IN ('Fermeture', 'Réservation'))
                          )
                          """):
            print("Erreur lors de la création de la table events : ", query.lastError().text())
            return

        # Création des index pour la table events
        if not query.exec("CREATE INDEX IF NOT EXISTS idx_events_client ON events (client_id)"):
            print("Erreur lors de la création de l'index idx_events_client : ", query.lastError().text())
            return

        if not query.exec("CREATE INDEX IF NOT EXISTS idx_events_logement ON events (logement_id)"):
            print("Erreur lors de la création de l'index idx_events_logement : ", query.lastError().text())
            return

        # Création de la table politique_tarif
        if not query.exec("""
                          CREATE TABLE IF NOT EXISTS politique_tarif
                          (
                              id INTEGER PRIMARY KEY AUTOINCREMENT
                          )
                          """):
            print("Erreur lors de la création de la table politique_tarif : ", query.lastError().text())
            return

        # Confirmation de la création des tables
        print("Les tables ont été créées ou existent déjà.")
    else:
        print("Erreur : Impossible d'ouvrir la base de données.")


if __name__ == "__main__":
    setup_db()