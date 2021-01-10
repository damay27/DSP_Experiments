import math
from matplotlib import pyplot as plt

#This function causes the signal to be decimated by the block size
def block_average(buffer, block_size):
    block_index = 0
    output_buffer = []

    while(block_index < len(buffer)):
        stretch_factor = 0
        sum = 0
        for i in range(block_size):
            if(block_index + block_size >= len(buffer)):
                stretch_factor += 1
                break
            else:
                sum += buffer[block_index + block_size]
                stretch_factor += 1

        #We need to stretch the signal so that it matches the time scale of the input
        #signal
        output_buffer += [sum/len(buffer)] * stretch_factor
        block_index += block_size

    print(output_buffer)
    return output_buffer


##############################################
# Control values for the test signal
##############################################
signal_freq = 60 #Hz
signal_freq_rad = (signal_freq) * 2 * math.pi #60Hz in radians/second
phase = math.pi #seconds
dc_offset = 0.0
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
plt.plot(time_buffer, block_average(buffer, 15))
plt.show()

