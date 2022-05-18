import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Start Talking")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio_text = recognizer.listen(source)
    print("Time over, thank you")

    try:
        # using google speech recognition
        # print("Text without google recognizer: " + audio_text)
        print("Text: " + recognizer.recognize_google(audio_text))
        # print("Text: " + recognizer.recognize_houndify(audio_text))
        # print("Text: " + recognizer.recognize_ibm(audio_text))
        # print("Text: " + recognizer.recognize_google_cloud(audio_text))
        # print("Text: " + recognizer.recognize_sphinx(audio_text))
    except:
        print("Sorry, I did not get that")