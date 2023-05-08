import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):
        fabricate_date = [
            datetime.datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            )
            for product in products
        ]
        near_expiration_date = min(
            (
                product["data_de_validade"]
                for product in products
                if product["data_de_validade"]
                >= datetime.datetime.now().strftime("%Y-%m-%d")
            )
        )
        company_most_itens = [
            product["nome_da_empresa"] for product in products
        ]

        old_fabricate_date = min(fabricate_date).strftime("%Y-%m-%d")

        company_most = Counter(company_most_itens).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {old_fabricate_date}\n"
            f"Data de validade mais próxima: {near_expiration_date}\n"
            f"Empresa com mais produtos: {company_most}"
        )
