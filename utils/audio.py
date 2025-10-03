from pydub import AudioSegment
import os
#how to hash the input file to create a unique temp file name
import hashlib
from hashlib import sha256
from datetime import datetime

def hash_file(file_path):
    now = str(datetime.now())
    encoded = sha256((now + file_path).encode('utf-8')).hexdigest()
    return encoded



def convert_audio(input_path, output_format):
    output_path = input_path.split('.')[-1]
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=output_format)
    return output_path

def merge_audios(audio_paths):
    combined = AudioSegment.empty()
    for path in audio_paths:
        audio = AudioSegment.from_file(path)
        combined += audio
    combined.export(output_path, format="mp3")
    return output_path

def trim_audio(input_path, output_path, start_ms, end_ms):
    audio = AudioSegment.from_file(input_path)
    trimmed = audio[start_ms:end_ms]
    trimmed.export(output_path, format="mp3")
    return output_path

def cut_audio(input_path, output_path, cut_start_ms, cut_end_ms):
    audio = AudioSegment.from_file(input_path)
    cut_audio = audio[:cut_start_ms] + audio[cut_end_ms:]
    cut_audio.export(output_path, format="mp3")
    return output_path

def reverse_audio(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    reversed_audio = audio.reverse()
    reversed_audio.export(output_path, format="mp3")
    return output_path



