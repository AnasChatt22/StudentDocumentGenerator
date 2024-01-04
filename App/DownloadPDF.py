import pdfkit as pdf
from lxml import etree


def Download_emploi(xml_file, xslt_file, output_pdf):
    try:
        # Load XML and XSLT files
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_tree)

        # Apply the transformation to the XML document
        result_tree = transform(xml_tree)

        # Convert transformed XML to HTML string
        html_content = str(result_tree, encoding='utf-8')

        # Convert HTML to PDF
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)
        options = {
            'quiet': '',
            'encoding': 'utf-8',
            'page-width': '1300px',
            'page-height': '750px'
        }

        if pdf.from_string(html_content, output_pdf, configuration=config, options=options):
            print("PDF file generated successfully")
            return True
        else:
            return False

    except Exception as ex:
        print(f"Error Downloading emploi : {ex}")


def Download_CarteEtd(xml_file, xslt_file, output_pdf, id_etudiant):
    try:
        # Load XML and XSLT files
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_tree)

        # Apply the transformation to the XML document
        result_tree = transform(xml_tree, id_etudiant=str(id_etudiant))

        # Convert transformed XML to HTML string
        html_content = str(result_tree, encoding='utf-8')

        # Convert HTML to PDF
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)
        options = {
            'quiet': '',
            'encoding': 'utf-8'
        }

        if pdf.from_string(html_content, output_pdf, configuration=config, options=options):
            print("PDF file generated successfully")
            return True
        else:
            return False

    except Exception as ex:
        print(f"Error Downloading Carte etudiant : {ex}")


def Download_Att_reuss(xml_file, xslt_file, output_pdf, id_etudiant):
    try:
        # Load XML and XSLT files
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_tree)

        # Apply the transformation to the XML document
        result_tree = transform(xml_tree, id_etudiant=str(id_etudiant))

        # Convert transformed XML to HTML string
        html_content = str(result_tree, encoding='utf-8')

        # Convert HTML to PDF
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=wkhtmltopdf_path)
        options = {
            'quiet': '',
            'encoding': 'utf-8'
        }

        if pdf.from_string(html_content, output_pdf, configuration=config, options=options):
            print("PDF file generated successfully")
            return True
        else:
            return False

    except Exception as ex:
        print(f"Error Downloading attestation de reussite : {ex}")
