import math
import wave
import struct
import os


def SettingFileName(file_name):
    if file_name[-4:] != ".wav":
        file_name = file_name + ".wav"
    if os.path.isfile(file_name):
        try:
            os.remove(file_name)
        except PermissionError:
            print(f"File '{file_name}' is being used by another program. No permission.'")
    return file_name

"""def creatingFrequencyWithOctaves(frate, data_size, freq_1=0, freq_2=0, num_of_octaves_1=1, num_of_octaves_2=1):
    octave_list_1 = []
    for i in range(0, num_of_octaves_1):
        octave_list_1.append(i + 1)
    octave_list_2 = []
    for i in range(0, num_of_octaves_2):
        octave_list_2.append(i + 1)
    sine_list_x = []
    sine_list_y = []
    sine_out_1 = 0
    sine_out_2 = 0
    for x in range(data_size):
        for i in octave_list_1:
            sine_out_1 = sine_out_1 + math.sin(2*math.pi*freq_1*i*(x/frate))
        for i in octave_list_2:
            sine_out_1 = sine_out_2 + math.sin(2*math.pi*freq_2*i*(x/frate))
        sine_list_x.append(sine_out_1)
        sine_list_y.append(sine_out_2)
    sin_values_tuple = (sine_list_x, sine_list_y)
    return sin_values_tuple"""

def creatingFrequencyWithOctaves(frate, data_size, freq_1=0, freq_2=0):    
    sine_list_x = []
    sine_list_y = []
    sine_out_1 = 0
    sine_out_2 = 0
    for x in range(data_size):
        sine_out_1 = math.sin(2*math.pi*freq_1*(x/frate))
        sine_out_2 = math.sin(2*math.pi*freq_2*(x/frate))
        sine_list_x.append(sine_out_1)
        sine_list_y.append(sine_out_2)
    sin_values_tuple = (sine_list_x, sine_list_y)
    return sin_values_tuple

def fun(specs):
    frate = 44100.0 # framerate as a float
    data_size = int(frate) * int(specs[3])
    amp = 64000.0     # multiplier for amplitude
    print(specs)
    fname = SettingFileName(specs[0])
    freq_1 = int(specs[1])
    freq_2 = int(specs[2])
    print(f"{freq_1} -- {freq_2}")

    octaves_1 = 2
    octaves_2 = 2

    sinus = creatingFrequencyWithOctaves(frate, data_size, freq_1=freq_1, freq_2=freq_2)
    print(str(sinus[0][101]))
    

    """sine_list_x = []
    for x in range(data_size):
        sine_list_x.append(sinus_1 + sinus_2)"""

    wav_file = wave.open(fname, "w")

    nchannels = 2
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"

    wav_file.setparams((nchannels, sampwidth, framerate, nframes,
        comptype, compname))

    for s, z in zip(sinus[0], sinus[1]):
        # write the audio frames to file
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
        wav_file.writeframes(struct.pack('h', int(z*amp/2)))

    wav_file.close()