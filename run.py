import glob

from array2csv.loader import Loader
from array2csv.writer import Writer

"""
This is a wrapper script that uses the Loader() and Writer() classes from the array2csv package.
The aim of this script is to open .npz files, parse their data, and write it out in .csv format.
"""

if __name__ == "__main__":
    """
    Loops through all the .npz files in a path
    """
    for npz_file in glob.glob("./data/*.npz"):

        # Load a file
        loader = Loader(npz_file)
        loader.load_file()
        loader.set_identifier()

        # Save the data to CSV
        writer = Writer(loader.data, loader.get_identifier())
        writer.save()
