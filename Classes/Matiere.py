class Matiere:
    def __init__(self, id_matiere, designation):
        self.id_matiere = id_matiere
        self.designation = designation

    def __str__(self):
        return str(self.__dict__)
