import whisper
from generateNumbers import generateNumbers
from recordAudio import recordAudio
from compareNumbers import compareNumbers
#WHISPER config
model = whisper.load_model('base.en')

#Record and Save Audio
randomNumbers = generateNumbers()
print(randomNumbers)
print("Recording...")

#Use Whipser to transcribe Audio
userAudioFile = recordAudio(10)
transcribedAudio = model.transcribe(userAudioFile)

compareNumbers(transcribedAudio['text'], randomNumbers)



