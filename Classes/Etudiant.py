from enum import Enum


class SEXE(Enum):
    HOMME = "Homme"
    FEMME = "Femme"


class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, email, sexe, date_naissance):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.sexe = sexe
        self.date_naissance = date_naissance

    def __str__(self):
        return f"{self.id_etudiant}"
