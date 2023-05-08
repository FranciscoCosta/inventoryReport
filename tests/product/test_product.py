from inventory_report.inventory.product import Product


def test_cria_produto():
    product_mock = {
        "id": 1,
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1.",
    }
    product = Product(**product_mock)

    for key, value in product_mock.items():
        assert getattr(product, key) == value
