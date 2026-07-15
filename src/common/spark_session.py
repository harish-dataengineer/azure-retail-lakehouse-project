from pyspark.sql import SparkSession


def get_spark(app_name: str = "RetailNova"):
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")        # Local mode
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark