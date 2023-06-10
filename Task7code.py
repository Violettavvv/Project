import xml.etree.ElementTree as ET

root = ET.Element("root")

element1 = ET.SubElement(root, "cos1")
element2 = ET.SubElement(root, "cos2")
element3 = ET.SubElement(root, "cos3")

cos1.text = "Wartość 1"
cos2.text = "Wartość 2"
cos3.text = "Wartość 3"

tree = ET.ElementTree(root)

tree.write("DanePlik.xml")