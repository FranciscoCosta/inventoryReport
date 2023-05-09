import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path) as file:
                reader = csv.DictReader(file)
                data = list(reader)
                return data
        else:
            raise ValueError("Arquivo inválido")
