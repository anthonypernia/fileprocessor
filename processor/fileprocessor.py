from processor.utilities.utilities import Utilities as util
from abc import ABC, abstractmethod
from  pyspark.sql.dataframe import DataFrame

class FileProcessor(ABC):

    def __init__(self):
        self.spark = util.init_spark()

    def read_data(self, filename: str) -> DataFrame:
        ...

    @abstractmethod
    def process(self, filename: str):
        ...

