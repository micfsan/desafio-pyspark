import logging
import sys
import os

from config.settings import ConfigManager
from session.spark_session import SparkManager
from io_utils.data_handler import DataHandler
from processing.transformations import Transformation
from pipeline.pipeline import FraudPipeline


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def main():
    setup_logging()
    config_manager = ConfigManager()
    config = config_manager.get_config()# 1. Classe de Configuração

    # 2. Instanciando dependência de Sessão Spark
    spark_man = SparkManager(config["spark"]["app_name"])
    spark = spark_man.get_session()
    
    # 3. Instanciando dependência de Leitura e Escrita (I/O)
    dh = DataHandler(spark)
    
   # 4. Instanciando dependência de Lógica de Negócios
    logic = Transformation()

    # 5. INJEÇÃO DE DEPENDÊNCIAS: Injetando dh e logic no Pipeline (Orquestrador)
    pipeline = FraudPipeline(spark, dh, logic)

    try:
        pipeline.run(config)
    except Exception as e:
        logging.error(f"Falha crítica na execução do pipeline: {e}")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()