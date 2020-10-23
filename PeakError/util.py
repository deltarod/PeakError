import numpy as np
import PeakErrorPandas as pd


def checkPositions(df):
    if not isinstance(df, pd.DataFrame):
        return False

    cols = ["chromStart", "chromEnd"]

    for column in cols:
        col = df[column]

        if not np.int64 == col.dtypes:
            return False

        if (col < 1).empty:
            return False
    if df[df["chromStart"] > df['chromEnd']].size > 0:
        return False
    return True


def checkChrom(df):
    if not isinstance(df, pd.DataFrame):
        return False

    for val in df['chrom']:
        if not isinstance(val, str):
            return False

    # TODO: Check if factor

    return True


def toCode(annotation):
    annToCode = {'noPeaks': 0, 'noPeak': 0, 'peakStart': 1, 'peakEnd': 2, 'peaks': 3, 'peak': 3}
    try:
        output = annToCode[annotation]
    except KeyError:
        return None

    return output


def fpStatus(val):
    if val > 0:
        return 'false positive'
    else:
        return 'correct'


def fnCalc(row):
    return row['possible_tp'] - row['tp']


def fnStatus(val):
    if val > 0:
        return 'false negative'
    else:
        return 'correct'


def status(row):
    if row['fn'] > 0:
        return "false negative"
    else:
        if row['fp'] > 0:
            return "false positive"
        else:
            return "correct"
