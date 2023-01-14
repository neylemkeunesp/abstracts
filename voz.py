import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.eloquence.pt-BR.Luciana')
engine.say('Pedro viu a uva')
engine.save_to_file('Pedro viu a uva. Joana viu a pera.','test.mp3')
engine.runAndWait()