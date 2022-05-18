import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
# recognizer.energy_threshold = 100

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Start Talking")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio_text = recognizer.listen(source)
    print("Time over, thank you")

    try:
        print("Text: " + recognizer.recognize_google(audio_text))

    except:
        print("Sorry, I did not get that")