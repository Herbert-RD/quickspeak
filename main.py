import whisper
import sounddevice as sd
from scipy.io.wavfile import write 
from random import randrange
from generateNumbers import generateNumbers
from recordAudio import recordAudio

#WHISPER config
model = whisper.load_model('base.en')

#Record and Save Audio
randomNumbers = generateNumbers()
print(randomNumbers)
print("Recording...")

userAudioFile = recordAudio()

transcribedAudio = model.transcribe(userAudioFile)

#Compare result
if(transcribedAudio["text"].strip() == randomNumbers):
    print("You speaked correctly!")
else:
    print("You pronounced incorrectly, your answer: " + transcribedAudio["text"])

