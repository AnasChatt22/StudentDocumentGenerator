import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom
from Classes.Etudiant import Etudiant
from Classes.Matiere import Matiere
from Classes.Module import Module
from Classes.Note import Note
from datetime import datetime



class CreateXML:
    def __init__(self, etudiant_xl_path, modules_xl_path, notes_xl_path, xml_path):
        self.etudiants_xl_path = etudiant_xl_path
        self.modules_xl_path = modules_xl_path
        self.notes_xl_path = notes_xl_path
        self.xml_path = xml_path
        self.etudiants = []
        self.modules = []
        self.notes = []

    def ajout_etudiants(self):
        read_xl = pd.read_excel(self.etudiants_xl_path)
        for _, row in read_xl.iterrows():
            date_naissance = pd.to_datetime(row['date_naissance'])

            etudiant = Etudiant(row['id_etudiant'], row['nom'], row['prenom'], row['email'], row['sexe'],
                                date_naissance)
            self.etudiants.append(etudiant)

    def ajout_modules(self):
        read_xl = pd.read_excel(self.modules_xl_path)
        for _, row in read_xl.iterrows():
            module = Module(row['id_module'], row['designation_module'], row['responsable'], row['semestre'])
            self.modules.append(module)

            for i in range(1, 4):
                matiere_id = row[f'id_matiere_{i}']
                designation = row[f'designation_matiere_{i}']
                if not pd.isna(designation):
                    matiere = Matiere(matiere_id, designation)
                    module.matieres.append(matiere)

    def ajout_notes(self):
        for module in self.modules:
            # Récupérer les données de chaque feuille
            sheet = pd.read_excel(self.notes_xl_path, sheet_name=str(module.id_module))

            for _, row in sheet.iterrows():
                id_etudiant = row['id_etudiant']
                id_matiere = row['id_matiere']
                note_value = row['note']

                # Rechercher l'étudiant correspondant
                etudiant = next((etudiant for etudiant in self.etudiants if etudiant.id_etudiant == id_etudiant), None)

                # Rechercher la matière correspondante dans les matières du module actuel
                matiere = next((matiere for matiere in module.matieres if matiere.id_matiere == id_matiere), None)

                if etudiant is not None and matiere is not None:
                    # Créer une instance de la classe Note et l'ajouter à la liste
                    note = Note(etudiant, matiere, note_value)
                    self.notes.append(note)

    def Creer_xml(self):
        xml_doc = ET.Element("Etudiants")

        for etudiant in self.etudiants:
            etudiant_element = ET.SubElement(xml_doc, "Etudiant", idetudiant=str(etudiant.id_etudiant),
                                             sexe=str(etudiant.sexe),
                                             date_naissance=str(etudiant.date_naissance.strftime("%Y-%m-%d")))

            ET.SubElement(etudiant_element, "Nom").text = etudiant.nom
            ET.SubElement(etudiant_element, "Prenom").text = etudiant.prenom
            ET.SubElement(etudiant_element, "Email").text = etudiant.email

            for module in self.modules:
                module_element = ET.SubElement(etudiant_element, "Module", id_module=str(module.id_module))
                ET.SubElement(module_element, "Designation").text = module.designation
                ET.SubElement(module_element, "Responsable").text = module.responsable
                ET.SubElement(module_element, "Semestre").text = str(module.semestre)

                for matiere in module.matieres:
                    matiere_element = ET.SubElement(module_element, "Matiere", id_matiere=str(matiere.id_matiere))
                    ET.SubElement(matiere_element, "Designation").text = matiere.designation

                    for note in self.notes:
                        if note.etudiant.id_etudiant == etudiant.id_etudiant and note.matiere.id_matiere == matiere.id_matiere:
                            ET.SubElement(matiere_element, "Note").text = str(note.note)

        xml_string = ET.tostring(xml_doc, encoding="UTF-8")
        dom = xml.dom.minidom.parseString(xml_string)
        prettified_xml = dom.toprettyxml(indent="    ")  # we can adjust the number of spaces for indentation

        # Write the prettified XML to the file
        with open(self.xml_path, "w", encoding="UTF-8") as xml_file:
            xml_file.write(prettified_xml)


if __name__ == "__main__":
    etudiant_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\Fichiers Excel\\Etudiants.xlsx"
    modules_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\Fichiers Excel\\Modules.xlsx"
    notes_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\Fichiers Excel\\Notes.xlsx"
    xml_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\Fichiers XML\\GINF2.xml"

    xml_file = CreateXML(etudiant_xl_path, modules_xl_path, notes_xl_path, xml_path)

    xml_file.ajout_etudiants()
    xml_file.ajout_modules()
    xml_file.ajout_notes()
    xml_file.Creer_xml()
