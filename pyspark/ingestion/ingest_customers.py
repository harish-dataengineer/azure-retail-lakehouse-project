from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("RetailNova Customer Ingestion")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("../../datasets/raw/customers.csv")
)

print("=" * 80)
print("CUSTOMER DATA")
print("=" * 80)

df.show()

print("=" * 80)
print("SCHEMA")
print("=" * 80)

df.printSchema()

print("=" * 80)
print("TOTAL RECORDS")
print("=" * 80)

print(df.count())

spark.stop()