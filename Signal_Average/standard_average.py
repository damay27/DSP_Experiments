import math
from matplotlib import pyplot as plt

def average(buffer):
    sum = 0
    for i in buffer:
        sum += i
    return sum/len(buffer)


##############################################
# Control values for the test signal
##############################################
signal_freq = 60 #Hz
signal_freq_rad = (signal_freq) * 2 * math.pi #60Hz in radians/second
phase = math.pi #seconds
dc_offset = 4.0
amplitude = 2.0

#Used to record signal values
buffer = []
#Used to record sampling time indices
time_buffer = []

#The frequency at which the signal is sampled
sampling_freq = 240 #Hz
sampling_freq_rad = sampling_freq * 2 * math.pi
#Amount of time to capture for in seconds
capture_time = .1 #second

#Use the sampling frequence and amount of time beign captured for
#to determine how long the buffer needs to be
buffer_len = math.ceil(sampling_freq_rad * capture_time)
print(buffer_len)


sample_time = 0
for i in range(buffer_len):
    buffer.append( amplitude * math.sin(signal_freq_rad * sample_time + phase) + dc_offset )
    sample_time += 1/sampling_freq_rad
    time_buffer.append(sample_time)
    


# plt.scatter(time_buffer, buffer)
plt.plot(time_buffer, buffer)
plt.plot(time_buffer, [average(buffer)] * buffer_len)
plt.show()

