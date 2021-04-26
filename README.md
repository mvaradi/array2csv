Array2Csv utility
====

[![Build Status](https://www.travis-ci.com/mvaradi/array2csv.svg?branch=main)](https://www.travis-ci.com/mvaradi/array2csv)
[![codecov](https://codecov.io/gh/mvaradi/array2csv/branch/master/graph/badge.svg?token=i8ZEnNxKLf)](https://codecov.io/gh/mvaradi/array2csv)
[![Maintainability](https://api.codeclimate.com/v1/badges/59c50e14dbf01c82f12c/maintainability)](https://codeclimate.com/github/mvaradi/array2csv/maintainability)

## Basic information

This is a simple package for reading in .npz files and writing out their data to .csv files.

## Usage

Clone this repository
```
git clone https://github.com/mvaradi/array2csv.git
```
Run the process:
```
python3 run.py path/to/files/
```

1.) The script will first load .npz files from a path, and grab the useful part of the data

2.) Then it will convert the information and save it into .csv output files

## Dependencies

For running:
`numpy`

For development: 
`codecov, pytest-cov`

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/PDBe-KB/pdbe-kb-uniprot-variant-import/tags).

## Authors
* **Mihaly Varadi** - *Initial work* - [mvaradi](https://github.com/mvaradi)

See also the list of [contributors](https://github.com/mvaradi/array2csv/contributors) who participated in this project.

## License
This project is licensed under the Apache License (version 2.) - see the [LICENSE](LICENSE) file for details.