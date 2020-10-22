import PeakError
import pandas as pd


peaks = pd.read_csv('inst/exampleData/testpeaks.bed', sep='\t', header=None, index_col=False)
peaks.columns = ['chrom', 'chromStart', 'chromEnd']
labels = pd.read_csv('inst/exampleData/testlabels.bed', sep='\t', header=None, index_col=False)
labels.columns = ['chrom', 'chromStart', 'chromEnd', 'annotation']


output = PeakError.pandasErrorChrom(peaks, labels)

# print("Test Output", output)

peaks = pd.read_csv('inst/exampleData/peaks.bed', sep='\t', header=None, index_col=False)
peaks.columns = ['chrom', 'chromStart', 'chromEnd']
labels = pd.read_csv('inst/exampleData/labels.bed', sep='\t', header=None, index_col=False)
labels.columns = ['chrom', 'chromStart', 'chromEnd', 'annotation']


output = PeakError.pandasError(peaks, labels)

print("Test Output", output)



