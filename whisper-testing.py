import whisper



model = whisper.load_model('base.en')

#RECORD THE AUDIO

result = model.transcribe("number-test.mp3")

if(result["text"].strip() == "2056 12 18"):
    print("You speaked correctly!")
else:
    print("You pronounced incorrectly, correct answer: " + result["text"])
