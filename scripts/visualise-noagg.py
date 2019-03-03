import sys
import scipy
import matplotlib.pyplot as plt
import numpy as np


if ((len(sys.argv) != 2) and (len(sys.argv) != 4)):
    print("Plots the file without aggregation")
    print("Arguments: <input file> <start sample index> <end sample index>")
    print("If start and end sample indices are omitted, the total number of samples is output and the user will be prompted to plot the entire data set")
    exit(1)

fp = open(sys.argv[1])
a = scipy.fromfile(fp, dtype=scipy.float32)
fp.close()

if (len(sys.argv) == 2):
    print("Total number of samples in file: {}".format(len(a)))
    resp = input("Do you want to plot all points (Y/N)? ")
    if ((resp == "Y") or (resp == "y")):
        print("let's plot!")

if (len(sys.argv) == 4):
    start_idx = int(sys.argv[2])
    end_idx = int(sys.argv[3])
    plt.plot(a[start_idx:end_idx])
    plt.show()
