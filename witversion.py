import speech_recognition as sr
from wit import Wit
import json
from operations import *
import wikipedia
import win32api
import win32gui
from pynput import keyboard
from threading import Thread

WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

hwnd_active = win32gui.GetForegroundWindow()

def mic_toggler():
    def on_press(key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys

        if k in ['1', '2', 'left', 'right', 'space']:  # keys of interest

            # self.keys.append(k)  # store it in global-like variable
            print('Key pressed: ' + k)
            win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
            # return False  # stop listener; remove this if want more keys

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    print("Started listening for keyboard interrupt for mic toggling")
    listener.join()  # remove if main thread is polling self.keys

Thread(target=mic_toggler).start()

# Initialize listener instance
listener = sr.Recognizer()

# Initialize text to speach engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # Female Voice is given
engine.setProperty('rate', 170)     # setting up speaking rate


# Speaks the text passed to it
def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Athena is initializing")

# Creates an nlp_client instance to get curated data from text data
nlp_client = Wit("K32COVD3O2X6JM7O3DIIA5RLN3Q7PKCC")


def get_wit_response(command):
    wit_response = nlp_client.message(command)
    json_string = str(wit_response).replace("'", '"').replace("True", "true")
    json_data = json.loads(json_string)
    print("####################################")
    beautified_json_string = json.dumps(json_data, indent=4)
    print(beautified_json_string)
    print("####################################")
    return json_data

c=0
# Returns the voice command as text
def take_command():
    global c
    try:
        # Listens for speach and when it recognizes, it creates an audio file of the speach
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=3)
            if c == 0:
                talk("Initialization Complete. listening.")
                c += 1
            print("Listening ...")
            audio_file = listener.listen(source=source)
            print("Voice Heard")

            # Gets text from the audio file using google recognizer
            try:
                command = listener.recognize_google(audio_file)
                print("Google Speech Recognition results: " + command)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                command = "notaspeach"
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                command = "notaspeach"

    # Handles exception that could arise from the listener instance
    except Exception as e:
        print("execption occured")
        print(e)
        command = "notaspeach"

    # Returns text command
    return command


def run_bot():
    command = take_command()
    if command == "notaspeach":
        pass
    else:
        json_data = get_wit_response(command)
        intent = json_data["intents"][0]["name"]
        print(intent, type(intent))
        try:
            print(mapping[intent])
            mapping[intent]()
        except:
            try:
                data = json_data["entities"]["item:item"][0]["value"]
                mapping[intent](data)
            except:
                print("the intend funtion does not exist")


while True:
    run_bot()






#
# resp = nlp_client.message('who is barak obama ?')
# json_data = str(resp).replace("'",'"').replace("True", "true")
# # print(json_data)
# obj = json.loads(json_data)
# print(obj)
# print(type(obj))
# print("####################################")
#
#
# formated_data = json.dumps(obj, indent=4)
# print(formated_data)
#
# print(obj["intents"][0]["name"])







