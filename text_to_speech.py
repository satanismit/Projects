import pyttsx3

def text_to_speech(text):
    # Initialize the engine
    engine=pyttsx3.init()
    rate=engine.getProperty('rate') # getting details of current speaking rate
    # SETTING THE RATE
    engine.setProperty('rate','rate-20')
    engine.say(text)
    engine.runAndWait()
 
