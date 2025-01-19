def compareNumbers(transcribedAudio, correctAnswer):    
    
    transcribedAudio = transcribedAudio.strip()
    transcribedAudioList = ['nothing']

    #removes commas and other stuff and then transforms it in a list.
    if(transcribedAudio.count(" ") >= 1): 
        removeItemsList = [',', '.', '/', '-']
        for x in removeItemsList:
            transcribedAudio = transcribedAudio.replace(x, "")
        transcribedAudioList = transcribedAudio.split(" ", -1)

    elif(transcribedAudio.count("-") >= 1):
        transcribedAudioList = transcribedAudio.split("-", -1)


    if(transcribedAudioList == correctAnswer):
        print("You spoke correctly!")
        print(transcribedAudioList)
        print(correctAnswer)
    else:
        print("You pronounced incorrectly, your answer: " + transcribedAudio)
        print(transcribedAudioList)
        print(correctAnswer)


