import Peak
import pandas as pd
import os

def test_PeakErrorChrom():
    exampleDataPath = '%s/inst/exampleData/' % os.getcwd()
    peaksPath = '%sonechrompeaks.bed' % exampleDataPath
    peaksdf = pd.read_csv(peaksPath, sep='\t', header=None, index_col=False)
    peaksdf.columns = ['chrom', 'chromStart', 'chromEnd']

    regionsPath = '%sonechromlabels.bed' % exampleDataPath
    regionsdf = pd.read_csv(regionsPath, sep='\t', header=None, index_col=False)
    regionsdf.columns = ['chrom', 'chromStart', 'chromEnd', 'annotation']

    output = Peak.errorChrom(peaksdf, regionsdf)

    testfp = [1, 1, 1, 0]

    assert testfp == output['fp'].tolist()

    testtp = [0, 1, 1, 1]

    assert testtp == output['tp'].tolist()


def test_PeakError():
    exampleDataPath = '%s/inst/exampleData/' % os.getcwd()
    peaksPath = '%speaks.bed' % exampleDataPath
    peaksdf = pd.read_csv(peaksPath, sep='\t', header=None, index_col=False)
    peaksdf.columns = ['chrom', 'chromStart', 'chromEnd']

    regionsPath = '%slabels.bed' % exampleDataPath
    regionsdf = pd.read_csv(regionsPath, sep='\t', header=None, index_col=False)
    regionsdf.columns = ['chrom', 'chromStart', 'chromEnd', 'annotation']

    output = Peak.error(peaksdf, regionsdf)

    testfp = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0]

    assert testfp == output['fp'].tolist()

    testtp = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1]

    assert testtp == output['tp'].tolist()


def test_summarize():
    exampleDataPath = '%s/inst/exampleData/' % os.getcwd()
    peaksPath = '%speaks.bed' % exampleDataPath
    peaksdf = pd.read_csv(peaksPath, sep='\t', header=None, index_col=False)
    peaksdf.columns = ['chrom', 'chromStart', 'chromEnd']

    regionsPath = '%slabels.bed' % exampleDataPath
    regionsdf = pd.read_csv(regionsPath, sep='\t', header=None, index_col=False)
    regionsdf.columns = ['chrom', 'chromStart', 'chromEnd', 'annotation']

    output = Peak.error(peaksdf, regionsdf)

    summary = Peak.summarize(output)

    toCheck = [16, 7, 12, 1, 12, 8]

    assert toCheck == summary.iloc[0].tolist()
