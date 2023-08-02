from record_sound import record
from audio_to_text import *
from save_to_docx import write_docx
import os

duration = float(input("Enter class time(in min):"))
duration = duration * 60
play_sound("Recording is started...")
record(duration)
a = get_audio("./recording.wav")
txt = audio_to_text(a)
play_sound("Done, Saving the file.")
# if ACTIVATION_COMMAND in txt.lower():
# play_sound("Start Talking, I am listening")
# note = get_audio()
# note = audio_to_text(note)
write_docx(txt)
print(txt)
