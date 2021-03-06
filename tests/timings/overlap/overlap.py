
from time import time
import datetime

from pyranges import PyRanges

import pandas as pd

chip = "/mnt/scratch/endrebak/genomes/chip/UCSD.Aorta.H3K27me3.STL003.bed.gz"
background = "/mnt/scratch/endrebak/genomes/chip/UCSD.Aorta.Input.STL002.bed.gz"

nrows = int(5e6) # None # int(1e6)

print("starting to read")
c = pd.read_table(chip, sep="\t", usecols=[0, 1, 2, 5], header=None, names="Chromosome Start End Strand".split(), nrows=nrows)
b = pd.read_table(background, sep="\t", usecols=[0, 1, 2, 5], header=None, names="Chromosome Start End Strand".split(), nrows=nrows)

print("done reading")
start = time()
c_gr = PyRanges(c)

print("first range finished")

end = time()

b_gr = PyRanges(b)

print("second range finished")
end2 = time()

first = datetime.datetime.fromtimestamp(end - start).strftime('%M\t%S\n')
second = datetime.datetime.fromtimestamp(end2 - end).strftime('%M\t%S\n')


start_overlap = time()

o_gr = c_gr.overlap(b_gr)

end_overlap = time()

overlap_time = datetime.datetime.fromtimestamp(end_overlap - start_overlap).strftime('%M\t%S\n')

print(first, second, overlap_time, sep="\n")
