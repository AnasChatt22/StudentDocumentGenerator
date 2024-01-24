import os
import subprocess

import pdfkit as pdf
from lxml import etree


def generate_html_from_xquery(xquery_data, xquery, html_output, id_etudiant):
    process = subprocess.Popen(
        ['basex', "-i", xquery_data, "-b", f'idEtudiant={id_etudiant}', xquery, "-o", html_output],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True)
    output, err = process.communicate()
    process.wait()
    if process.returncode != 0:
        print(output)

    else:
        with open(html_output, "w", encoding='utf-8') as output_file:
            output_file.write(output.decode('utf-8'))

        # Convert XSL-FO to PDF using Apache FOP

        print("html generated successfully.")


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

        print("PDF generated successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


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

        # Output the result to an HTML file with explicit UTF-8 encoding
        with open(output_html_file, 'w', encoding='utf-8') as html_file:
            html_file.write(str(result_tree, encoding='utf-8'))

        print("Fichier html créé avec succès")
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
            print("Fichier PDF générer avec succès")
            return True
        else:
            return False
    except Exception as ex:
        print(f"Erreur :{ex}")


def generate_pdf_from_xslt(xml_file, xslt_file, output_pdf, Options, id_etudiant=None):
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
xml_ginf2_path = "../FichiersXML/XML/GINF2.xml"
xml_emploi_path = "../FichiersXML/XML/Emploi.xml"

# XSLT
xslt_carteEtd_path = "../FichiersXML/XSLT/CarteEtd.xsl"
xslt_att_reuss_path = "../FichiersXML/XSLT/Attestation_reussite.xsl"
xslt_EmploisAll_path = "../FichiersXML/XSLT/Emplois.xsl"
xslt_rlv_gen_path = "../FichiersXML/XSLT/releve_general.xsl"

# Xquery
Xquery_rlv_note_perso_pdf = "../FichiersXML/FO/releve_personnel_pdf.xquery"
Xquery_rlv_note_perso_html = "../FichiersXML/Xquery/releve_personnel.xquery"
Xquery_att_sco_pdf = "../FichiersXML/FO/attestation_pdf.xquery"
Xquery_att_sco_html = "../FichiersXML/Xquery/attestation.xquery"

# HTML
output_html_carteEtd_path = "../FichiersHTML/CarteEtd.html"
output_html_attReuss_path = "../FichiersHTML/Attestation_reussite.html"
output_html_AllEmp_path = "../FichiersHTML/Emplois.html"
output_html_rlv_perso = "../FichiersHTML/Releve_perso.html"
output_html_att_sco = "../FichiersHTML/Attestation_scolarite.html"
output_html_rlv_gen = "../FichiersHTML/Releve_general.html"

# PDF
output_pdf_attReuss_path = "../FichiersPDF/Attestation_reussite.pdf"
output_pdf_AllEmp_path = "../FichiersPDF/Emplois.pdf"
output_pdf_CarteEtd = "../FichiersPDF/CarteEtd.pdf"
output_pdf_rlv_preso = "../FichiersPDF/Releve_perso.pdf"
output_pdf_att_sco = "../FichiersPDF/Attestation_scolarite.pdf"
output_pdf_rlv_gen = "../FichiersPDF/Releve_general.pdf"

options = {
    'quiet': '',
    'encoding': 'utf-8',
    'page-width': '2000px',
    'page-height': '800px'
}
# generate_pdf_from_html(output_html_rlv_gen, output_pdf_rlv_gen, options)
