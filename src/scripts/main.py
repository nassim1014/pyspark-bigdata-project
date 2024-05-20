from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

def main():
    spark = SparkSession.builder \
    .appName("NYC Taxi Duration Prediction") \
    .getOrCreate()

    df = spark
