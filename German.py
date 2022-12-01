from gtts import gTTS
import os
text = "I think of German attitude as humorous but in a dark manner"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")
