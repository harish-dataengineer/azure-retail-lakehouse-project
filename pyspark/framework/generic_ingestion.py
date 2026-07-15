from pyspark.common.spark_session import create_spark
from pyspark.common.logger import logger
from pyspark.common.config_reader import read_metadata

spark = create_spark("RetailNova Generic Ingestion")

metadata = read_metadata("../../metadata/tables.json")

for table in metadata["tables"]:

    logger.info(f"Processing {table['table_name']}")

    path = f"../../datasets/raw/{table['file_name']}"

    df = (
        spark.read
        .option("header", table["header"])
        .option("inferSchema", True)
        .option("delimiter", table["delimiter"])
        .csv(path)
    )

    print("="*80)
    print(table["table_name"].upper())
    print("="*80)

    df.show(5)

    print(df.count())

spark.stop()