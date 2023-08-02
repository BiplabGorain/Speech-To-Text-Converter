import sounddevice as sd
import wavio as wv


def record(sec):
    freq = 44100

    duration = sec
    print("Recording...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()

    wv.write("recording.wav", recording, freq, sampwidth=2)

    print("Done.")
