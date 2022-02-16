from tkinter import Tk, filedialog
import os, random
import time
from os import system, name
from moviepy.editor import VideoFileClip

#clear console function
def clear():
    #for windows 
    if name == 'nt':
        _ = system('cls')
    #for mac and linux
    else:
        _ = system('clear')



root = Tk() #pointing root to Tk() to use it as Tk() in program
root.withdraw() #hides small tkinter window
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection

clear()
print("Selezionare la cartella che contiene i film")
time.sleep(2)
directory_path = filedialog.askdirectory() #returns opened path as str

movie = random.choice(os.listdir(directory_path))
#complete_path = directory_path + '/' + movie
#duration = VideoFileClip(complete_path).duration
print("Il tuo film per stasera è: " + movie)
#print("Durata: " + time.strftime('%H:%M:%S', time.gmtime(duration)) )

#quelli commentati sono per la durata, li farò poi