import eel

#EEL config
eel.init('static_web_folder')

@eel.expose
def helloFunc():
    print('hello world')

eel.start('main.html')