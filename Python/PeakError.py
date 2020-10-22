from PeakErrorInterface import interface
import util
import numpy as np
import pandas as pd


def pandasError(peaks, regions):
    if not util.checkChrom(peaks):
        return
    if not util.checkChrom(regions):
        return





    return "Bottom"


def pandasErrorChrom(peaks, regions):
    if not util.checkPositions(peaks):
        return

    if not util.checkPositions(regions):
        return

    p = peaks.sort_values('chromStart', ignore_index=True)
    r = regions.sort_values('chromStart', ignore_index=True)

    code = r['annotation'].apply(util.toCode)
    unknown = r['annotation'][code.isnull()]

    if unknown.size > 0:
        uniques = unknown.unique()

        for unique in uniques:
            print("Annotation %s was found, invalid annotation" % unique)
            return

    output = interface(p['chromStart'].to_numpy(dtype=np.intc), p['chromEnd'].to_numpy(dtype=np.intc), len(p.index),
                       r['chromStart'].to_numpy(dtype=np.intc), r['chromEnd'].to_numpy(dtype=np.intc),
                       code.to_numpy(dtype=np.intc), len(r.index))

    error = pd.DataFrame(output)

    error = pd.concat(objs=[r, error], axis=1)

    error['fp_status'] = error['fp'].apply(util.fpStatus)

    error['fn'] = error.apply(util.fnCalc, axis=1)

    error['fn_status'] = error['fn'].apply(util.fnStatus)

    error['status'] = error.apply(util.status, axis=1)

    return error
