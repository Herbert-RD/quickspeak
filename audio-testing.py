import sounddevice as sd

#git testing

sd.default.samplerate = 44100
sd.default.channels = 2

myaudio = sd.rec(int(3 * sd.default.samplerate))

sd.wait()

print(myaudio)