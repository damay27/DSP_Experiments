import math
import ctypes

def float_to_fixed_16_16(f):
    return int(f * (1<<16) )

def fixed_16_16_to_float(f):
    return int(f / (1<<16) )

def interpolate(lut, value, step_size):

    #The table maxes out at 360 degrees so scale the input
    #to match this range.
    if(value > 360):
        value %= 360

    #Find the table entries that map to the input value
    index = 0
    while index < len(lut) - 2:

        if value >= list(lut.keys())[index] and value < list(lut.keys())[index + 1]:
            break
        index += 1



    ###############################################################
    #Linear interpolation
    ###############################################################

    x0 = list(lut.keys())[index]
    x1 = list(lut.keys())[index + 1]

    y0 = list(lut.values())[index]
    y1 = list(lut.values())[index + 1]

    slope = (y1 - y0) / (x1 - x0)
    
    y_intercept = y0 - slope * x0

    y_interpolate = slope * value + y_intercept

    return y_interpolate

point_count = 1024

step_size = 360/point_count

position = 0.0

lut = {}

#Generate the lookup table
for i in range(point_count):
    # lut[float_to_fixed_16_16(position)] = float_to_fixed_16_16(math.sin(math.radians(position)))
    lut[position] = math.sin(math.radians(position))
    position += step_size

error = []

degree_step = .1

for i in range(0, int( 360 / degree_step) ):
    x = degree_step * i
    exact = math.sin(math.radians(x))
    interpolate_val = interpolate(lut, x, step_size)
    diff = abs(exact - interpolate_val)

    #Keep track of the error between the interpolated value and the computed value
    error.append(diff)


print("Highest error: %f" % max(error))