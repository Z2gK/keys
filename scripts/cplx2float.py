import sys
import scipy
import numpy as np

if (len(sys.argv) != 3):
    print("This script converts IQ GNUradio data to floats")
    print("Argument: <IQ file> <output file>")
    exit()

fp = open(sys.argv[1])
arr = scipy.fromfile(open(sys.argv[1]),dtype=scipy.complex64)
floatstream = np.abs(arr)
floatstream.tofile(sys.argv[2])

fp.close()
