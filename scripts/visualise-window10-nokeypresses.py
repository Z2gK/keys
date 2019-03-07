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
# plt.rcParams.update({'font.size': 36})
commonfontsize = 14
plt.xlabel("Samples (x {})".format(aggregatewindow), fontsize = commonfontsize)
plt.ylabel("Signal Amplitude", fontsize = commonfontsize)
plt.xticks(fontsize = commonfontsize)
plt.yticks(fontsize = commonfontsize)
plt.show()
