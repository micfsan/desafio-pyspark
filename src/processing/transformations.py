import logging
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

logger = logging.getLogger(__name__)

class Transformation:
    def add_valor_total_pedidos(self, df: DataFrame) -> DataFrame:
        """Calcula o valor total (valor_unitario * quantidade)"""
        return df.withColumn("valor_total", F.col("valor_unitario") * F.col("quantidade"))

    def filter_legit_refused_2025(self, df_pedidos: DataFrame, df_pagamentos: DataFrame) -> DataFrame:
        """Executa a lógica principal do desafio conforme escopo de negócio"""
        try:
            logger.info("Iniciando transformações de negócio...")

            # 1. Cruzar Pedidos com Pagamentos (Inner Join)
            joined_df = df_pedidos.join(df_pagamentos, "id_pedido", "inner")

            # 2. Aplicar Filtros: status=false, fraude=false, ano=2025
            relatorio = joined_df.filter(
                (F.col("status") == False)
                & (F.col("fraude") == False)
                & (F.year(F.col("data_criacao")) == 2025)
            )

            # 3. Calcular Valor Total usando o método da própria classe
            relatorio_com_valor = self.add_valor_total_pedidos(relatorio)

            # 4. Selecionar atributos solicitados e aplicar Ordenação
            # Itens solicitados: id_pedido, UF, Forma Pagamento, Valor Total e Data
            final_df = relatorio_com_valor.select(
                F.col("id_pedido").alias("ID_Pedido"),
                F.col("uf").alias("Estado"),
                F.col("metodo_pagamento").alias("Forma_Pagamento"),
                F.col("valor_total").alias("Valor_Total"),
                F.col("data_criacao").alias("Data_Pedido"),
            ).orderBy("Estado", "Forma_Pagamento", "Data_Pedido")

            logger.info("Transformações concluídas com sucesso e dados ordenados.")
            return final_df

        except Exception as e:
            logger.error(f"Erro ao processar lógica de negócio: {str(e)}")
            raise e