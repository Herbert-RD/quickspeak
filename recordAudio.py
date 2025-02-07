import sounddevice as sd
from scipy.io import wavfile
import eel


def recordAudio(audioDuration = 8):  
  #SOUNDDEVICE config
  sd.default.samplerate = 44100
  sd.default.channels = 2
  userAudioFile = "userAudio.wav"

  userAudio = sd.rec(int(audioDuration * sd.default.samplerate))
  sd.wait()

  wavfile.write(userAudioFile, 44100, userAudio)
  eel.comparingNumbers()
  return userAudioFile