import pyaudio
import wave

class AudioRecorder:
    def __init__(self, file_name="output.wav", duration=5):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.file_name = file_name
        self.duration = duration

    def record_audio(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("Recording...")

        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.duration)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("Finished recording!")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self.file_name, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

class MicrophoneRecorder(AudioRecorder):
    def __init__(self, file_name="output.wav", duration=5, microphone_index=0):
        super().__init__(file_name, duration)
        self.microphone_index = microphone_index

    def record_audio(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK,
                        input_device_index=self.microphone_index)

        print(f"Recording from microphone {self.microphone_index}...")

        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.duration)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("Finished recording!")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self.file_name, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

# Приклад використання класу MicrophoneRecorder
microphone_recorder = MicrophoneRecorder(file_name="microphone_output.wav", duration=5, microphone_index=1)
microphone_recorder.record_audio()
