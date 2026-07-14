from pyspark.common.spark_session import get_spark

spark = get_spark("RetailNova Product Ingestion")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("../../datasets/raw/products.csv")
)

print("=" * 80)
print("PRODUCT DATA")
print("=" * 80)

df.show()

print("=" * 80)
print("SCHEMA")
print("=" * 80)

df.printSchema()

print("=" * 80)
print("TOTAL PRODUCTS")
print("=" * 80)

print(df.count())

spark.stop()