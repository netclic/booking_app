from db.db_connection import connect_to_db
from PySide6.QtSql import QSqlQuery, QSqlError


class Event:
    """Représente un événement dans la base de données."""

    def __init__(
        self,
        id=None, client_id=None, logement_id=None, status=None, date_debut=None,
        date_fin=None, description=None, nombre_adultes=0, nombre_enfants=0, type=None
    ):
        self.id = id
        self.client_id = client_id
        self.logement_id = logement_id
        self.status = status
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
        self.nombre_adultes = nombre_adultes
        self.nombre_enfants = nombre_enfants
        self.type = type

    @staticmethod
    def load_all():
        """Charge tous les événements depuis la base de données dans une liste d'objets `Event`."""
        events = []
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            if query.exec("""
                SELECT id, client_id, logement_id, status, date_debut,
                       date_fin, description, nombre_adultes, nombre_enfants, type
                FROM events
            """):
                while query.next():
                    events.append(
                        Event(
                            id=query.value(0),
                            client_id=query.value(1),
                            logement_id=query.value(2),
                            status=query.value(3),
                            date_debut=query.value(4),
                            date_fin=query.value(5),
                            description=query.value(6),
                            nombre_adultes=query.value(7),
                            nombre_enfants=query.value(8),
                            type=query.value(9),
                        )
                    )
            else:
                print("Erreur lors de l'exécution de la requête load_all : ", query.lastError().text())
        else:
            print("Erreur : Base de données non ouverte dans Event.load_all().")
        return events

    @staticmethod
    def get_by_id(event_id):
        """Charge un événement spécifique en fonction de son ID."""
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            query.prepare("""
                SELECT id, client_id, logement_id, status, date_debut, 
                       date_fin, description, nombre_adultes, nombre_enfants, type
                FROM events
                WHERE id = :id
            """)
            query.bindValue(":id", event_id)
            if query.exec() and query.next():
                return Event(
                    id=query.value(0),
                    client_id=query.value(1),
                    logement_id=query.value(2),
                    status=query.value(3),
                    date_debut=query.value(4),
                    date_fin=query.value(5),
                    description=query.value(6),
                    nombre_adultes=query.value(7),
                    nombre_enfants=query.value(8),
                    type=query.value(9),
                )
            else:
                print(f"Aucun événement trouvé pour ID={event_id} ou erreur : {query.lastError().text()}")
        else:
            print("Erreur : Base de données non ouverte dans Event.get_by_id().")
        return None

    def save(self):
        """Enregistre ou met à jour un événement dans la base de données."""
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            if self.id:  # Mise à jour
                query.prepare("""
                    UPDATE events
                    SET client_id = :client_id, logement_id = :logement_id,
                        status = :status, date_debut = :date_debut, date_fin = :date_fin,
                        description = :description, nombre_adultes = :nombre_adultes,
                        nombre_enfants = :nombre_enfants, type = :type
                    WHERE id = :id
                """)
                query.bindValue(":id", self.id)
            else:  # Création
                query.prepare("""
                    INSERT INTO events (client_id, logement_id, status, date_debut, date_fin,
                                        description, nombre_adultes, nombre_enfants, type)
                    VALUES (:client_id, :logement_id, :status, :date_debut, :date_fin,
                            :description, :nombre_adultes, :nombre_enfants, :type)
                """)
            # Liaison des champs communs
            query.bindValue(":client_id", self.client_id)
            query.bindValue(":logement_id", self.logement_id)
            query.bindValue(":status", self.status)
            query.bindValue(":date_debut", self.date_debut)
            query.bindValue(":date_fin", self.date_fin)
            query.bindValue(":description", self.description)
            query.bindValue(":nombre_adultes", self.nombre_adultes)
            query.bindValue(":nombre_enfants", self.nombre_enfants)
            query.bindValue(":type", self.type)

            if query.exec():
                print("Événement enregistré avec succès.")
                if not self.id:
                    self.id = query.lastInsertId()
                return True
            else:
                print("Erreur lors de l'enregistrement de l'événement :", query.lastError().text())
        else:
            print("Erreur : Base de données non ouverte dans Event.save().")
        return False

    def delete(self):
        """Supprime un événement de la base de données."""
        db = connect_to_db()
        if db.isOpen() and self.id:
            query = QSqlQuery(db)
            query.prepare("DELETE FROM events WHERE id = :id")
            query.bindValue(":id", self.id)
            if query.exec():
                print(f"Événement ID={self.id} supprimé avec succès.")
                return True
            else:
                print("Erreur lors de la suppression :", query.lastError().text())
        else:
            print(f"Erreur : Base de données non ouverte ou ID non défini dans Event.delete().")
        return False