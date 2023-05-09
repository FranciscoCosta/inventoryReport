from inventory_report.inventory.product import Product


def test_relatorio_produto():
    p_mock = {
        "id": 1,
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1.",
    }

    product = Product(**p_mock)
    expected = (
        f"O produto {p_mock['nome_do_produto']}"
        f" fabricado em {p_mock['data_de_fabricacao']}"
        f" por {p_mock['nome_da_empresa']} com validade"
        f" até {p_mock['data_de_validade']}"
        f" precisa ser armazenado {p_mock['instrucoes_de_armazenamento']}."
    )

    assert repr(product) == expected
