from movies import *
import tkinter as tk
from tkinter import filedialog
import glob
import random
import time

class Gui(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        #basic setup
        self.geometry("900x400")
        self.title("Random movie picker")
        self.rowconfigure(9)
        self.columnconfigure(4)
        self.resizable(True, True)

        self.folderPath = tk.StringVar()
        self.movieTitle = tk.StringVar()
        self.movieDuration = tk.StringVar()
        self.imdbUserRating = tk.StringVar()
        self.imdbMetascore = tk.StringVar()

        #directory label
        self.directoryLabel = tk.Label(self ,text="Movies folder path")
        self.directoryLabel.grid(row=0,column = 0)

        #choose directory button
        self.btnFind = tk.Button(self, text="Browse Folders",command=self.getFolderPath)
        self.btnFind.grid(row=0,column=2)

        #directory entry
        self.directoryEntry = tk.Entry(self, width=50, textvariable=self.folderPath)
        self.directoryEntry.grid(row=0,column=1)

        #pick movie button
        self.pickMovieButton = tk.Button(self ,text="Pick random movie", command=self.setMovie)
        self.pickMovieButton.grid(row=1,column=1)

        #title label
        self.titleLabel = tk.Label(self, text="Title")
        self.titleLabel.grid(row=2, column=0)

        #title entry
        self.titleEntry = tk.Entry(self, width=50, textvariable=self.movieTitle)
        self.titleEntry.grid(row=2, column=1)

        #duration label
        self.durationLabel = tk.Label(self, text="Duration")
        self.durationLabel.grid(row=3, column=0)

        #duration entry
        self.durationEntry = tk.Entry(self, width=50, textvariable=self.movieDuration)
        self.durationEntry.grid(row=3, column=1)

        #imdb userscore label
        self.imdbUserscoreLabel = tk.Label(self, text="IMDb user score")
        self.imdbUserscoreLabel.grid(row=4, column=0)

        #imdb userscore entry
        self.imdbUserscoreEntry = tk.Entry(self, width=50, textvariable=self.imdbUserRating)
        self.imdbUserscoreEntry.grid(row=4, column=1)

        #imdb metascore label
        self.imdbMetascoreLabel = tk.Label(self, text="IMDb Metascore")
        self.imdbMetascoreLabel.grid(row=5, column=0)

        #imdb metascore entry
        self.imdbMetascoreEntry = tk.Entry(self, width=50, textvariable=self.imdbMetascore)
        self.imdbMetascoreEntry.grid(row=5, column=1)


    def setMovie(self):
        movieList = glob.glob(self.folderPath.get() + "/**/*." + "mp4", recursive = True) + glob.glob(self.folderPath.get() + "/**/*." + "mkv", recursive = True)
        
        if (len(movieList) == 0):
            self.movieTitle.set("No movie files found in this folder")
            time.sleep(5)
            exit()
            

        moviePath = random.choice(movieList)
        movie = Movie(moviePath)
        self.movieTitle.set(movie.getParsedName())
        self.movieDuration.set(movie.getDuration()) 
        self.imdbUserRating.set(movie.getUserscore())
        self.imdbMetascore.set(movie.getMetascore())



    def getFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)


if __name__ == "__main__":
    app = Gui()
    app.mainloop()
