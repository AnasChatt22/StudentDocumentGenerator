import os
import subprocess

import pdfkit as pdf
from bs4 import BeautifulSoup
from lxml import etree


def generate_html_from_xquery(xml_file, xquery_file, output_html_file, id_etudiant):
    process = subprocess.Popen(
        ['basex', "-i", xml_file, "-b", f'idEtudiant={id_etudiant}', xquery_file, "-o", output_html_file],
        stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    output, err = process.communicate()
    process.wait()
    if process.returncode != 0:
        print(output)
    else:
        # Format html file
        soup = BeautifulSoup(output.decode('utf-8'), 'html.parser')
        formatted_html = soup.prettify()

        with open(output_html_file, "w", encoding='utf-8') as output_file:
            output_file.write(formatted_html)

        # Convert XSL-FO to PDF using Apache FOP
        print("Fichier HTML généré avec succès (En utilisant XQuery).")


def generate_html_from_xslt(xml_file, xslt_file, output_html_file, id_etudiant=None):
    try:
        # Load XML and XSLT files
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_tree)

        # Apply the transformation to the XML document
        if id_etudiant:
            result_tree = transform(xml_tree, id_etudiant=str(id_etudiant))
        else:
            result_tree = transform(xml_tree)

        # Format html file
        soup = BeautifulSoup(str(result_tree), 'html.parser')
        formatted_html = soup.prettify()
        # Output the result to an HTML file with explicit UTF-8 encoding
        with open(output_html_file, 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_html)

        print("Fichier HTML généré avec succès (En utilisant XSLT).")
    except Exception as ex:
        print(f"Erreur : {ex}")


def generate_pdf_from_html(html_file, output_pdf, Options=None):
    try:
        # Spécifiez le chemin complet de wkhtmltopdf ici
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Initialisez la configuration avec le chemin de wkhtmltopdf
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Utilisez la configuration lors de la conversion
        if pdf.from_file(html_file, output_pdf, configuration=config, options=Options):
            print("Fichier PDF généré avec succès (En utilisant HTML).")
            return True
        else:
            return False
    except Exception as ex:
        print(f"Erreur :{ex}")


def generate_pdf_from_xquery_fo(xml_file, xquery_foo, output_pdf, id_etudiant):
    temp = "../FichiersXML/XML/temp.fo"

    try:
        process = subprocess.Popen(
            ['basex', "-i", xml_file, "-b", f'idEtudiant={id_etudiant}', xquery_foo, "-o", temp],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True)

        output, err = process.communicate()
        process.wait()

        if process.returncode != 0:
            print("Error executing XQuery:", process.returncode)
            raise Exception("Error executing XQuery")

        with open(temp, "w+", encoding='utf-8') as output_file:
            output_file.write(output.decode())

        # Convert XSL-FO to PDF using Apache FOP
        subprocess.run(
            ['fop', '-fo', temp, '-pdf', output_pdf], shell=True)

        os.remove(temp)

        print("Fichier PDF généré avec succès (En utilisant XQuery-FO).")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def generate_pdf_from_xslt(xml_file, xslt_file, output_pdf, id_etudiant=None, Options=None):
    try:
        # Load XML and XSLT files
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_tree)

        # Apply the transformation to the XML document
        if id_etudiant:
            result_tree = transform(xml_tree, id_etudiant=str(id_etudiant))
        else:
            result_tree = transform(xml_tree)

        # Convert transformed XML to HTML string
        html_content = str(result_tree, encoding='utf-8')

        # Specify the path to wkhtmltopdf
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Initialize the configuration with the path to wkhtmltopdf
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Convert HTML to PDF using the temporary HTML file
        if pdf.from_string(html_content, output_pdf, configuration=config, options=Options):
            print("Fichier PDF créé avec succès")
            return True
        else:
            return False
    except Exception as ex:
        print(f"Error converting XML to PDF: {ex}")


# XML
xml_ginf2 = "../FichiersXML/XML/GINF2.xml"
xml_emploi = "../FichiersXML/XML/Emploi.xml"

# XSLT
xslt_carteEtd = "../FichiersXML/XSLT/CarteEtd.xsl"
xslt_att_reuss = "../FichiersXML/XSLT/Attestation_reussite.xsl"
xslt_Emplois = "../FichiersXML/XSLT/Emplois.xsl"
xslt_rlv_gen = "../FichiersXML/XSLT/releve_general.xsl"

# Xquery
Xquery_rlv_note_perso_pdf = "../FichiersXML/FO/releve_personnel_pdf.xquery"
Xquery_rlv_note_perso_html = "../FichiersXML/Xquery/releve_personnel.xquery"
Xquery_att_sco_pdf = "../FichiersXML/FO/attestation_pdf.xquery"
Xquery_att_sco_html = "../FichiersXML/Xquery/attestation.xquery"

# HTML
output_html_carteEtd = "../FichiersHTML/CarteEtd.html"
output_html_attReuss = "../FichiersHTML/Attestation_reussite.html"
output_html_Emplois = "../FichiersHTML/Emplois.html"
output_html_rlv_perso = "../FichiersHTML/Releve_perso.html"
output_html_att_sco = "../FichiersHTML/Attestation_scolarite.html"
output_html_rlv_gen = "../FichiersHTML/Releve_general.html"

# PDF
output_pdf_attReuss = "../FichiersPDF/Attestation_reussite.pdf"
output_pdf_Emplois = "../FichiersPDF/Emplois.pdf"
output_pdf_carteEtd = "../FichiersPDF/CarteEtd.pdf"
output_pdf_rlv_preso = "../FichiersPDF/Releve_perso.pdf"
output_pdf_att_sco = "../FichiersPDF/Attestation_scolarite.pdf"
output_pdf_rlv_gen = "../FichiersPDF/Releve_general.pdf"

"""
options = {
    'quiet': '',
    'encoding': 'utf-8',
    'page-width': '2000px',
    'page-height': '800px'
}"""

options = {
    'quiet': '',
    'encoding': 'utf-8',
    'page-width': '1300px',
    'page-height': '835px'
}

generate_html_from_xslt(xml_emploi, xslt_Emplois, output_html_Emplois)
generate_html_from_xquery(xml_ginf2, Xquery_att_sco_html, output_html_att_sco, 20000493)

# generate_pdf_from_xslt(xml_emploi, xslt_Emplois, output_pdf_Emplois, Options=options)
