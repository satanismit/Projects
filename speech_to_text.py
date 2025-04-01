import speech_recognition as sr
# record audio and return it as a string
def speech_to_text():
    # print("say anything :")
    # Initialize recognizer
    r=sr.Recognizer()

    # Use microphone as source for input
    with sr.Microphone() as source:
        # print("Say something")
        audio=r.listen(source)
        print("Time over, thanks")
        try:
            voice_data=""
            voice_data=r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Request error")  
        








