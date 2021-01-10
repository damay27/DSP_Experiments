
import math
from matplotlib import pyplot as plt

#I want to generate a some what complicated functin for filtering
def input_signal(sample_time):

    #########################################
    #Signal parameters 
    #########################################
    signal_freq_15 = 15 #Hz
    signal_freq_15_rad = (signal_freq_15) * 2 * math.pi #radians/second
    phase_15 = math.pi #seconds
    dc_offset_15 = 4.0
    amplitude_15 = 1.5

    signal_freq_2 = 2 #Hz
    signal_freq_2_rad = (signal_freq_2) * 2 * math.pi #radians/second
    phase_2 = .5 * math.pi #seconds
    dc_offset_2 = 1.0
    amplitude_2 = 2.0

    signal_freq_5 = 5 #Hz
    signal_freq_5_rad = (signal_freq_5) * 2 * math.pi #radians/second
    phase_5 = 0.0 #seconds
    dc_offset_5 = 0.0
    amplitude_5 = 1.0

    value = 0
    value += amplitude_15 * math.sin(2 * math.pi * signal_freq_15 * sample_time + phase_15) + dc_offset_15
    value += amplitude_2 * math.sin(2 * math.pi * signal_freq_2 * sample_time + phase_2) + dc_offset_2
    value += amplitude_5 * math.sin(2 * math.pi * signal_freq_5 * sample_time + phase_5) + dc_offset_5

    return value


def sinc(freq, sample_time):
    if(sample_time == 0):
        return 0
    sinc = ( math.sin(math.pi * freq * sample_time) ) / (math.pi * freq * sample_time)
    return sinc

def blackman_window(sample_time, window_size):
    blackman_A = .5 * math.cos( (2 * math.pi * sample_time)/(window_size - 1) )
    blackman_B = .08 * math.cos( (4 * math.pi * sample_time) / (window_size -1) )
    blackman_window = .42 - blackman_A + blackman_B
    return blackman_window

def filter_convolve(filter, signal):
    
    output = []
    filter_len = len(filter)
    signal_len = len(signal)

    filter_sum = 0
    for x in range(filter_len):
        filter_sum += filter[x]

    #NOTE: This cuts off the first N points where the N is equal to the lenght of the filter
    #This resolves the issues with there initially not being enough points to run the entire filter
    for i in range(filter_len, signal_len):
        sum = 0
        for j in range(filter_len):
            sum += filter[j] * signal[i - j]
        output.append(sum / filter_sum)
    return output

#The frequency at which the signal is sampled
signal_sampling_freq = 500 #Hz
#Amount of time to capture for in seconds
capture_time = 6 #second

#Use the sampling frequence and amount of time beign captured for
#to determine how long the buffer needs to be
buffer_len = math.ceil(capture_time * signal_sampling_freq)
print(buffer_len)
signal_buffer = []
time_buffer = []

sample_time = 0
# for i in range(buffer_len):
# for i in range(-int(buffer_len/2), int(buffer_len/2)):
for i in range(buffer_len):
    signal_buffer.append( input_signal(sample_time) )
    sample_time = i * 1/signal_sampling_freq
    time_buffer.append(sample_time)



filter_buffer = []
filter_point_count = 500
filter_sampling_freq = 500

blackman_window_buffer = []

#Sample the sinc function to generate the filter taps
for i in range(-int(filter_point_count/2), int(filter_point_count/2)):
    sample_time = i * 1/filter_sampling_freq
    filter_buffer.append(sinc(6, sample_time))

#Multiply the sinc function with the blackman window values
for i in range(filter_point_count):
    filter_buffer[i] = filter_buffer[i] * blackman_window(i, filter_point_count)


# plt.plot(range(filter_point_count), filter_buffer)
plt.plot(time_buffer[len(filter_buffer):], signal_buffer[len(filter_buffer):])
plt.plot(time_buffer[len(filter_buffer):], filter_convolve(filter_buffer, signal_buffer))
plt.show()