from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import PTN
import random
import glob
import os
from moviepy.editor import VideoFileClip
import time
from imdb import IMDb
import rtsimple as rt



#GUI settings
gui = Tk()
gui.geometry("900x400")
gui.title("Random movie")
gui.rowconfigure(9)
gui.columnconfigure(4)

ia = IMDb() #create imdb istance

rt.API_KEY = '5z3fnv5f9j6ewc2hy6s8zbg7'


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

def setMovie():
    movieList = fileList = glob.glob(folderPath.get() + "/**/*." + "mp4", recursive = True) + glob.glob(folderPath.get() + "/**/*." + "mkv", recursive = True)
    if (len(movieList) == 0):
        movieTitle.set("Nessun Film Trovato")
        time.sleep(5)
        exit()
    moviePath = random.choice(movieList)
    movieName = os.path.basename(os.path.normpath(moviePath))
    movieParsed = PTN.parse(movieName) #returns dict
    movieTitle.set(movieParsed['title'])
    duration = VideoFileClip(moviePath).duration
    movieDuration.set(time.strftime('%H:%M:%S', time.gmtime(duration)))
    try:
        search = ia.search_movie(movieParsed['title']) #uses title field from parsed movie name
        movie_id = search[0].movieID #gets movie id
        movie_from_id = ia.get_movie(movie_id) #gets movie data using the movie id
        imdbUserRating.set(movie_from_id.data['rating'])
        critics_data = ia.get_movie_critic_reviews(movie_id) #gets critics data, returned value is a dict
        imdbMetascore.set(critics_data['data']['metascore'])
    except:
        imdbUserRating.set("Impossibile trovare i dati su IMDb")  
        imdbMetascore.set("Impossibile trovare i dati su IMDb")

    try:
        rt_movie = rt.Movies()
        response = rt_movie.search(q=movieParsed)
        movieId = rt_movie.movie[0]['id']
        rt_movie = rt.Movies(movieId)
        rtUserScore.set(rt_movie.ratings['audience_score'])
        rtCriticScore.set(rt_movie.ratings['critics_score'])
    except:
        rtUserScore.set("Impossibile trovare i dati su RottenTomatoes")
        rtCriticScore.set("Impossibile trovare i dati su RottenTomatoes")


#variables
folderPath = StringVar()
movieTitle = StringVar()
movieDuration = StringVar()
imdbUserRating = StringVar()
imdbMetascore = StringVar()
rtUserScore = StringVar()
rtCriticScore = StringVar()


#directory label
a = Label(gui ,text="Path")
a.grid(row=0,column = 0)

#choose directory button
btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
btnFind.grid(row=0,column=2)

#path entry
E = Entry(gui,textvariable=folderPath)
E.grid(row=0,column=1)

#bottone azione
c = ttk.Button(gui ,text="Film Casuale", command=setMovie)
c.grid(row=1,column=1)

#title label
title_label = Label(gui, text="Titolo")
title_label.grid(row=2, column=0)

#title entry
file_entry = Entry(gui, width=50, textvariable=movieTitle)
file_entry.grid(row=2, column=1)

#duration label
title_label = Label(gui, text="Durata")
title_label.grid(row=3, column=0)

#duration entry
file_entry = Entry(gui, width=50, textvariable=movieDuration)
file_entry.grid(row=3, column=1)

#imdb userscore label
title_label = Label(gui, text="Punteggio utenti IMDb")
title_label.grid(row=4, column=0)

#imdb userscore entry
file_entry = Entry(gui, width=50, textvariable=imdbUserRating)
file_entry.grid(row=4, column=1)

#imdb metascore label
title_label = Label(gui, text="Metascore IMDb")
title_label.grid(row=5, column=0)

#imdb metascore entry
file_entry = Entry(gui, width=50, textvariable=imdbMetascore)
file_entry.grid(row=5, column=1)

#rt user score label
title_label = Label(gui, text="Audience Score RottenTomatoes")
title_label.grid(row=6, column=0)

#rt user score entry
file_entry = Entry(gui, width=50, textvariable=rtUserScore)
file_entry.grid(row=6, column=1)

#rt critic score label
title_label = Label(gui, text="Critics Score RottenTomatoes")
title_label.grid(row=7, column=0)

#rt critic score entry
file_entry = Entry(gui, width=50, textvariable=rtCriticScore)
file_entry.grid(row=7, column=1)


gui.mainloop()