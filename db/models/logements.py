from db.db_connection import connect_to_db
from PySide6.QtSql import QSqlQuery, QSqlError


class Logement:
    """Représente un logement tel qu'enregistré dans la base de données."""

    def __init__(self, id=None, nom=None, adresse=None, code_postal=None, ville=None, capacite=None, classement=None):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.capacite = capacite
        self.classement = classement

    @staticmethod
    def load_all():
        """Charge tous les logements depuis la base dans une liste d'objets `Logement`."""
        logements = []
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            if query.exec("SELECT id, nom, adresse, code_postal, ville, capacite, classement FROM logements"):
                while query.next():
                    logements.append(
                        Logement(
                            id=query.value(0),
                            nom=query.value(1),
                            adresse=query.value(2),
                            code_postal=query.value(3),
                            ville=query.value(4),
                            capacite=query.value(5),
                            classement=query.value(6),
                        )
                    )
            else:
                print("Erreur lors de l'exécution de la requête load_all : ", query.lastError().text())
        else:
            print("Erreur : Base de données non ouverte dans Logement.load_all().")
        return logements

    @staticmethod
    def get_by_id(logement_id):
        """Charge un logement spécifique depuis la base via son ID."""
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            query.prepare("SELECT id, nom, adresse, code_postal, ville, capacite, classement FROM logements WHERE id = :id")
            query.bindValue(":id", logement_id)
            if query.exec() and query.next():
                return Logement(
                    id=query.value(0),
                    nom=query.value(1),
                    adresse=query.value(2),
                    code_postal=query.value(3),
                    ville=query.value(4),
                    capacite=query.value(5),
                    classement=query.value(6),
                )
            else:
                print(f"Aucun logement trouvé pour ID={logement_id} ou erreur : {query.lastError().text()}")
        else:
            print("Erreur : Base de données non ouverte dans Logement.get_by_id().")
        return None

    def save(self):
        """Enregistre ou met à jour un logement dans la base de données."""
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            if self.id:  # Mise à jour
                query.prepare("""
                    UPDATE logements
                    SET nom = :nom, adresse = :adresse, code_postal = :code_postal, ville = :ville,
                        capacite = :capacite, classement = :classement
                    WHERE id = :id
                """)
                query.bindValue(":id", self.id)
            else:  # Création
                query.prepare("""
                    INSERT INTO logements (nom, adresse, code_postal, ville, capacite, classement)
                    VALUES (:nom, :adresse, :code_postal, :ville, :capacite, :classement)
                """)
            # Champs communs dans les deux cas
            query.bindValue(":nom", self.nom)
            query.bindValue(":adresse", self.adresse)
            query.bindValue(":code_postal", self.code_postal)
            query.bindValue(":ville", self.ville)
            query.bindValue(":capacite", self.capacite)
            query.bindValue(":classement", self.classement)
            if query.exec():
                print("Logement enregistré avec succès.")
                if not self.id:
                    self.id = query.lastInsertId()
                return True
            else:
                print("Erreur lors de l'enregistrement du logement :", query.lastError().text())
        else:
            print("Erreur : Base de données non ouverte dans Logement.save().")
        return False

    def delete(self):
        """Supprime un logement de la base de données."""
        db = connect_to_db()
        if db.isOpen() and self.id:
            query = QSqlQuery(db)
            query.prepare("DELETE FROM logements WHERE id = :id")
            query.bindValue(":id", self.id)
            if query.exec():
                print(f"Logement ID={self.id} supprimé avec succès.")
                return True
            else:
                print("Erreur lors de la suppression :", query.lastError().text())
        else:
            print(f"Erreur : Base de données non ouverte ou suivi ID non défini dans Logement.delete().")
        return False