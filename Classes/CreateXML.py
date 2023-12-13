import random
import traceback
import xml.dom.minidom
import xml.etree.ElementTree as ET

import pandas as pd


def Creer_xml_GINF2(Excel_Path_Etudiants, Excel_Path_Modules, XML_Path_GINF2):
    try:
        # Read Excel files
        read_xl_etudiant = pd.read_excel(Excel_Path_Etudiants)
        read_xl_module = pd.read_excel(Excel_Path_Modules)

        # Root element for the XML document
        xml_doc = ET.Element("Etudiants")

        # Iterate over each row in the Etudiants Excel file
        for _, row_etd in read_xl_etudiant.iterrows():
            # Convert the date of birth to a datetime object
            date_naissance = pd.to_datetime(row_etd['date_naissance'])

            # Create an Etudiant element with attributes
            etudiant_element = ET.SubElement(xml_doc, "Etudiant", id_etudiant=str(row_etd['id_etudiant']),
                                             sexe=str(row_etd['sexe']),
                                             date_naissance=str(date_naissance.strftime("%Y-%m-%d")))

            # Add sub-elements for Nom, Prenom, and Email under Etudiant
            ET.SubElement(etudiant_element, "Nom").text = row_etd['nom']
            ET.SubElement(etudiant_element, "Prenom").text = row_etd['prenom']
            ET.SubElement(etudiant_element, "Email").text = row_etd['email']

            # Iterate over each row in the Modules Excel file
            for _, row_module in read_xl_module.iterrows():
                # Create a Module element with attributes
                module_element = ET.SubElement(etudiant_element, "Module", id_module=str(row_module['id_module']))
                ET.SubElement(module_element, "Designation").text = row_module['designation_module']
                ET.SubElement(module_element, "Responsable").text = row_module['responsable']
                ET.SubElement(module_element, "Semestre").text = str(row_module['semestre'])

                # Iterate over three potential Matieres
                for i in range(1, 4):
                    # Check if the id_matiere_i column is not empty
                    if pd.notna(row_module[f'id_matiere_{i}']):
                        # Create a Matiere element with attributes
                        matiere_element = ET.SubElement(module_element, "Matiere",
                                                        id_matiere=str(row_module[f'id_matiere_{i}']))
                        ET.SubElement(matiere_element, "Designation").text = row_module[f'designation_matiere_{i}']

                        # Generate a random Note for Matiere
                        ET.SubElement(matiere_element, "Note").text = str(round(random.uniform(2.0, 20.0)))

        # Format XML file
        xml_string = ET.tostring(xml_doc, encoding="UTF-8")
        dom = xml.dom.minidom.parseString(xml_string)
        prettified_xml = dom.toprettyxml(indent="    ")

        # Create XML File
        with open(XML_Path_GINF2, "w", encoding="UTF-8") as generatedXML:
            generatedXML.write(prettified_xml)

        print("Fichier GINF2.xml créé avec succès")
    except Exception as ex:
        traceback_str = traceback.format_exc()
        print(f"Erreur de création du fichier GINF2.xml: {ex}\n{traceback_str}")


def Creer_xml_Emploi(Excel_Path_Emplois, Excel_Path_Modules, XML_Path_Emploi):
    global semaine_element, jour_element, designation
    try:
        read_xl_emplois = pd.ExcelFile(Excel_Path_Emplois)
        read_xl_module = pd.read_excel(Excel_Path_Modules)

        xml_doc = ET.Element("Mi-semestres")
        j = 0

        for sheet in read_xl_emplois.sheet_names:
            j += 1
            mi_semestre_element = ET.SubElement(xml_doc, "Mi_semestre", numero=str(j))
            sheet_data = pd.read_excel(read_xl_emplois, sheet)

            for _, row in sheet_data.iterrows():
                salle = "" if pd.isna(row['salle']) else row['salle']
                professeur = "" if pd.isna(row['professeur']) else row['professeur']
                seance_type = "" if pd.isna(row['type']) else row['type']

                if pd.isna(row['id_matiere']):
                    designation = ""
                else:
                    for _, row_module in read_xl_module.iterrows():
                        for i in range(1, 4):
                            if pd.notna(row_module[f'id_matiere_{i}']):
                                if row_module[f'id_matiere_{i}'] == row['id_matiere']:
                                    designation = row_module[f'designation_matiere_{i}']
                                    break

                if not pd.isna(row['premiere_semaine']):
                    semaine_element = ET.SubElement(mi_semestre_element, "Semaine",
                                                    Premiere=str(int(row['premiere_semaine'])),
                                                    Derniere=str(int(row['derniere_semaine'])))

                if not pd.isna(row['jour']):
                    jour_element = ET.SubElement(semaine_element, "Jour", nom=row['jour'])

                seance_element = ET.SubElement(jour_element, "Seance", horaire=row['horaire'], type=seance_type)
                matiere_element = ET.SubElement(seance_element, "Matière")
                ET.SubElement(matiere_element, "Designation").text = designation
                ET.SubElement(matiere_element, "Professeur").text = professeur
                ET.SubElement(matiere_element, "Salle").text = salle

        # Format xml file
        xml_string = ET.tostring(xml_doc, encoding="UTF-8")
        dom = xml.dom.minidom.parseString(xml_string)
        prettified_xml = dom.toprettyxml(indent="    ")

        # Create XML File
        with open(XML_Path_Emploi, "w", encoding="UTF-8") as generatedXML:
            generatedXML.write(prettified_xml)

        print("Fichier Emploi.xml créé avec succès")
    except Exception as ex:
        print(f"Erreur de création du fichier Emploi.xml: {ex}")


if __name__ == "__main__":
    # Example usage
    etudiant_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Etudiants.xlsx"
    modules_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Modules.xlsx"
    emploi_xl_path = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersExcel\\Emplois.xlsx"

    xml_path_GINF2 = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersXML\\XML\\GINF2.xml"
    xml_path_Emploi = "C:\\Users\\AnasChatt\\Desktop\\XMLProjet\\FichiersXML\\XML\\Emploi.xml"

    # Call the function with the specified Excel and XML file paths
    Creer_xml_GINF2(etudiant_xl_path, modules_xl_path, xml_path_GINF2)
    Creer_xml_Emploi(emploi_xl_path, modules_xl_path, xml_path_Emploi)
