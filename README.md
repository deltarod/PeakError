# pyPeakError
![](https://travis-ci.com/deltarod/PeakError.svg?branch=master)


A Python3 binding for PeakError, which can be found at [github.com/tdhock/PeakError](https://github.com/tdhock/PeakError)

## Functionalities

This section will explain some of the functionalities of pyPeakError.

Label files will need the column names chrom, chromStart, chromEnd, annotation

Peak files will need the column names chrom, chromStart, and chromEnd.

### pandasError
Calculates the error given a pandas dataframe for peaks and labels

### pandasErrorChrom
Calculates the error given that the peaks and labels df passed in is using all the same chrom

### pandasSummarize
Takes the output from either pandasError or pandasErrorChrom and summarizes the data into a one row DataFrame

## Installing
This section will explain how to install pyPeakError

### With Pip

`python3 -m pip install git+https://github.com/deltarod/PeakError.git`

### From Sources

1. `git clone https://github.com/deltarod/PeakError.git`
2. `cd PeakError/`
3. `python3 -m pip install .`
