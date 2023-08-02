import speech_recognition as sr
import gtts
from playsound import playsound

r = sr.Recognizer()


def get_audio(file_name):
    with sr.AudioFile(file_name) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print("Saving...")
    return audio


def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        print("could not request results from API")
    return text


def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        temp_file = "./temp.mp3"
        tts.save(temp_file)
        playsound(temp_file)
    except AssertionError:
        print("could not play sound")

