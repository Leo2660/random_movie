from tkinter import Tk, filedialog
import os, random
import time
from os import system, name
from moviepy.editor import VideoFileClip
import glob
import PTN

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


movies_mp4 = glob.glob(directory_path + "/**/*.mp4", recursive = True) #trova tutti gli mp4
movies_mkv = glob.glob(directory_path + "/**/*.mkv", recursive = True) #trova tutti gli mkv
movies = movies_mp4 + movies_mkv
random_movie_path = random.choice(movies)
movie_name = os.path.basename(os.path.normpath(random_movie_path)) #tiene solo la parte finale del path
movie_parsed = PTN.parse(movie_name)
duration = VideoFileClip(random_movie_path).duration #ottiene la durata del film
print("Il tuo film per stasera è: " + movie_parsed['title'])
print("Durata: " + time.strftime('%H:%M:%S', time.gmtime(duration)) )

