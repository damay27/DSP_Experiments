#include <stdio.h>
#include <math.h>
#include <stdint.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define PI 3.14159265
#define SAMPLE_COUNT 1024
#define STEP_SIZE 360.0f / SAMPLE_COUNT

uint32_t float_to_fixed_16_16(float value) {
    return (uint32_t) (value * (1<<16));
}

//Program for generating look up table values in 16:16 fixed point format

int main() {

    FILE * key_file = fopen("./sine_key_lut.mem", "w");
    FILE * value_file = fopen("./sine_value_lut.mem", "w");

    printf("Fixed point step size: %d\n", float_to_fixed_16_16(STEP_SIZE));

    for(int i = 0; i < SAMPLE_COUNT; i++) {
        float x = i * STEP_SIZE;
        float sample = sin( (PI/180.0) * x );
        fprintf(key_file, "%04x\n", float_to_fixed_16_16(x));
        fprintf(value_file, "%04x\n", float_to_fixed_16_16(sample));
    }

    fclose(key_file);
    fclose(value_file);
}