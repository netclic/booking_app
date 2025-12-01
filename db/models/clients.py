import json

from db.db_connection import connect_to_db
from PySide6.QtSql import QSqlQuery, QSqlError


class Client:
    """Représente un client tel qu'enregistré dans la base de données."""

    def __init__(self, id=None, nom=None, email=None, telephone=None, prenom=None, adresse=None, code_postal=None, ville=None, adresse_complement=None):
        self.id = id
        self.nom = nom
        self.email = email
        self.telephone = telephone
        self.prenom = prenom
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.adresse_complement = adresse_complement


    @staticmethod
    def delete(self, client_id):
        """Supprime un client de la base de données."""
        db = connect_to_db()
        if db.isOpen() and isinstance(client_id, int):
            query = QSqlQuery(db)
            query.prepare("DELETE FROM clients WHERE id = :id")
            query.bindValue(":id", client_id)
            if query.exec():
                print(f"Client ID={client_id} supprimé avec succès.")
                return True
            else:
                print("Erreur lors de la suppression :", query.lastError().text())
        else:
            print(f"Erreur : Base de données non ouverte ou suivi ID non défini dans Client.delete().")
        return False


    @staticmethod
    def get_by_id(client_id):
        """Charge un client spécifique depuis la base via son ID."""
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            query.prepare("""
                SELECT id, nom, email, telephone, prenom, adresse, code_postal, ville, adresse_complement 
                FROM clients 
                WHERE id = :id
            """)
            query.bindValue(":id", client_id)
            if query.exec() and query.next():
                return Client(
                    id=query.value(0),
                    nom=query.value(1),
                    email=query.value(2),
                    telephone=query.value(3),
                    prenom=query.value(4),
                    adresse=query.value(5),
                    code_postal=query.value(6),
                    ville=query.value(7),
                    adresse_complement=query.value(8),
                )
            else:
                print(f"Aucun client trouvé pour ID={client_id} ou erreur : {query.lastError().text()}")
        else:
            print("Erreur : Base de données non ouverte dans Client.get_by_id().")
        return None


    @staticmethod
    def load_all():
        """Charge tous les clients depuis la base dans une liste d'objets `Client`."""
        clients = []
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            if query.exec("""
                SELECT id, nom, email, telephone, prenom, adresse, code_postal, ville, adresse_complement 
                FROM clients
            """):
                while query.next():
                    clients.append(
                        Client(
                            id=query.value(0),
                            nom=query.value(1),
                            email=query.value(2),
                            telephone=query.value(3),
                            prenom=query.value(4),
                            adresse=query.value(5),
                            code_postal=query.value(6),
                            ville=query.value(7),
                            adresse_complement=query.value(8),
                        )
                    )
            else:
                print("Erreur lors de l'exécution de la requête load_all : ", query.lastError().text())
        else:
            print("Erreur : Base de données non ouverte dans Client.load_all().")
        return clients


    def save(self):
        """Enregistre ou met à jour un client dans la base de données."""
        db = connect_to_db()
        if db.isOpen():
            query = QSqlQuery(db)
            if self.id:  # Mise à jour
                query.prepare("""
                    UPDATE clients
                    SET nom = :nom, email = :email, telephone = :telephone, prenom = :prenom,
                        adresse = :adresse, code_postal = :code_postal, ville = :ville, adresse_complement = :adresse_complement
                    WHERE id = :id
                """)
                query.bindValue(":id", self.id)
            else:  # Création
                query.prepare("""
                    INSERT INTO clients (nom, email, telephone, prenom, adresse, code_postal, ville, adresse_complement)
                    VALUES (:nom, :email, :telephone, :prenom, :adresse, :code_postal, :ville, :adresse_complement)
                """)
            # Liaison des valeurs communes pour création ou mise à jour
            query.bindValue(":nom", self.nom)
            query.bindValue(":email", self.email)
            query.bindValue(":telephone", self.telephone)
            query.bindValue(":prenom", self.prenom)
            query.bindValue(":adresse", self.adresse)
            query.bindValue(":code_postal", self.code_postal)
            query.bindValue(":ville", self.ville)
            query.bindValue(":adresse_complement", self.adresse_complement)

            if query.exec():
                print("Client enregistré avec succès.")
                if not self.id:
                    self.id = query.lastInsertId()
                return True
            else:
                print("Erreur lors de l'enregistrement du client :", query.lastError().text())
        else:
            print("Erreur : Base de données non ouverte dans Client.save().")
        return False


    def to_dict(self):
        """Retourne un dictionnaire représentant l'objet Client."""
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "telephone": self.telephone,
            "adresse": self.adresse,
            "code_postal": self.code_postal,
            "ville": self.ville,
            "adresse_complement": self.adresse_complement,
            # Exclure adresse_complement pour l'exemple
        }


    def to_json(self):
        """Retourne un enregistrement JSON représentant l'objet Client."""
        client_dict = self.to_dict()
        return json.dumps(client_dict)