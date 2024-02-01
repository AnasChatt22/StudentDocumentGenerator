import os
import subprocess

import pdfkit as pdf
from bs4 import BeautifulSoup
from lxml import etree


def generate_html_from_xquery(xml_file, xquery_file, output_html_file, id_etudiant):
    try:
        # Lancer le processus externe avec BaseX
        process = subprocess.Popen(
            ['basex', "-i", xml_file, "-b", f'idEtudiant={id_etudiant}', xquery_file, "-o", output_html_file],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

        # Capturer la sortie et les erreurs du processus
        output, err = process.communicate()
        process.wait()

        # Vérifier si le processus s'est terminé avec succès (code de retour 0)
        if process.returncode != 0:
            print(output)
        else:
            # Formater le fichier HTML avec BeautifulSoup
            soup = BeautifulSoup(output.decode('utf-8'), 'html.parser')
            formatted_html = soup.prettify()

            # Enregistrer le fichier HTML formaté
            with open(output_html_file, "w", encoding='utf-8') as output_file:
                output_file.write(formatted_html)

            print("Fichier HTML généré avec succès (En utilisant XQuery).")
            return True
    except Exception as ex:
        print(f"Erreur de génération de HTML en utilisant XQuery: {ex}")
        return False


def generate_html_from_xslt(xml_file, xslt_file, output_html_file, id_etudiant=None):
    try:
        # Charger les fichiers XML et XSLT
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Créer un transformateur XSLT
        transform = etree.XSLT(xslt_tree)

        # Appliquer la transformation au document XML
        if id_etudiant:
            result_tree = transform(xml_tree, id_etudiant=str(id_etudiant))
        else:
            result_tree = transform(xml_tree)

        # Formater le fichier HTML avec BeautifulSoup
        soup = BeautifulSoup(str(result_tree), 'html.parser')
        formatted_html = soup.prettify()

        # Enregistrer le résultat dans un fichier HTML avec l'encodage UTF-8 explicite
        with open(output_html_file, 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_html)
        print("Fichier HTML généré avec succès (En utilisant XSLT).")
        return True
    except Exception as ex:
        print(f"Erreur de génération de HTML en utilisant XSLT: {ex}")
        return False


def generate_pdf_from_html(html_file, output_pdf, Options=None):
    try:
        # Spécifier le chemin complet de wkhtmltopdf ici
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Initialiser la configuration avec le chemin de wkhtmltopdf
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Utiliser la configuration lors de la conversion
        if pdf.from_file(html_file, output_pdf, configuration=config, options=Options):
            print("Fichier PDF généré avec succès (En utilisant HTML).")
            return True
        else:
            return False
    except Exception as ex:
        print(f"Erreur de génération du PDF en utilisant HTML: {ex}")
        return False


def generate_pdf_from_xquery(xml_file, xquery_fo, output_pdf, id_etudiant):
    # Définir un fichier temporaire pour le résultat intermédiaire au format XSL-FO
    temp = "../FichiersXML/XML/temp.fo"

    try:
        # Exécuter la requête XQuery et sauvegarder le résultat au format XSL-FO
        process = subprocess.Popen(
            ['basex', "-i", xml_file, "-b", f'idEtudiant={id_etudiant}', xquery_fo, "-o", temp],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True)

        output, err = process.communicate()
        process.wait()

        # Vérifier le code de retour de la requête XQuery
        if process.returncode != 0:
            print("Erreur lors de l'exécution de la requête XQuery :", process.returncode)
            raise Exception("Erreur lors de l'exécution de la requête XQuery")

        # Écrire le résultat dans le fichier temporaire
        with open(temp, "w+", encoding='utf-8') as output_file:
            output_file.write(output.decode())

        # Convertir le fichier XSL-FO en PDF en utilisant Apache FOP
        subprocess.run(
            ['fop', '-fo', temp, '-pdf', output_pdf], shell=True)

        # Supprimer le fichier temporaire
        os.remove(temp)

        print("Fichier PDF généré avec succès (En utilisant XQuery-FO).")
        return True
    except Exception as ex:
        print(f"Erreur de génération du PDF en utilisant XQuery-FO: {ex}")
        return False


def generate_pdf_from_xslt(xml_file, xslt_file, output_pdf, Options=None, id_etudiant=None):
    try:
        # Charger les fichiers XML et XSLT
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Créer un transformateur XSLT
        transform = etree.XSLT(xslt_tree)

        # Appliquer la transformation au document XML
        if id_etudiant:
            result_tree = transform(xml_tree, id_etudiant=str(id_etudiant))
        else:
            result_tree = transform(xml_tree)

        # Convertir le XML transformé en une chaîne HTML
        html_content = str(result_tree, encoding='utf-8')

        # Spécifier le chemin de wkhtmltopdf
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Initialiser la configuration avec le chemin de wkhtmltopdf
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Convertir HTML en PDF en utilisant le fichier HTML temporaire
        if pdf.from_string(html_content, output_pdf, configuration=config, options=Options):
            print("Fichier PDF créé avec succès")
            return True
        else:
            return False
    except Exception as ex:
        print(f"Erreur de génération du PDF en utilisant XSLT: {ex}")
        return False


# XML
xml_ginf2 = "../FichiersXML/XML/GINF2.xml"
xml_emploi = "../FichiersXML/XML/Emploi.xml"

# XSLT
xslt_carteEtd = "../FichiersXML/XSLT/CarteEtd.xsl"
xslt_att_reuss = "../FichiersXML/XSLT/Attestation_reussite.xsl"
xslt_Emplois = "../FichiersXML/XSLT/Emploi.xsl"
xslt_rlv_gen = "../FichiersXML/XSLT/releve_general.xsl"

# XQuery
Xquery_rlv_note_perso_pdf = "../FichiersXML/FO/releve_personnel_pdf.xquery"
Xquery_rlv_note_perso_html = "../FichiersXML/XQuery/releve_personnel.xquery"
Xquery_att_sco_pdf = "../FichiersXML/FO/attestation_sco_pdf.xquery"
Xquery_att_sco_html = "../FichiersXML/XQuery/attestation_sco_html.xquery"

# HTML
output_html_carteEtd = "../FichiersHTML/CarteEtd.html"
output_html_attReuss = "../FichiersHTML/Attestation_reussite.html"
output_html_Emplois = "../FichiersHTML/Emploi.html"
output_html_rlv_perso = "../FichiersHTML/Releve_perso.html"
output_html_att_sco = "../FichiersHTML/Attestation_scolarite.html"
output_html_rlv_gen = "../FichiersHTML/Releve_general.html"

# PDF
output_pdf_attReuss = "../FichiersPDF/Attestation_reussite.pdf"
output_pdf_Emplois = "../FichiersPDF/Emploi.pdf"
output_pdf_carteEtd = "../FichiersPDF/CarteEtd.pdf"
output_pdf_rlv_preso = "../FichiersPDF/Releve_perso.pdf"
output_pdf_att_sco = "../FichiersPDF/Attestation_scolarite.pdf"
output_pdf_rlv_gen = "../FichiersPDF/Releve_general.pdf"