import sys
import glob

from array2csv.loader import Loader
from array2csv.writer import Writer

"""
This is a wrapper script that uses the Loader() and Writer() classes from the array2csv package.
The aim of this script is to open .npz files, parse their data, and write it out in .csv format.
"""

if __name__ == "__main__":
    # Load a file
    loader = Loader(sys.argv[1])
    loader.load_file()

    # Save the data to CSV
    writer = Writer(loader.create_tiled_data(2), loader.get_identifier())
    writer.save()
