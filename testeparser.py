import argparse
from gtts import gTTS
import os

# Cria um parser
parser = argparse.ArgumentParser()

# Adiciona um argumento opcional '--mensagem'
parser.add_argument('--file', help='arquivo a ser transformado em voz')
parser.add_argument('--say', help='reproduz o som')
parser.add_argument('--language', help='reproduz o som')

# Analisa os argumentos da linha de comando
args = parser.parse_args()

# Imprime a mensagem, se foi passada
if args.file:
    filename=args.file
    with open(filename, 'r') as f: #open the file
        contents = f.read()
    tts = gTTS(text=contents, lang=args.language)
    soundfilename=filename[:-4]+".mp3"
    tts.save(soundfilename)
if args.say=='yes':
    os.system("mpg123 "+soundfilename)
else:
    print("Arquivo criado: "+soundfilename)