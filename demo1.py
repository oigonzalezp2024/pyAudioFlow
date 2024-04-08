
from pyAudioFlow import PyAudioFlow

audio = PyAudioFlow()
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "./records/grabacion1.mp3"
audio.recordController(CHANNELS, RATE, CHUNK, RECORD_SECONDS, OUTPUT_FILENAME)
