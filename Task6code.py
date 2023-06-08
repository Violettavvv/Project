import xml.etree.ElementTree as ET

def verify_xml_syntax(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("Składnia pliku XML jest poprawna.")
    except ET.ParseError as e:
        print(f"Błąd składni pliku XML: {e}")

file_path = "sciezka/do/pliku.xml"
verify_xml_syntax(file_path)