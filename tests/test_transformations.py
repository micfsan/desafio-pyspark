import pytest
from pyspark.sql import SparkSession, Row
from processing.transformations import Transformation


@pytest.fixture(scope="session")
def spark_session():
    """Cria uma SparkSession única para os testes."""
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("Desafio-Unit-Tests")
        .getOrCreate()
    )
    yield spark
    spark.stop()


def test_filter_legit_refused_2025(spark_session):
    """
    Testa o filtro de pedidos recusados, legítimos e de 2025.
    Inclui verificação do ID_Pedido solicitado no escopo.
    """
    transformer = Transformation()

    # 1. Dados de Pedidos
    pedidos_data = [
        Row(id_pedido="101", uf="SP", valor_unitario=100.0, quantidade=2, data_criacao="2025-05-20 10:00:00"),
        Row(id_pedido="102", uf="RJ", valor_unitario=50.0, quantidade=1, data_criacao="2024-12-31 23:59:59"),
        Row(id_pedido="103", uf="MG", valor_unitario=10.0, quantidade=10, data_criacao="2025-01-01 00:01:00"),
    ]

    # 2. Dados de Pagamentos
    pagamentos_data = [
        Row(id_pedido="101", status=False, fraude=False, metodo_pagamento="cartao"),
        Row(id_pedido="102", status=False, fraude=False, metodo_pagamento="pix"),
        Row(id_pedido="103", status=False, fraude=True, metodo_pagamento="boleto"),
    ]

    df_ped = spark_session.createDataFrame(pedidos_data)
    df_pag = spark_session.createDataFrame(pagamentos_data)

    # 3. Executar Lógica
    df_resultado = transformer.filter_legit_refused_2025(df_ped, df_pag)
    resultados = df_resultado.collect()

    # 4. Asserts (Evidências de sucesso)
    assert df_resultado.count() == 1
    assert resultados[0]["ID_Pedido"] == "101"  
    assert resultados[0]["Estado"] == "SP"
    assert resultados[0]["Valor_Total"] == 200.0
    assert resultados[0]["Forma_Pagamento"] == "cartao"

def test_schema_columns(spark_session):
    """Verifica se TODAS as colunas solicitadas pelo professor estão no DataFrame final."""
    transformer = Transformation()

    df_ped = spark_session.createDataFrame(
        [Row(id_pedido="1", uf="SC", valor_unitario=10.0, quantidade=1, data_criacao="2025-01-01")]
    )
    df_pag = spark_session.createDataFrame(
        [Row(id_pedido="1", status=False, fraude=False, metodo_pagamento="debito")]
    )

    df_res = transformer.filter_legit_refused_2025(df_ped, df_pag)

    # Lista de colunas conforme o escopo do PDF do professor
    colunas_esperadas = ["ID_Pedido", "Estado", "Forma_Pagamento", "Valor_Total", "Data_Pedido"]
    
    for col in colunas_esperadas:
        assert col in df_res.columns, f"Coluna {col} não encontrada no resultado final!"