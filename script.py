from gtts import gTTS
import os
gtt = gTTS(text='Anjali start studying', lang='en')
gtt.save("scripting2.mp3")
os.system("mpg321 scripting2.mp3")
