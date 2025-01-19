def compareResult(transcribedAudio, correctAnswer):    
  if(transcribedAudio.strip() == correctAnswer):
      print("You speaked correctly!")
  else:
      print("You pronounced incorrectly, your answer: " + transcribedAudio)