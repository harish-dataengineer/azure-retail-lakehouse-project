from pyspark.common.spark_session import get_spark
from pyspark.common.logger import logger
from pyspark.common.config_reader import load_metadata


def ingest():

    spark = get_spark()

    metadata = load_metadata("metadata/tables.json")

    for table in metadata["tables"]:

        logger.info(f"Processing {table['table_name']}")

        file_path = f"datasets/raw/{table['file_name']}"

        df = (
            spark.read
            .option("header", table["header"])
            .option("delimiter", table["delimiter"])
            .option("inferSchema", True)
            .csv(file_path)
        )

        print("=" * 80)
        print(table["table_name"].upper())
        print("=" * 80)

        df.show(5, truncate=False)

        print(f"Total Records : {df.count()}")

    spark.stop()