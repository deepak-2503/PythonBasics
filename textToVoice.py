# text to voice changer

import pyttsx3
engine = pyttsx3.init()
engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
''')
engine.runAndWait()