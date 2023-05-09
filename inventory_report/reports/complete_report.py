from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:

    @staticmethod
    def generate(data):
        report = SimpleReport.generate(data)
        report += "\nProdutos estocados por empresa:\n"
        companies = [product["nome_da_empresa"] for product in data]
        companies = Counter(companies)
        for company in companies:
            report += f"- {company}: {companies[company]}\n"
        return report
