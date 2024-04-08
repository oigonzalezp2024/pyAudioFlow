
import pyaudio
import wave

class PyAudioFlow(pyaudio.PyAudio):

    def recordController(self, CHANNELS, RATE, CHUNK, RECORD_SECONDS, OUTPUT_FILENAME):
        FORMAT = pyaudio.paInt16
        stream = self.recordConfig(FORMAT, CHANNELS, RATE, CHUNK)
        frames = self.recordStart(RATE, CHUNK, stream, RECORD_SECONDS)
        self.recordEnd(stream)
        self.recordSave(OUTPUT_FILENAME, CHANNELS, FORMAT, RATE, frames)

    def recordConfig(self, FORMAT, CHANNELS, RATE, CHUNK):
        stream = self.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )
        return stream

    def recordStart(self, RATE, CHUNK, stream, RECORD_SECONDS):
        print("Grabando...")
        frames = []
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        return frames

    def recordEnd(self, stream):
        print("¡Grabación terminada!")
        stream.stop_stream()
        stream.close()
        self.terminate()

    def recordSave(self, OUTPUT_FILENAME, CHANNELS, FORMAT, RATE, frames):
        with wave.open(OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        print(f"Audio guardado como '{OUTPUT_FILENAME}'")
