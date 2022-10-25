import sqlite3
from sqlite3 import OperationalError
import sys

db_name = sys.argv[1]

conn = sqlite3.connect(db_name)
c = conn.cursor()

def execFile(filename):
    """
    Allows the reading and execution of SQL queries from files that are passed through as arguments

    :param filename: name of the file containing queries to be run
    """
    file = open(filename, 'r')
    execFile = file.read()
    file.close()
    lines = execFile.split(';')

    for line in lines:
        c.execute(line)

def loginScreen():
    """
    Prompts the user to login with their user ID and password.
    Checks if user exists and password is correct, determines type of user.
    Redirects to the appropriate menu depending on the type of user.
    A user ID that is both a 'user' and 'artist' may choose how they would like to log in.
    """
    pass

def userOptions():
    """
    Presents the menu options for a USER. 
    Calls the appropriate function according to the menu choice.
    """
    pass

def artistOptions():
    """
    Presents the menu options for an ARTIST. 
    Calls the appropriate function according to the menu choice.
    """
    pass

def startSession(userID):
    """
    Starts a session for a user with a unique session number.
    The session's start date is the current date, and the end date is NULL

    :param userID: the ID of the user currently logged in
    """
    pass

def searchSP(keywords):
	"""
	Searches for songs and playlists that match one or more keywords provided by the user.
	Retrieves all songs and playlists that have any of the keywords in their title. Ordered by number of matching keywords (highest at the top).
	At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
	If a playlist is selected, display the id, title, and total duration of songs.
	Songs are displayed with id, title, and duration. If selected, users can perform a song action.
	
	:param keywords: user inputted string
	"""
    pass

def searchA(keywords):
	"""
	Searches for artists that match one or more keywords provided by the user.
	Retrieves artists that have any of the keywords in their name or in the title of a song they have performed.
	Each match returns the name, nationality, and number of songs performed by that artist.
	Matches are ordered by number of matching keywords (highest at the top).
	At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
	Selecting an artist will return the id, title, and duration of all songs they have performed.
	
	:param keywords:
	"""
    pass

def endSession():
	"""
	
	"""
    pass

def addSong():
    pass

def findTop():
    pass
