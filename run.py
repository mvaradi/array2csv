import sys

from array2csv.loader import Loader
from array2csv.writer import Writer





if __name__ == "__main__":
    loader = Loader(sys.argv[1])
    loader.load_file()

    writer = Writer(loader.data)
    writer.save()