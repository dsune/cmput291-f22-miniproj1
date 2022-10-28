import sqlite3
from sqlite3 import OperationalError
import sys
import getpass

#db_name = sys.argv[1]

#conn = sqlite3.connect(db_name)

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

def loginScreen(cursor):
    """
    Prompts the user to login with their user ID and password.
    Checks if user exists and password is correct, determines type of user.
    Redirects to the appropriate menu depending on the type of user.
    A user ID that is both a 'user' and 'artist' may choose how they would like to log in.
    """
    while(True):
        loginChoice = 0
        mainChoice = 0
        userResult = None

        # initial menu when starting the program
        print("\nMAIN MENU")
        mainChoice = int(input("1) Log In\n2) Register User \n3) Exit\nWelcome! Please choose an option: "))

        if mainChoice == 1:
            username = input("\nUsername: ")
            password = getpass.getpass("Password: ") # getpass hides text while user is typing

            # check if user exists
            cursor.execute("SELECT * FROM users WHERE uid= ? COLLATE NOCASE AND pwd= ? ;", (username, password))
            userResult = c.fetchone()

            # check if artist exists
            cursor.execute("SELECT * FROM artists WHERE aid= ? COLLATE NOCASE AND pwd= ? ;", (username, password))
            artistResult = c.fetchone()

            # if login info appears in users AND artists tables
            if userResult is not None and artistResult is not None:
                print("\nHello " + userResult[1] + "!")
                while loginChoice not in [1, 2]:
                    print("\nAccount belongs to user and artist")
                    loginChoice = int(input("1) User\n2) Artist\nChoose how you would like to log in: "))
                if loginChoice == 1:
                    print("\nLogging in as a user...")
                    userOptions()
                elif loginChoice == 2:
                    print("\nLogging in as an artist...")
                    artistOptions()
                
            # if login info appears in users OR artists tables
            elif userResult is not None:
                print("\nHello " + userResult[1] + "!")
                userOptions()
            elif artistResult is not None:
                print("\nHello " + artistResult[1] + "!")
                artistOptions()
                
            # login info does not exist
            else:
                print("\nAccount does not match our records")
        elif mainChoice == 2:
            regAccount()
        elif mainChoice == 3:
            print("\nShutting down...")
            break
        else:
            print("Invalid input")
            continue

    print("Program shut down")

class People:
    def __init__(self, id):
        self.id = id

class Artiste(People):
    def addSong(self):
        print("Add song function")
        pass

    def findTopFan(self):
        print("Find top fans/playlists function")
        pass

    def findTopPlaylist(self):
        print("Find top fans/playlists function")
        pass

    def artistOptions(self):
        """
        Presents the menu options for an ARTIST. 
        Calls the appropriate function according to the menu choice.
        """
        while(True):
            menuChoice = 0

            # menu options
            print("\nARTIST MENU")
            print("1) Add a song")
            print("2) Find your top fans and playlists")
            print("3) Log Out")

            menuChoice = int(input("Choose an option: "))

            if (menuChoice not in range(1, 4, 1)):
                print("Invalid option, please input a number between x and x")
            elif menuChoice == 1:
                self.addSong()
            elif menuChoice == 2:
                self.findTopFan()
            elif menuChoice == 3:
                print("\nLogging out artist...")
                break

class User(People):
    def startSession(self):
        """
        Starts a session for a user with a unique session number.
        The session's start date is the current date, and the end date is NULL

        :param userID: the ID of the user currently logged in
        """
        print("Start session function")
        pass

    def endSession(self):
        print("End session function")
        pass

    def searchArtiste(self,keywords):
        # Searches for artists that match one or more keywords provided by the user.
        # Retrieves artists that have any of the keywords in their name or in the title of a song they have performed.
        # Each match returns the name, nationality, and number of songs performed by that artist.
        # Matches are ordered by number of matching keywords (highest at the top).
        # At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
        # Selecting an artist will return the id, title, and duration of all songs they have performed.
            
        # :param keywords: user inputted string
            
        print("Search artists function")
        pass

    def searchSong(self,keywords):
        #Searches for songs and playlists that match one or more keywords provided by the user.
        #Retrieves all songs and playlists that have any of the keywords in their title. Ordered by number of matching keywords (highest at the top).
        #At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
        #If a playlist is selected, display the id, title, and total duration of songs.
        #Songs are displayed with id, title, and duration. If selected, users can perform a song action.
            
        #:param keywords: user inputted string
            
        global connection, cursor

        x= keywords.split(" ")
        # x is a list. traverse x then match the word and place it into a SP list if the same tuple is not in SP.
        #Display function to display top five
        # if displayed display everything is selected display all in SP list.

    def searchPlaylist(self,keywords):
        #Searches for songs and playlists that match one or more keywords provided by the user.
        #Retrieves all songs and playlists that have any of the keywords in their title. Ordered by number of matching keywords (highest at the top).
        #At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
        #If a playlist is selected, display the id, title, and total duration of songs.
        #Songs are displayed with id, title, and duration. If selected, users can perform a song action.
                    
        #:param keywords: user inputted string
                    
        global connection, cursor

        x= keywords.split(" ")
        # x is a list. traverse x then match the word and place it into a SP list if the same tuple is not in SP.
        #Display function to display top five
        # if displayed display everything is selected display all in SP list.
    
    def userOptions(self):
        """
        Presents the menu options for a USER. 
        Calls the appropriate function according to the menu choice.
        """
        while(True):
            menuChoice = 0

            # menu options
            print("\nUSER MENU")
            print("1) Start a listening session")
            print("2) Search songs and playlists")
            print("3) Search artists")
            print("4) End your listening session")
            print("5) Log Out")

            menuChoice = int(input("Choose an option: "))

            if (menuChoice not in range(1, 8, 1)):
                print("Invalid option, please input a number between x and x")
            elif menuChoice == 1:
                self.startSession()
            elif menuChoice == 2:
                self.searchSP()
            elif menuChoice == 3:
                self.searchA()
            elif menuChoice == 4:
                self.endSession()
            elif menuChoice == 5:
                print("\nLogging out user...")
                break


def main():
    conn = sqlite3.connect('proj.db')

    c = conn.cursor()
    execFile('prj-tables.sql')
    execFile('test-data.sql')
    loginScreen(c)

    conn.commit()
    conn.close()


if __name__ ==  '__main__':
    main()