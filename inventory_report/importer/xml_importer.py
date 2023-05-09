import xml.etree.ElementTree as Et

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        data = []
        with open(path) as file:
            root_xml = Et.parse(file).getroot()
            for rec in root_xml.findall(".//record"):
                product_data = {}
                for tag in rec:
                    product_data[tag.tag] = tag.text
                data.append(product_data)
        return data
