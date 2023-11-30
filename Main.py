#This is a Morse code convertor

#Importing modules
import speech_recognition as sr
import pyttsx3
import time
from playsound import playsound


def speech_text():  # Converts Speech to Text
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Go Ahead I am Listening!")
        audio = r.listen(source)
        print("Recognizing.....")
        try:
            txt = r.recognize_google(audio)
            txt = txt.upper()
            return txt
            # print("Audio recorded sucessfully!")

        except Exception as e:
            print("Error : " + str(e))

def text_morse(txt):  # Converts text  to Morse code

    utxt = txt.upper()
    txt = " ".join(MORSE_CODE_DICT[c] for c in utxt)
    return txt


def morse_text(mt):  # Converts morse to text
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    reverse_message = "".join(reverse_dict[c] for c in mt.split(" "))
    return reverse_message


def text_speech(t):  # Converts Text to Speech
    tx = pyttsx3.init()
    tx.say(t)
    tx.runAndWait()


def play_morse_code(mcode):  # Plays the corresponding audio for morse code
    for c in mcode:
        if c == ".":
            playsound("short.mp3")
            time.sleep(0.1)
        elif c == "-":
            playsound("long.mp3")
            time.sleep(0.1)
        elif c == "/" or c == " ":
            time.sleep(0.3)
        else:
            print("Invalid Character detected")
def compute(val):
    op = input("Enter a for entering morse code else b to read morse of a random text and then convert into speech or text ")
    if op == "a":
        m = input("Enter morse code ")
        play_morse_code(m)
        mtt = morse_text(m)
        print("Text of Morse code is: \n" + mtt)
        if val==True:
            text_speech(mtt)


    elif op == "b":
        print("Converting the morse code of a random text into text ")

        with open("Morse.txt", "r") as file:
            for line in file:
                print("Morse code is: \n" + line.rstrip())
                play_morse_code(line.rstrip())
                mtt = morse_text(line.rstrip())
                print("Text of Morse code is: \n" + mtt)
                if val == True:
                    text_speech(mtt)
    else:
        print("Invalid Input!")

# This  is Morse code Dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}

print("WELCOME TO MORSE CODE CONVERTOR!!!")
print("Enter \n 1 For Speech to Morse \n 2 For Text to Morse \n 3 For Morse to Speech \n 4 For Morse to Text")
c = 0
try:
    ch = int(input())
except Exception:
    print("Invalid Input!")
    c = 1
if c == 0:
    if ch == 1:
        message = speech_text()
        print("You have Spoken : \n" + message)
        text = text_morse(message)
        print("Morse code is: \n" + text)
        play_morse_code(text)
    elif ch == 2:
        texty = input("Enter your text : ")
        text1 = text_morse(texty)
        print("Morse code is: \n" + text1)
        play_morse_code(text1)
    elif ch == 3:
        flag=True
        compute(flag)

    elif ch == 4:
        flag=False
        compute(flag)
    else:
        print("Invalid Input!")
