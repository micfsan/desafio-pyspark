import logging
from config.settings import load_config
from session.spark_session import SparkManager
from io_utils.data_handler import DataHandler
from pipeline.pipeline import FraudPipeline
from processing.transformations import Transformation  # Já está correto aqui


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def main():
    setup_logging()
    config = load_config()

    # Instanciando dependências
    spark_man = SparkManager(config["spark"]["app_name"])
    spark = spark_man.get_session()

    dh = DataHandler(spark)
    
    # AJUSTE 1: Mudar de BusinessLogic() para Transformation()
    logic = Transformation()

    # AJUSTE 2: Garantir que a variável 'logic' (agora uma instância de Transformation)
    # seja injetada corretamente no Pipeline
    pipeline = FraudPipeline(spark, dh, logic)

    try:
        pipeline.run(config)
    except Exception as e:
        logging.error(f"Falha crítica na execução do pipeline: {e}")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()