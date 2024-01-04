from lxml import etree


def validate_with_dtd(xml_file_path, dtd_file_path):
    try:
        f = open(xml_file_path, "r")
        dtd = etree.DTD(dtd_file_path)
        xml_file = etree.parse(f)
        return dtd.validate(xml_file)
    except IOError as err:
        print("Could not read File: ", err)
        return False
    except etree.XMLSyntaxError as e:
        print("XML File not Well-Formed: ", e)
        return False


def validate_with_xsd(xml_file_path, xsd_file_path):
    try:
        f1 = open(xml_file_path, "r")
        f2 = open(xsd_file_path, "r")
        xml_file = etree.parse(f1)
        xsd_file = etree.parse(f2)
        xsd = etree.XMLSchema(xsd_file)
        return xsd.validate(xml_file)
    except IOError as err:
        print("Could not read File: ", err)
        return False
    except etree.XMLSyntaxError as e:
        print("XML File not Well-Formed: ", e)
        return False
    except etree.XMLSchemaParseError as e:
        print("XSD File error: ", e)
        return False

