from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BronzeToSilver") \
    .getOrCreate()

sales_df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

silver_df = sales_df.dropDuplicates()

silver_df.show()
