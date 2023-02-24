from processor.factory_processor import FactoryProcessor

def process():
    factory = FactoryProcessor()
    factory.process("data-example/data.json")


if __name__ == "__main__":
    process()


