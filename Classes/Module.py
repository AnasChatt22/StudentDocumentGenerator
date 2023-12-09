import Matiere
class Module:
    def __init__(self, id_module, designation, responsable, semestre):
        self.id_module = id_module
        self.designation = designation
        self.responsable = responsable
        self.semestre = semestre
        self.matieres = []

    def __str__(self):
        return str(self.__dict__)


