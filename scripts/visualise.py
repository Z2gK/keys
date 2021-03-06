import sys
import scipy
import matplotlib.pyplot as plt
import numpy as np

# Visualise 100ms worth of time domain signal
# Visualise 10% of a time-domain file including the relevant keypress lines,
# given the follow arguments
# 1 - time domain filename
# 2 - .mtime file
# 3 - sample rate of time domain file, in full form, e.g. 40000 instead of 4e6
# 4 - keypress file
# 5 - which 10% slice to plot: 0...9
# 6 - number of samples for aggregation to enable better plotting

windowsize = 100e-3  # size of the time window of interest in seconds
keydowntimestamp = 1550981596.312444 # this is the start of the key press
endtimestamp     = 1550981615.3688593 # time stamp of the end of the capture
# Sample rate of data
samplerate = 4e6  # sample rate of input file

fp = open(sys.argv[1])
a = scipy.fromfile(fp, dtype=scipy.float32)
fp.close()

n_samplestotal = len(a)
print("Total number of samples in file: {}".format(n_samplestotal))

timepersample = 1.0/samplerate
n_samplesinwindow = int(windowsize/timepersample)

n_samplesfromback = int((endtimestamp - keydowntimestamp)/timepersample)

print("Number of samples from back: {}".format(n_samplesfromback))

#running_mean = np.convolve(a, np.ones(n_samplesinwindow,)/n_samplesinwindow, mode='valid')

#plt.plot(running_mean)

#plt.subplot(2,1,1)
#dataslice1 = a[-n_samplesfromback:-n_samplesfromback+n_samplesinwindow]
#print(len(dataslice1))
#plt.plot(dataslice1)

#plt.subplot(2,1,2)
#dataslice2 = a[-n_samplesfromback-n_samplesinwindow:-n_samplesfromback]
#print(len(dataslice2))
#plt.plot(dataslice2)

#plt.subplot(3,1,3)
#dataslice3 = dataslice1 - dataslice2
#plt.plot(dataslice3)

#plt.show()

# Exploratory data analysis
#print(np.max(a))


# Code for sliding window max - applies to dummy03
# Also plot the windows
# timeslices = [(1550981596.312444, 1550981596.392425),
#              (1550981596.688417, 1550981596.784408),
#              (1550981597.40411, 1550981597.128403),
#              (1550981599.896386,1550981599.960376)]

subwindow = int(n_samplestotal/10)

aggregatewindow = 40000
b = [np.max(a[x:x+aggregatewindow]) for x in range(1*subwindow,(1+1)*subwindow,aggregatewindow)]
plt.plot(b)

#b = [np.max(a[x:x+40000]) for x in range(0,n_samplestotal,40000)]
#plt.plot(b)

# plot time slices
#for slice in timeslices:
#    start = slice[0]
#    end = slice[1]
#    start_in_plot = (n_samplestotal - (endtimestamp - start)/(1/4e6))/aggregatewindow
    # end_in_plot = (n_samplestotal - (endtimestamp - end)/(1/4e6))/aggregatewindow
#    plt.plot((start_in_plot,start_in_plot), (0.1,0.04), 'r')

plt.show()
