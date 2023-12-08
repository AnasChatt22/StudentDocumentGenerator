from enum import Enum


class SEXE(Enum):
    HOMME = "HOMME"
    FEMME = "FEMME"


class Etudiant:
    def __init__(self, id_etud, nom, prenom, email, sexe, date_naissance):
        self.id_etud = id_etud
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.sexe = sexe
        self.date_naissance = date_naissance
