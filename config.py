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

def createOutputDirectory():
    while os.getcwd()[-12:] == "Output files":
        os.chdir('..')
    if not os.path.exists("Output files"):
        os.makedirs("Output files")
    os.chdir("Output files")

def creatingFrequencyLists(frate, data_size, freq_1=0, freq_2=0):    
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

def runApp(specs):
    print(os.getcwd())
    createOutputDirectory()

    # Configuration
    frate = 44100.0                             # framerate as a float
    data_size = int(frate) * int(specs['time'])
    amp = 64000.0                               # multiplier for amplitude
    fname = SettingFileName(specs['filename'])
    freq_1 = int(specs['freq_1'])
    freq_2 = int(specs['freq_2'])

    print(f"Output file '{fname}' in directory" + "'" + os.getcwd() + "'")
    print(f"Left channel frequency: {freq_1}Hz\nRight channel frequency: {freq_2}Hz")

    sinus = creatingFrequencyLists(frate, data_size, freq_1=freq_1, freq_2=freq_2)
    
    wav_file = wave.open(fname, "w")

    # Setting parameters of *.wav file
    nchannels = 2
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"

    wav_file.setparams((nchannels, sampwidth, framerate, nframes,
        comptype, compname))

    for s, z in zip(sinus[0], sinus[1]):
        # writing the audio frames to file
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
        wav_file.writeframes(struct.pack('h', int(z*amp/2)))

    wav_file.close()



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