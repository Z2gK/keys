import sys
import scipy
import matplotlib.pyplot as plt
import numpy as np

# Visualise 10% of a time-domain file including the relevant keypress lines,
# given the follow arguments
# 1 - time domain filename
# 2 - .mtime file
# 3 - sample rate of time domain file, in full form, e.g. 40000 instead of 4e6
# 4 - keypress file
# 5 - which 10% slice to plot: 0...9
# 6 - number of samples for aggregation to enable better plotting
message = \
'''1 - time domain filename
2 - .mtime file
3 - sample rate of time domain file, in full form, e.g. 40000 instead of 4e6
4 - keypress file
5 - which 10% section to plot: 0...9
6 - number of samples for aggregation to enable better plotting'''

if (len(sys.argv) != 7):
    print("Arguments:")
    print(message)
    exit(1)

samplerate = int(sys.argv[3])  # sample rate of input file
print("Sample rate: {}".format(samplerate))
section = int(sys.argv[5])
print("Section: {}".format(section))
aggregatewindow = int(sys.argv[6])
print("Size of aggregate window: {}".format(aggregatewindow))

mtimefp = open(sys.argv[2])
endtimestamp = float(mtimefp.read().strip())
print("endtimestamp: {}".format(endtimestamp))
mtimefp.close()

keypressfp = open(sys.argv[4])


fp = open(sys.argv[1])
a = scipy.fromfile(fp, dtype=scipy.float32)
fp.close()

# windowsize = 100e-3  # size of the time window of interest in seconds
# keydowntimestamp = 1550981596.312444 # this is the start of the key press
# endtimestamp     = 1550981615.3688593 # time stamp of the end of the capture
# Sample rate of data

n_samplestotal = len(a)
print("Total number of samples in file: {}".format(n_samplestotal))

timepersample = 1.0/samplerate

# define the section to plot and plot it
section_start_idx = int(section * (n_samplestotal/10))
section_end_idx = int((section + 1)* (n_samplestotal/10))
a_section = a[section_start_idx:section_end_idx]
subwindow = int(n_samplestotal/10)
b = [np.max(a_section[x:x+aggregatewindow]) for x in range(0, subwindow, aggregatewindow)]

print("Section start and end indices: {} {}".format(section_start_idx,section_end_idx))
print("Length of section in original file: {}".format(len(a_section)))
print("Number of samples in aggregated section: {}".format(len(b)))

plt.plot(b)

# Now read the keypress file and see which keypresses are within the plotted range
keydownevents = []
for line in keypressfp:
    keypressline = line.strip().split(",")

    if ((keypressline[0] == "1") and (keypressline[2] == "1")):
        # key down event
        keyval = int(keypressline[1])
        timestamp = float(keypressline[3])
        keydownevents.append((keyval,timestamp))

# print(keydownevents)
# determine if event in within plotting window. If so, plot it
# offset is the human determined error between keypress time stamp and the actual on the IQ capture
offset = 6500000 # for normal operation just set this to 0. This is in number of samples in original capture
for event in keydownevents:
    timestamp = event[1]
    samplesfromstart = int(n_samplestotal - (endtimestamp - timestamp)/timepersample)
    samplesfromstart = samplesfromstart + offset
    #    print((endtimestamp - timestamp)/timepersample)
    if ((samplesfromstart >= section_start_idx) and (samplesfromstart <= section_end_idx)):
        # This event is within our window - plot it
        eventidx = int((samplesfromstart - section_start_idx)/aggregatewindow)
        plt.plot((eventidx,eventidx),(0.1,0.04),'r')
        
# n_samplesinwindow = int(windowsize/timepersample)
# n_samplesfromback = int((endtimestamp - keydowntimestamp)/timepersample)
# print("Number of samples from back: {}".format(n_samplesfromback))

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

# subwindow = int(n_samplestotal/10)

# b = [np.max(a[x:x+aggregatewindow]) for x in range(1*subwindow,(1+1)*subwindow,aggregatewindow)]
# plt.plot(b)

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
