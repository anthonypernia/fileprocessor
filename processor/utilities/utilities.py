
from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as F
from  pyspark.sql.dataframe import DataFrame
import processor.utilities.config as config


class Utilities:

        
    @staticmethod
    def init_spark() -> SQLContext:
        """init the sparkcontext
        Returns:
            SQLContext: sparkcontext
        """        
        sparkContext = SparkContext.getOrCreate()
        return SQLContext(sparkContext)
    
    @staticmethod
    def filter_nulls_by_column(df: DataFrame, column: str) -> DataFrame:
        """filter nulls in df
        Args:
            df (DataFrame): dataframe to filter
        Returns:
            DataFrame: filtered dataframe
        """
        return df.filter((F.col(column).isNotNull()) & (F.col(column) != '') & (F.col(column) != 'None'))
    

    def read_table_from_db(spark: SQLContext, table: str ) -> DataFrame:
        """read table from db
        Args:
            spark (SQLContext): spark
            database (str): database name
            table (str): tablename
        Returns:
            DataFrame: dataframe with data from dbtable
        """        
        df = spark.read.format("jdbc").options(
            url=config.db_mysql_url,
            driver= config.db_driver,
            dbtable=table,
            user=config.db_user,
            password=config.db_password
            ).load()
        return df
        
    @staticmethod
    def count_data(df: DataFrame, group_by: str, agg_by: str) -> DataFrame:
        """count data by columns
        Args:
            df (DataFrame): dataframe
            group_by (str): column to group by
            agg_by (str): column to count
        Returns:
            DataFrame: dataframe with count
        """        
        return df.groupBy(group_by).agg(F.count(agg_by).alias("count"))
    
    @staticmethod
    def write_data_to_db(df: DataFrame, table: str):
        """write data to db
        Args:
            df (DataFrame): dataframe to write
            database (str): database name
            table (str): tablename
        """        
        df.write.format("jdbc").options(
            url=config.db_mysql_url,
            driver= config.db_driver,
            dbtable=table,
            user=config.db_user,
            password=config.db_password
            ).mode("append").save()