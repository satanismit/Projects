import webbrowser
import text_to_speech as tts,speech_to_text as stt
import datetime
import weather

def Action(data):  
        user_data=data.lower()

        if "what is your name" in user_data:
            tts.text_to_speech("My name is Virtual Assistant")
            return "My name is Virtual Assistant"
        
        elif "hello" in user_data:
            tts.text_to_speech("Hello Smit, How can I help you?")
            return "Hello Smit, How can I help you?"
        
        elif "how are you" in user_data:
            tts.text_to_speech("I am fine, thank you")
            return "I am fine, thank you"
        
        elif "time" in user_data:
            time=datetime.datetime.now().strftime("%I:%M %p")
            tts.text_to_speech("The time is "+time)
            return "The time is "+time
        
        elif "date" in user_data:
            date=datetime.datetime.now().strftime("%d %B %Y")
            tts.text_to_speech("Today's date is "+date)
            return "Today's date is "+date
        
        elif "good morning" in user_data:
            tts.text_to_speech("Very Good Morning, Smit")
            return "Very Good Morning, Smit"

        elif "shutdown" in user_data:
            tts.text_to_speech("Shutting down")
            return "Shutting down"
            
        elif "youtube" in user_data:
            webbrowser.open("https://www.youtube.com/")
            tts.text_to_speech(" Youtube is ready for you")
            return "Youtube is ready for you"
        
        elif "music" in user_data:
            webbrowser.open("https://open.spotify.com/")
            tts.text_to_speech("Spotify is ready for you, enjoy!!")
            return "Spotify is ready for you, enjoy!!"

        elif "google" in user_data:
            webbrowser.open("https://www.google.com")
            tts.text_to_speech("Google is ready for you")
            return "Google is ready for you"
        
        # elif "weather" in user_data:
        #     tts.text_to_speech(weather.weather())
        #     return weather.weather()
        
        elif "movie" in user_data or "movies" in user_data:
            webbrowser.open("https://hdhub4u.pub/")
            tts.text_to_speech("site is ready for you")
            return "site is ready for you"

        else:
            tts.text_to_speech("Sorry, I am not able to understand you")
            return "Sorry, I am not able to understand you"


