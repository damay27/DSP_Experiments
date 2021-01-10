import math
from matplotlib import pyplot as plt
import pdb

def DFT(buffer, start_freq, end_freq):
    output_buffer = []
    N = len(buffer)
    
    #Loop through all of the frequencies in 1 Hz steps
    for k in range(start_freq, end_freq + 1):
        freq_content = 0
        sine_part = 0
        cosine_part = 0
        for n in range(N):
            inner_val = (2 * math.pi * k * n) / N
            sine_part += buffer[n] * math.sin(inner_val)
            cosine_part += buffer[n] * math.cos(inner_val)
            # freq_content += math.sqrt( (sine_part ** 2) + (cosine_part ** 2) )
            print(k)
            print(n)
            print(N)
            print(inner_val)
            print(sine_part)
            print(cosine_part)
            print(freq_content)
            # pdb.set_trace()
            # input()
        # print(k)
        # print(freq_content)
        # input()
        # output_buffer.append(freq_content)
        output_buffer.append(math.sqrt( (sine_part ** 2) + (cosine_part ** 2) ) / N)


    return output_buffer


##############################################
# Control values for the test signal
##############################################
signal_freq = 1 #Hz
signal_freq_rad = (signal_freq) * 2 * math.pi #60Hz in radians/second
phase = 0.0 #seconds
dc_offset = 0.0
amplitude = 1.0

signal_freq2 = 5 #Hz
signal_freq_rad2 = (signal_freq2) * 2 * math.pi #60Hz in radians/second
phase2 = math.pi #seconds
dc_offset2 = 0.0
amplitude2 = 1.0

#Used to record signal values
buffer = []
#Used to record sampling time indices
time_buffer = []

#The frequency at which the signal is sampled
sampling_freq = 8 #Hz
sampling_freq_rad = sampling_freq * 2 * math.pi
#Amount of time to capture for in seconds
capture_time = 1 #second

#Use the sampling frequence and amount of time beign captured for
#to determine how long the buffer needs to be
buffer_len = math.ceil(sampling_freq_rad * capture_time)

sample_time = 0
for i in range(buffer_len):
    x = amplitude * math.sin(signal_freq_rad * sample_time + phase) + dc_offset + amplitude2 * math.sin(signal_freq_rad2 * sample_time + phase2) + dc_offset2
    buffer.append( x )
    sample_time += 1/sampling_freq_rad
    time_buffer.append(sample_time)
    
print(buffer)
# plt.plot(time_buffer, buffer)
plt.scatter(range(1, sampling_freq+1), DFT(buffer, 1, sampling_freq))
# print(DFT(buffer, 1, sampling_freq))
plt.show()

