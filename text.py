import speech_recognition as sr
from pydub import AudioSegment
import os
from hashlib import sha256
from datetime import datetime
import pyttsx3

def hash_file(file_path):
    now = str(datetime.now())
    encoded = sha256((now + file_path).encode('utf-8')).hexdigest()
    return encoded

def audio_to_text(file_path):
    recognizer = sr.Recognizer()
    
    # Convert to WAV (required by speech_recognition)
    sound = AudioSegment.from_file(file_path)
    sound.export("temp.wav", format="wav")

    # Recognize speech
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            text = "Could not understand audio"
        except sr.RequestError as e:
            text = f"API error: {e}"

    os.remove("temp.wav")
    return text

def text_to_speech(text):
    output_path = "static/audio/output/" + hash_file(text) + ".mp3"    
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path


text_to_speech("Hello, this is a test.")


audio_to_text("static/audio/output/b6c858be35ce35110112b46855e0bde008ebea537ab4cd795bf78deec9ecc325.mp3")    