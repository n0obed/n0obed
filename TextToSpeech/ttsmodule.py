import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate') # 200
engine.setProperty('rate', 125)


def speak(txt, vol):
    vol = float(vol)/10
    global engine
    engine.stop()
    engine.setProperty('rate', 125)
    print('speaking...')
    engine.setProperty('volume',vol)
    engine.say(txt)
    engine.runAndWait()
    print('Complete.')

def rate(y=125):
    global engine
    engine.setProperty('rate', y) 
    print('rate set to {0}'.format(y) )


'''engine.say('hello there area oaei ok wait o know idk')
engine.runAndWait()
engine.setProperty('volume',0.5)

engine.say('hello there area oaei ok wait o know idk',1)
engine.runAndWait()'''