from gtts import gTTS

tts = gTTS('This is an example of emphasizing a word', lang='en')
tts.save('example.mp3')

tts = gTTS('This is an example of emphasizing a word', lang='en', emphasis=2)
tts.save('example_emphasis.mp3')
