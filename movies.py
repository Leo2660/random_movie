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


import os
import PTN
from imdb import IMDb
from moviepy.editor import VideoFileClip
import time
import cv2
import datetime

class Movie:

    #Overview: objects of this class represent movies. The attributes represent:
    #   path = the full path of the movie file
    #   fileName = the movie file's name
    #   parsedName = the title of the movie, obtained by parsing fileName
    #   duration = the movie's runtime
    #   imdbUserscore = the movie's user score on IMDb
    #   imdbMetascore = the movie's Metascore (critics score) on IMDb
    #
    #Every attribute can be accessed with a method 

    def __init__(self, path):
        self.path = str(path)
        self.fileName = os.path.basename(os.path.normpath(self.path))
        parsedFIle = PTN.parse(self.fileName)
        self.parsedName= parsedFIle['title']
        self.duration = time.strftime('%H:%M:%S', time.gmtime(VideoFileClip(self.path).duration))
        try:
            ia = IMDb() #create imdb istance
            search = ia.search_movie(self.parsedName) #uses title field from parsed movie name
            movie_id = search[0].movieID #gets movie id
            movie_from_id = ia.get_movie(movie_id) #gets movie data using the movie id
            self.imdbUserscore = movie_from_id.data['rating']
            critics_data = ia.get_movie_critic_reviews(movie_id) #gets critics data, returned value is a dict
            self.imdbMetascore = critics_data['data']['metascore']
        except:
            self.imdbUserscore = "Impossibile trovare i dati su IMDb"  
            self.imdbMetascore = "Impossibile trovare i dati su IMDb"


    #METHODS
    def getPath(self):
        return self.path

    def getFileName(self):
        return self.fileName

    def getParsedName(self):
        return self.parsedName

    def getDuration(self):
        return self.duration
    
    def getUserscore(self):
        return self.imdbUserscore

    def getMetascore(self):
        return self.imdbMetascore
        


def extensionsDotted():
    extensions = [".mp4", ".mkv", ".avi", ".wmv", ".flv", ".webm"]
    return extensions

def extensions():
    extensions = ["mp4", "mkv", "avi", "wmv", "flv", "webm"]
    return extensions
    
def durationFromPath(path):
    return VideoFileClip(path).duration
