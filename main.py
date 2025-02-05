import eel
import whisper
from generateNumbers import generateNumbers
from recordAudio import recordAudio
from compareNumbers import compareNumbers

#EEL config
eel.init('static_web_folder')

@eel.expose
def loadWhisperModel():
  global model
  model = whisper.load_model('base.en')
  modelLoaded()
  return model



@eel.expose
def recordProcess():

  randomNumbers = generateNumbers()
  print(randomNumbers)
  eel.recordingSign(randomNumbers)
  userAudioFile = recordAudio(10)
  #Use Whipser to transcribe Audio
  transcribedAudio = model.transcribe(userAudioFile)
  compareNumbers(transcribedAudio['text'], randomNumbers)
  
  continueQuestion = input("Quer tentar novamente? (S/N)")
  
  if(continueQuestion.upper() == 'S'):
    recordProcess()


@eel.expose
def modelLoaded():
  eel.modelLoaded()
  eel.removeLoadingModal()
  print('MODELO CARREGADO!')

eel.start('main.html')