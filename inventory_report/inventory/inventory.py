from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if path.endswith(".csv"):
            report_data = CsvImporter().import_data(path)
        elif path.endswith(".xml"):
            report_data = XmlImporter().import_data(path)
        else:
            report_data = JsonImporter().import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(report_data)
        elif report_type == "completo":
            return CompleteReport.generate(report_data)
