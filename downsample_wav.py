#!/usr/bin/env python3

import librosa
import os

"""
Testing LJS Resample
--------------------

+ (python) bt@halide:~/dev/voice-tools$ aplay test_input.wav
Playing WAVE 'test_input.wav'
    : Signed 16 bit Little Endian, Rate 22050 Hz, Mono

+ (python) bt@halide:~/dev/voice-tools$ aplay test_output.wav
Playing WAVE 'test_output.wav'
    : Float 32 bit Little Endian, Rate 16000 Hz, Mono


Signed 16 bit --> Float 32 bit

WaveRNN
-------

aplay model_outputs/mel-northandsouth_52_f000076.wav
Playing WAVE 'model_outputs/mel-northandsouth_52_f000076.wav'
    : Float 32 bit Little Endian, Rate 16000 Hz, Mono

aplay model_outputs/mel-LJ001-0109.npy_orig.wav
Playing WAVE 'model_outputs/mel-LJ001-0109.npy_orig.wav'
    : Float 32 bit Little Endian, Rate 22050 Hz, Mono

Everything in ML is Float 32 bit?

"""

OUTPUT_RATE = 16000

def resample_file(input_filename, output_filename, sample_rate):
    mono = True # librosa converts signal to mono by default, so I'm just surfacing this
    audio, _rate = librosa.load(input_filename, sr=sample_rate, mono=mono)
    librosa.output.write_wav(output_filename, audio, sr=sample_rate)

output_dir = '/home/bt/dev/voice-tools/temp'
input_dir = '/home/bt/dev/2nd/Tacotron-2/LJSpeech-1.1/wavs/'

for name in os.listdir(input_dir):
    input_filename = os.path.join(input_dir, name)

    if not os.path.isfile(input_filename) \
            or not name.endswith(".wav"):
        continue

    output_filename = os.path.join(output_dir, name)

    resample_file(input_filename, output_filename, OUTPUT_RATE)
    print(name)

