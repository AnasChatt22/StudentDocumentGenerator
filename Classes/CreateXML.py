import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom
from Classes.Etudiant import Etudiant
from Classes.Matiere import Matiere
from Classes.Module import Module
from Classes.Note import Note
import ValidateXML


class CreateXML:
    def __init__(self, Excel_Path_Etudiants, Excel_Path_Modules, Excel_Path_Notes, Excel_Path_Emploi, XML_Path_GINF2,
                 XML_Path_Emploi):
        self.etudiants_xl_path = Excel_Path_Etudiants
        self.modules_xl_path = Excel_Path_Modules
        self.notes_xl_path = Excel_Path_Notes
        self.emploi_xl_path = Excel_Path_Emploi
        self.xml_path_GINF2 = XML_Path_GINF2
        self.xml_path_Emploi = XML_Path_Emploi
        self.etudiants = []
        self.modules = []
        self.notes = []

    def ajout_etudiants(self):
        try:
            read_xl = pd.read_excel(self.etudiants_xl_path)
            for _, row in read_xl.iterrows():
                date_naissance = pd.to_datetime(row['date_naissance'])
                etudiant = Etudiant(row['id_etudiant'], row['nom'], row['prenom'], row['email'], row['sexe'],
                                    date_naissance)
                self.etudiants.append(etudiant)
        except Exception as ex:
            print(f"Erreur d'ajout des étudiants: {ex}")

    def ajout_modules(self):
        try:
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
        except Exception as ex:
            print(f"Erreur d'ajout des modules: {ex}")

    def ajout_notes(self):
        try:
            for module in self.modules:
                sheet = pd.read_excel(self.notes_xl_path, sheet_name=str(module.id_module))

                for _, row in sheet.iterrows():
                    id_etudiant = row['id_etudiant']
                    id_matiere = row['id_matiere']
                    note_value = row['note']

                    etudiant = next((etudiant for etudiant in self.etudiants if etudiant.id_etudiant == id_etudiant),
                                    None)
                    matiere = next((matiere for matiere in module.matieres if matiere.id_matiere == id_matiere), None)

                    if etudiant is not None and matiere is not None:
                        note = Note(etudiant, matiere, note_value)
                        self.notes.append(note)
        except Exception as ex:
            print(f"Erreur d'ajout des notes: {ex}")

    def Creer_xml_GINF2(self):
        try:
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

            # Format xml file
            xml_string = ET.tostring(xml_doc, encoding="UTF-8")
            dom = xml.dom.minidom.parseString(xml_string)
            prettified_xml = dom.toprettyxml(indent="    ")

            # Create XML File
            with open(self.xml_path_GINF2, "w", encoding="UTF-8") as generatedXML:
                generatedXML.write(prettified_xml)
            print("Fichier GINF2.xml créé avec succés")
        except Exception as ex:
            print(f"Erreur de création du fichier GINF2.xml: {ex}")

    def Creer_xml_Emploi(self):
        try:
            xml_doc = ET.Element("Mi-semestres", )

            for i in range(1, 5):
                sheet = pd.read_excel(self.emploi_xl_path, sheet_name="mi_semestre" + str(i))
                mi_semestre_element = ET.SubElement(xml_doc, "Mi_semestre", numero=str(i))

                semaines = set()
                jours = set()
                cp = 0

                for _, row in sheet.iterrows():
                    semaine = row['semaine']
                    jour = row['jour']
                    horaire = row['horaire']
                    salle = "" if pd.isna(row['salle']) else row['salle']
                    id_matiere = row['id_matiere']
                    if pd.isna(id_matiere):
                        designation = ""
                    else:
                        for module in self.modules:
                            for matiere in module.matieres:
                                if matiere.id_matiere == id_matiere:
                                    designation = matiere.designation
                                    break
                    professeur = "" if pd.isna(row['professeur']) else row['professeur']
                    seance_type = row['type']
                    if pd.isna(seance_type):
                        seance_type = ""

                    if semaine not in semaines:
                        semaine_element = ET.SubElement(mi_semestre_element, "Semaine", numero=str(semaine))
                        semaines.add(semaine)
                    if jour == "Vendredi":
                        cp = cp + 1
                    if jour not in jours:
                        jour_element = ET.SubElement(semaine_element, "Jour", nom=jour)
                        jours.add(jour)

                    seance_element = ET.SubElement(jour_element, "Seance", horaire=horaire, type=seance_type)
                    matiere_element = ET.SubElement(seance_element, "Matière", designation=designation)
                    ET.SubElement(matiere_element, "Professeur").text = professeur
                    ET.SubElement(matiere_element, "Salle").text = salle

                    if cp == 4:
                        cp = 0
                        jours = set()

            # Format xml file
            xml_string = ET.tostring(xml_doc, encoding="UTF-8")
            dom = xml.dom.minidom.parseString(xml_string)
            prettified_xml = dom.toprettyxml(indent="    ")

            # Create XML File
            with open(self.xml_path_Emploi, "w", encoding="UTF-8") as generatedXML:
                generatedXML.write(prettified_xml)
            print("Fichier Emploi.xml du temps créé avec succès")
        except Exception as ex:
            print(f"Erreur de création du fichier Emploi.xml: {ex}")


if __name__ == "__main__":
    # Edit paths before testing
    etudiant_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Etudiants.xlsx"
    modules_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Modules.xlsx"
    notes_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Notes.xlsx"
    emploi_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Emplois.xlsx"
    xml_path_GINF2 = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersXML\\XML\\GINF2.xml"
    xml_path_Emploi = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersXML\\XML\\Emploi.xml"
    dtd_path_GINF2 = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersXML\\DTD\\GINF2.dtd"
    xsd_path_GINF2 = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersXML\\XSD\\GINF2.xsd"

    try:
        xml_file = CreateXML(etudiant_xl_path, modules_xl_path, notes_xl_path, emploi_xl_path, xml_path_GINF2,
                             xml_path_Emploi)
        xml_file.ajout_etudiants()
        xml_file.ajout_modules()
        xml_file.ajout_notes()
        xml_file.Creer_xml_GINF2()
        xml_file.Creer_xml_Emploi()

        ValidateXML.validate_with_dtd(xml_path_GINF2, dtd_path_GINF2)
        ValidateXML.validate_with_xsd(xml_path_GINF2, xsd_path_GINF2)
    except Exception as e:
        print(f"Il y a une erreur: {e}")
