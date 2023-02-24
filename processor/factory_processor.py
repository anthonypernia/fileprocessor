
from processor.jsonprocessor import JSONProcessor

class FactoryProcessor():


    def process(self, filename: str):
        """check file format and process it

        Args:
            filename (str): filename

        Raises:
            Exception: if fileformat not supported
        """
        if filename.endswith(".json"):
            processor = JSONProcessor()
        else:
            raise Exception("File format not supported")
        
        processor.process(filename)