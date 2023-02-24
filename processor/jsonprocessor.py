from processor.utilities.utilities import Utilities as util
from processor.fileprocessor import FileProcessor
from  pyspark.sql.dataframe import DataFrame
import pyspark.sql.functions as F
import processor.utilities.config as config

class JSONProcessor(FileProcessor):

    def read_data(self, filename: str, multiLine: bool = True) -> DataFrame:
        """read json file
        Args:
            filename (str): filename
            multiLine (bool, optional): multiline. Defaults to True.

        Returns:
            DataFrame: dataframe readed
        """
        return self.spark.read.format("json").load(filename, multiLine=multiLine)

    def process(self, filename: str):
        """process json file
        Args:
            filename (str): filename
        """
        df_readed = self.read_data(filename)
        df_readed.show()
        df_filtered = util.filter_nulls_by_column(df_readed, "creation_date")
        df_filtered.show()
        df_table = util.read_table_from_db(self.spark, config.additional_event_table)
        df_joined = df_filtered.join(df_table, "event_id", "inner")
        df_joined.show()
        df_transformed = df_joined.withColumn("creation_date", F.to_date(df_joined.creation_date))
        df_transformed.show()
        df_grouped = util.count_data(df_transformed, ["creation_date", "country", "device_type"], "event_id")
        df_grouped.show()
        util.write_data_to_db(df_grouped, config.db_final_table)


