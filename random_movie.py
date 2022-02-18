from tkinter import Tk, filedialog
import os, random
import time
from os import system, name
from moviepy.editor import VideoFileClip
import glob
import PTN
import imdb

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
ia = imdb.IMDb() #create imdb istance


clear()
print("Selezionare la cartella che contiene i film")
time.sleep(2)
directory_path = filedialog.askdirectory() #returns opened path as str


movies_mp4 = glob.glob(directory_path + "/**/*.mp4", recursive = True) #trova tutti gli mp4
movies_mkv = glob.glob(directory_path + "/**/*.mkv", recursive = True) #trova tutti gli mkv
movies = movies_mp4 + movies_mkv
random_movie_path = random.choice(movies)
movie_name = os.path.basename(os.path.normpath(random_movie_path)) #tiene solo la parte finale del path
movie_parsed = PTN.parse(movie_name) #returns dict
duration = VideoFileClip(random_movie_path).duration #ottiene la durata del film

print("Il tuo film per stasera è: " + movie_parsed['title'])
print("Durata: " + time.strftime('%H:%M:%S', time.gmtime(duration)) )

try:
    search = ia.search_movie(movie_parsed['title']) #uses title field from parsed movie name
    movie_id = search[0].movieID #gets movie id
    movie_from_id = ia.get_movie(movie_id) #gets movie data using the movie id
    user_rating = movie_from_id.data['rating']
    critics_data = ia.get_movie_critic_reviews(movie_id) #gets critics data, returned value is a dict
    metascore = critics_data['data']['metascore']
    print("User rating: " + str(user_rating))
    print("Metascore: " + str(metascore))
except:
    print("Errore nella ricerca dei dati su IMDb")

