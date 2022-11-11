# randomMoviePicker
# Copyright (C) 2022  Leonardo Solari

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from movies import *
import tkinter as tk
from tkinter import filedialog
import glob
import random
import time
import os
import re

class Gui(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        #basic setup
        self.geometry("700x400")
        self.title("Random movie picker")
        self.rowconfigure(9)
        self.columnconfigure(4)
        self.resizable(True, True)
        self.eval('tk::PlaceWindow . center')

        self.folderPath = tk.StringVar()
        self.movieTitle = tk.StringVar()
        self.movieDuration = tk.StringVar()
        self.imdbUserRating = tk.StringVar()
        self.imdbMetascore = tk.StringVar()
        self.movieList = []

        #directory label
        self.directoryLabel = tk.Label(self ,text="Movies folder path")
        self.directoryLabel.grid(row=0,column = 0)

        #choose directory button
        self.btnFind = tk.Button(self, text="Browse Folders",command=self.setDirectory)
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

        #close button
        self.closeButton = tk.Button(self, text="Close", command=lambda:exit())
        self.closeButton.grid(row=7, column=1)


    def setMovie(self):     
        moviePath = random.choice(self.movieList)
        movie = Movie(moviePath)
        self.movieTitle.set(movie.getParsedName())
        self.movieDuration.set(movie.getDuration()) 
        self.imdbUserRating.set(movie.getUserscore())
        self.imdbMetascore.set(movie.getMetascore())



    def setDirectory(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
        self.movieList = []
        for dirpath, dirnames, filenames in os.walk(folder_selected):
            for f in filenames:
                if os.path.splitext(f)[1] in extensionsDotted() and not f.startswith("._"):
                    self.movieList.append(os.path.join(dirpath, f))



if __name__ == "__main__":
    app = Gui()
    app.mainloop()
