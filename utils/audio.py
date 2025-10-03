from pydub import AudioSegment
import os

from hashlib import sha256
from datetime import datetime

def hash_file(file_path):
    now = str(datetime.now())
    encoded = sha256((now + file_path).encode('utf-8')).hexdigest()
    return encoded



def convert_audio(input_path, output_format):
    input_format = input_path.split('.')[-1]
    output_path = "static/audio/output/"+ hash_file(input_path) + "." + output_format   
    audio = AudioSegment.from_file(input_path,format=input_format)
    audio.export(output_path, format=output_format)
    return output_path

def merge_audios(audio_paths):
    input_format = audio_paths[0].split('.')[-1]
    output_path = "static/audio/output/"+ hash_file("".join(audio_paths)) + "." + input_format
    combined = AudioSegment.empty()
    for path in audio_paths:
        audio = AudioSegment.from_file(path, format=input_format)
        combined += audio
    combined.export(output_path, format=input_format)
    return output_path

def trim_audio(input_path, start_ms, end_ms):
    input_format = input_path.split('.')[-1]
    output_path = "static/audio/output/"+ hash_file(input_path) + "."+input_format
    audio = AudioSegment.from_file(input_path)
    trimmed = audio[start_ms:end_ms]
    trimmed.export(output_path, format=input_format)
    return output_path

def cut_audio(input_path, cut_start_ms, cut_end_ms):
    input_format = input_path.split('.')[-1]
    output_path = "static/audio/output/"+ hash_file(input_path + str(cut_start_ms) + str(cut_end_ms)) + "."+input_format
    audio = AudioSegment.from_file(input_path)
    cut_audio = audio[:cut_start_ms] + audio[cut_end_ms:]
    cut_audio.export(output_path, format=input_format)
    return output_path

def reverse_audio(input_path):
    input_format = input_path.split('.')[-1]
    output_path = "static/audio/output/"+ hash_file(input_path) + "."+input_format
    audio = AudioSegment.from_file(input_path)
    reversed_audio = audio.reverse()
    reversed_audio.export(output_path, format=input_format)
    return output_path

def fade_audio(input_path, fade_in_ms, fade_out_ms):
    input_format = input_path.split('.')[-1]
    output_path = "static/audio/output/" + hash_file(input_path ) + "." + input_format
    audio = AudioSegment.from_file(input_path)
    faded = audio.fade_in(fade_in_ms).fade_out(fade_out_ms)
    faded.export(output_path, format=input_format)
    return output_path

def volume_adjuster(input_path, change_volume):
    input_format = input_path.split('.')[-1]
    output_path = "static/audio/output/"+ hash_file(input_path ) + "."+input_format
    audio = AudioSegment.from_file(input_path)
    adjusted_audio = audio + change_volume
    adjusted_audio.export(output_path, format=input_format)
    return output_path




