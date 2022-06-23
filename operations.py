import pyttsx3
import pywhatkit
import datetime
import pyjokes




# Initialize text to speach engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # Female Voice is given
engine.setProperty('rate', 170)     # setting up speaking rate


# Speaks the text passed to it
def talk(text):
    engine.say(text)
    engine.runAndWait()

def play(song):
    talk('playing ' + song)
    pywhatkit.playonyt(song)


def hello():
    talk("hello")

def time_tell():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)

def tell_joke():
    talk(pyjokes.get_joke())

def tell_data(data):
    talk(f"{data}")


mapping = {
    # "greeting": lambda: hello(),
    "greeting": hello,
    "wit$get_time": time_tell,
    "joke": tell_joke,
    "data": tell_data,
    "play_youtube": play
}