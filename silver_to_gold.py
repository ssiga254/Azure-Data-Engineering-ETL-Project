from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SilverToGold") \
    .getOrCreate()

sales_df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

gold_df = sales_df.groupBy("customer_id") \
    .sum("quantity")

gold_df.show()
