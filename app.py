from pydub import AudioSegment
sound1 = AudioSegment.from_file("static/audio/sound1.mp3", format="mp3")
sound2 = AudioSegment.from_file("static/audio/sound2.mp3", format="mp3")


# sound1 6 dB louder, then 3.5 dB quieter
louder = sound1 + 6
quieter = sound1 - 3.5

# sound1, with sound2 appended
combined = sound1 + sound2
combined.export("combined_2.mp3", format="mp3")

# sound1 repeated 3 times
repeated = sound1 * 3

# duration
duration_in_milliseconds = len(sound1)

# first 5 seconds of sound1
beginning = sound1[:5000]

# last 5 seconds of sound1
end = sound1[-5000:]

# split sound1 in 5-second slices
slices = sound1[::5000]
