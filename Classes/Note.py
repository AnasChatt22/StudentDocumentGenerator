class Note:
    def __init__(self, etudiant, matiere, note):
        self.etudiant = etudiant
        self.matiere = matiere
        self.note = note

    def __str__(self):
        return f'{self}'