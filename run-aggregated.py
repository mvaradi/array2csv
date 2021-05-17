import sys
import glob

from npz_util.loader import Loader
from npz_util.writer import Writer

"""
This is a wrapper script that uses the Loader() and Writer() classes from the npz_util package.
The aim of this script is to open .npz files, parse their data, and write it out in .csv format.
"""

if __name__ == "__main__":
    # Load a file
    loader = Loader(sys.argv[1])
    loader.load_file()

    # Save the data to CSV
    writer = Writer(loader.create_tiled_data(2), loader.get_identifier())
    writer.save()
