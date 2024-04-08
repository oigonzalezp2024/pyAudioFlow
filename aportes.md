
# Ejemplo de uso de la librería Pyaudio,  por Oscar Fernandez:

<pre>
import pyaudio
import wave

# Configura los parámetros de la grabación
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "grabacion.wav"

# Inicializa PyAudio
audio = pyaudio.PyAudio()

# Abre el flujo de audio para la captura
stream = audio.open(format=FORMAT, channels=CHANNELS,
rate=RATE, input=True,
frames_per_buffer=CHUNK)

print("Grabando...")

frames = []

# Captura datos de audio
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
data = stream.read(CHUNK)
frames.append(data)

print("¡Grabación terminada!")

# Cierra el flujo de audio
stream.stop_stream()
stream.close()
audio.terminate()

# Guarda los datos de audio en un archivo WAV
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))

print(f"Audio guardado como '{OUTPUT_FILENAME}'")
</pre>

fuente:  
https://codigospython.com/capturando-y-manipulando-audio-con-pyaudio-en-python/
