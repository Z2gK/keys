import sys
import scipy
import matplotlib.pyplot as plt
import numpy as np


if ((len(sys.argv) != 2) and (len(sys.argv) != 5)):
    print("Plots the file without aggregation")
    print("Arguments: <input file> <start sample index> <end sample index> <aggregation window size>")
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

if (len(sys.argv) == 5):
    start_idx = int(sys.argv[2])
    end_idx = int(sys.argv[3])
    aggregatewindow = int(sys.argv[4])
    print("Section start and end indices {} {}".format(start_idx, end_idx))
    a_section = a[start_idx:end_idx]

    #    subwindow = int(n_samplestotal/10)
    b = [np.max(a_section[x:x+aggregatewindow]) for x in range(0, len(a_section), aggregatewindow)]

    #    plt.plot(a[start_idx:end_idx], linestyle=None, markersize = 1.0)
    plt.plot(b)
    commonfontsize = 14
    plt.xlabel("Samples (x {})".format(aggregatewindow), fontsize = 14)
    plt.ylabel("Signal Amplitude", fontsize = 14)
    plt.xticks(fontsize = commonfontsize)
    plt.yticks(fontsize = commonfontsize)
    plt.show()
