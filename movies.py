import os
import PTN
from imdb import IMDb
from moviepy.editor import VideoFileClip
import time

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
        self.path = path
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
        

     