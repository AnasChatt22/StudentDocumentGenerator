import subprocess
from lxml import etree
import pdfkit as pdf


def generate_html_from_xquery(xquery_data, xquery, html_output, variableValue):
    temp = "C:\\Users\\pc\\PycharmProjects\\XMLProjet\\FichiersXML\\XML\\temp.html"
    process = subprocess.Popen(
        ['basex', "-i", xquery_data, "-b", f'idEtudiant={variableValue}', xquery, "-o", html_output],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True)
    output, err = process.communicate()
    process.wait()
    if process.returncode != 0:
        print(output)

    else:
        with open(html_output, "wb") as output_file:
            output_file.write(output)

        # Convert XSL-FO to PDF using Apache FOP

        print("html generated successfully.")


def generate_pdf_from_xquery_foo(xquery_data, xquery_foo, output_pdf, variableValue):
    temp = "C:\\Users\\pc\\PycharmProjects\\XMLProjet\\FichiersXML\\XML\\temp.fo"
    process = subprocess.Popen(
        ['basex', "-i", xquery_data, "-b", f'idEtudiant={variableValue}', xquery_foo, "-o", temp],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True)

    output, err = process.communicate()
    process.wait()
    if process.returncode != 0:
        print("Error executing XQuery:", process.returncode)
    else:
        with open(temp, "w+", encoding='utf-8') as output_file:
            output_file.write(output.decode())

        # Convert XSL-FO to PDF using Apache FOP
        subprocess.run(
            ['fop', '-fo', temp, '-pdf', output_pdf], shell=True)
        print("pdf generated successfully.")


def generate_html_from_xslt(xml_file, xslt_file, output_html_file):
    try:
        # Load XML and XSLT files
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_tree)

        # Apply the transformation to the XML document
        result_tree = transform(xml_tree)

        # Output the result to an HTML file with explicit UTF-8 encoding
        with open(output_html_file, 'w', encoding='utf-8') as html_file:
            html_file.write(str(result_tree, encoding='utf-8'))

        print("Fichier html créé avec succès")
    except Exception as ex:
        print(f"Erreur:{ex}")


def generate_pdf_from_xslt(xml_file, xslt_file, output_pdf_file):
    temp = "C:\\Users\\pc\\PycharmProjects\\XMLProjet\\FichiersXML\\XML\\temp.html"
    generate_html_from_xslt(xml_file, xslt_file, temp)
    generate_pdf_from_html(temp, output_pdf_file)

def generate_pdf_from_html(html_file, output_pdf):
    try:
        # Spécifiez le chemin complet de wkhtmltopdf ici
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Initialisez la configuration avec le chemin de wkhtmltopdf
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)
        # Change options dependinh
        options = {
            'quiet': '',
            'encoding': 'utf-8',
            'page-width': '1400px',
            'page-height': '800px'
        }
        # Utilisez la configuration lors de la conversion
        pdf.from_file(html_file, output_pdf, configuration=config, options=options)
        print("Fichier pdf générer avec succès")
    except Exception as ex:
        print(f"Erreur : {ex}")



def generate_pdf_and_html(xml_file, xslt_file, output_html, output_pdf, id_etudiant=None):
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

        # Write HTML content to a temporary file
        with open(output_html, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print("Fichier html créé avec succès")

        # Specify the path to wkhtmltopdf
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        # Initialize the configuration with the path to wkhtmltopdf
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Customize options based on your requirements
        options = {
            'quiet': '',
            'encoding': 'utf-8'
        }

        # Convert HTML to PDF using the temporary HTML file
        pdf.from_file(output_html, output_pdf, configuration=config, options=options)
        print("Fichier PDF créé avec succès")
    except Exception as ex:
        print(f"Error converting XML to PDF: {ex}")


# XML
xml_ginf2_path = "../FichiersXML/XML/GINF2.xml"
xml_emploi_path = "../FichiersXML/XML/Emploi.xml"

# XSLT
xslt_carteEtd_path = "../FichiersXML/XSLTanas/CarteEtd.xsl"
xslt_att_reuss_path = "../FichiersXML/XSLTanas/Attestation_reussite.xsl"
xslt_EmploisAll_path = "../FichiersXML/XSLTanas/EmploisAll.xsl"
xslt_Emploi_mS1_path = "../FichiersXML/XSLTanas/Emploi_mS1.xsl"
xslt_Emploi_mS2_path = "../FichiersXML/XSLTanas/Emploi_mS2.xsl"
xslt_Emploi_mS3_path = "../FichiersXML/XSLTanas/Emploi_mS3.xsl"
xslt_Emploi_mS4_path = "../FichiersXML/XSLTanas/Emploi_mS4.xsl"

# HTML
output_html_carteEtd_path = "../FichiersHTML/CarteEtd.html"
output_html_attReuss_path = "../FichiersHTML/Attestation_reussite.html"
output_html_AllEmp_path = "../FichiersHTML/EmploisAll.html"
output_html_mS1_path = "../FichiersHTML/Emplois_mS1.html"
output_html_mS2_path = "../FichiersHTML/Emplois_mS2.html"
output_html_mS3_path = "../FichiersHTML/Emplois_mS3.html"
output_html_mS4_path = "../FichiersHTML/Emplois_mS4.html"

# PDF
output_pdf_attReuss_path = "../FichiersPDF/Attestation_reussite.pdf"
output_pdf_AllEmp_path = "../FichiersPDF/EmploisAll.pdf"
output_pdf_CarteEtd = "../FichiersPDF/CarteEtd.pdf"
output_pdf_mS1_path = "../FichiersPDF/Emploi_mS1.pdf"
output_pdf_mS2_path = "../FichiersPDF/Emploi_mS2.pdf"
output_pdf_mS3_path = "../FichiersPDF/Emploi_mS3.pdf"
output_pdf_mS4_path = "../FichiersPDF/Emploi_mS4.pdf"