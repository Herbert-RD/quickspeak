import sounddevice as sd
from scipy.io.wavfile import write


sd.default.samplerate = 44100
sd.default.channels = 2

print("Recording...")
myaudio = sd.rec(int(3 * sd.default.samplerate))


sd.wait()
write("sounddevice-audio.wav", 44100, myaudio)