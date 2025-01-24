import eel
import whisper
from generateNumbers import generateNumbers
from recordAudio import recordAudio
from compareNumbers import compareNumbers

#WHISPER config

#Record and Save Audio
@eel.expose
def recordProcess():
  model = whisper.load_model('base.en')
  
  randomNumbers = generateNumbers()
  print(randomNumbers)
  print("Recording...")
  userAudioFile = recordAudio(10)
  #Use Whipser to transcribe Audio
  transcribedAudio = model.transcribe(userAudioFile)
  compareNumbers(transcribedAudio['text'], randomNumbers)
  
  continueQuestion = input("Quer tentat novamente? (S/N)")
  
  if(continueQuestion.upper() == 'S'):
    recordProcess()

