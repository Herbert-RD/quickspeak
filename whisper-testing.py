import whisper
import sounddevice as sd
from scipy.io.wavfile import write 
from random import randrange




#SOUNDDEVICE config
sd.default.samplerate = 44100
sd.default.channels = 2
audioDuration = 8
userAudioFile = "userAudio.wav"


#Random number generator

#WHISPER config
model = whisper.load_model('base.en')

#Record and Save Audio
print("Recording...")
userAudio = sd.rec(int(audioDuration * sd.default.samplerate))
sd.wait()

write(userAudioFile, 44100, userAudio)


result = model.transcribe(userAudioFile)

#Compare result
if(result["text"].strip() == "2056 12 18"):
    print("You speaked correctly!")
else:
    print("You pronounced incorrectly, your answer: " + result["text"])

