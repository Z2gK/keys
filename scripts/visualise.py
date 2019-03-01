import sys
import scipy
import matplotlib.pyplot as plt
import numpy as np

# Visualise 100ms worth of time domain signal

windowsize = 100e-3  # size of the time window of interest in seconds
keydowntimestamp = 1550981596.312444 # this is the start of the key press
endtimestamp     = 1550981615.3688593 # time stamp of the end of the capture
# Sample rate of data
samplerate = 4e6  # sample rate of input file

fp = open(sys.argv[1])
a = scipy.fromfile(fp, dtype=scipy.float32)
fp.close()

print("Total number of samples in file: {}".format(len(a)))

timepersample = 1.0/samplerate
n_samplesinwindow = int(windowsize/timepersample)

n_samplesfromback = int((endtimestamp - keydowntimestamp)/timepersample)

print("Number of samples from back: {}".format(n_samplesfromback))

#running_mean = np.convolve(a, np.ones(n_samplesinwindow,)/n_samplesinwindow, mode='valid')

#plt.plot(running_mean)

plt.subplot(2,1,1)
dataslice1 = a[-n_samplesfromback:-n_samplesfromback+n_samplesinwindow]
print(len(dataslice1))
plt.plot(dataslice1)

plt.subplot(2,1,2)
dataslice2 = a[-n_samplesfromback-n_samplesinwindow:-n_samplesfromback]
print(len(dataslice2))
plt.plot(dataslice2)

#plt.subplot(3,1,3)
#dataslice3 = dataslice1 - dataslice2
#plt.plot(dataslice3)

plt.show()

# Exploratory data analysis
#print(np.max(a))


# Code for sliding window max
# b = [np.max(a[x:x+40000]) for x in range(0,118055956,40000)]
