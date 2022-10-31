from curses.ascii import NUL
from multiprocessing import connection
import sqlite3
from sqlite3 import OperationalError
from datetime import date
import sys
import getpass

#db_name = sys.argv[1]

#conn = sqlite3.connect(db_name)
conn = sqlite3.connect('proj.db')

def execFile(filename, cursor):
    """
    Allows the reading and execution of SQL queries from files that are passed through as arguments

    :param filename: name of the file containing queries to be run
    """
    file = open(filename, 'r')
    execFile = file.read()
    file.close()
    lines = execFile.split(';')

    for line in lines:
        cursor.execute(line)


def regAccount(cursor, conn):
    while(True):
        print("\nCreate an Account")
        username  = input("\nEnter a username: ").lower()
        # Checks to see if username exists
        cursor.execute("""
                            SELECT uid
                            FROM users
                            WHERE lower(uid) = ?
                             """ , (username,))
        result = cursor.fetchone()
        if(result == None):
            name = input("\nEnter your name: ")
            password = input("\nEnter password: ")
            cursor.execute("""
                                INSERT INTO users VALUES (? ,? ,?)
                                 """, (username,name,password,))
            conn.commit()
            new_user = User(username,cursor,conn)
            return new_user
        else:
            print("\nUsername is already in use. Select one of the options below\n")
            while(True):    
                selected_option = input("1) Already have an account \n2) Enter a new username\nSelected Option: ")
                if(selected_option == "1"):
                    return None
                elif(selected_option == "2"):
                    break
                else:
                    print("Select a value between 1 and 2")

def loginScreen(cursor, conn):
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
        mainChoice = input("1) Log In\n2) Register User \n3) Exit\nWelcome! Please choose an option: ")

        if mainChoice == "1":
            username = input("\nUsername: ")
            password = getpass.getpass("Password: ") # getpass hides text while user is typing
            #password = input("Password: ")

            # check if user exists
            cursor.execute("SELECT * FROM users WHERE uid= ? COLLATE NOCASE AND pwd= ? ;", (username, password))
            userResult = cursor.fetchone()


            # check if artist exists
            cursor.execute("SELECT * FROM artists WHERE aid= ? COLLATE NOCASE AND pwd= ? ;", (username, password))
            artistResult = cursor.fetchone()

            # if login info appears in users AND artists tables
            if userResult is not None and artistResult is not None:
                print("\nHello " + userResult[1] + "!")
                while loginChoice not in [1, 2]:
                    print("\nAccount belongs to user and artist")
                    loginChoice = input("1) User\n2) Artist\nChoose how you would like to log in: ")
                    if loginChoice == "1":
                        print("\nLogging in as a user...")
                        # userOptions()
                        person = User(username , cursor , conn)
                        return person
                    elif loginChoice == "2":
                        print("\nLogging in as an artist...")
                        # artistOptions()
                        person = Artiste(username , cursor, conn)
                        return person 
                
            # if login info appears in users OR artists tables
            elif userResult is not None:
                print("\nHello " + userResult[1] + "!")
                # userOptions()
                person = User(username , cursor, conn)
                return person
            elif artistResult is not None:
                print("\nHello " + artistResult[1] + "!")
                # artistOptions()
                person = Artiste(username , cursor, conn)
                return person
                
            # login info does not exist
            else:
                print("\nAccount does not match our records")
        elif mainChoice == "2":
            new_user = regAccount(cursor,conn)
            if(new_user is not None):
                return new_user
            else:
                continue
        elif mainChoice == "3":
            print("\nShutting down...")
            break
        else:
            print("Invalid input")
            continue

    print("Program shut down")

class People:
    def __init__(self, id , cursor , conn):
        self.id = id
        self.cursor = cursor
        self.conn = conn
        self.session_no = None

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

    def Options(self):
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

            menuChoice = input("Choose an option: ")

            if menuChoice == "1":
                self.addSong()
            elif menuChoice == "2":
                self.findTopFan()
            elif menuChoice == "3":
                print("\nLogging out artist...")
                break
            else:
                print("Invalid option, please input a number between x and x")

class User(People):
    def startSession(self):
        """
        Starts a session for a user with a unique session number.
        The session's start date is the current date, and the end date is NULL

        :param userID: the ID of the user currently logged in
        """

        if(self.session_no is not None):
            print("You cant start a new session")
        else:
            # Gets the session  with the highest number
            current_day = date.today()

            d1 = current_day.strftime("%Y-%m-%d")

            self.cursor.execute("SELECT COUNT(sno) FROM sessions;")
            number_of_sessions = self.cursor.fetchone()

            # Create a new session
            if(number_of_sessions[0] == 0):
                # Checks whether there are any created sessions
                self.session_no = number_of_sessions[0] + 1
                new_session = (self.id,self.session_no,d1,)
                print("Starting session " + str(self.session_no))
            else:
                # Checks for the maximum session number and adds one to it
                self.cursor.execute("SELECT MAX(sno) FROM sessions;")
                last_added_session = self.cursor.fetchone()
                self.session_no = last_added_session[0] + 1
                new_session = (self.id,self.session_no,d1,)
                print("Starting session " + str(self.session_no))
                
            # Insert session into table
            self.cursor.execute("insert into sessions values (?, ?, ?, NULL);",new_session)
            self.conn.commit()

    def endSession(self):
        # Checks if there is an active session
        if(self.session_no is None):
            print("Sorry you cant end the session, no session has been started")
        else:
            # Ends sessions if the is an existing sessiomn
            # Updates the end value of session
            current_day = date.today()

            d1 = current_day.strftime("%Y-%m-%d")
            self.cursor.execute("""UPDATE sessions 
                                    SET end = ?
                                    WHERE sno = ?  ;""" , (current_day,self.session_no))
            print("End of session "  + str(self.session_no))
            self.session_no = None
            self.conn.commit()
#=======================================================================================================================================
    def searchArtiste(self,keywords):
        # Searches for artists that match one or more keywords provided by the user.
        # Retrieves artists that have any of the keywords in their name or in the title of a song they have performed.
        # Each match returns the name, nationality, and number of songs performed by that artist.
        # Matches are ordered by number of matching keywords (highest at the top).
        # At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
        # Selecting an artist will return the id, title, and duration of all songs they have performed.
            
        # :param keywords: user inputted string
        pass
#====================================================================================================================================
    def searchSPlaylist(self,keywords):
        #Searches for songs and playlists that match one or more keywords provided by the user.
        #Retrieves all songs and playlists that have any of the keywords in their title. Ordered by number of matching keywords (highest at the top).
        #At most, 5 matches are shown at a time, user has the option to select a match or view the rest in a paginated, downward format.
        #If a playlist is selected, display the id, title, and total duration of songs.
        #Songs are displayed with id, title, and duration. If selected, users can perform a song action.
                    
        #:param keywords: user inputted string
                    
        #global connection, cursor

        Search = {}
        x = keywords.split(" ")
        for k in x:
            self.cursor.execute("SELECT s.sid FROM songs s WHERE title LIKE ? COLLATE NOCASE ;", ('%'+ k + '%',))
            s = self.cursor.fetchall()
            self.cursor.execute("SELECT playlists.pid FROM playlists WHERE title LIKE ? COLLATE NOCASE ;", ('%'+ k+ '%',))
            p = self.cursor.fetchall()
            for i in s:
                if i[0] not in Search:
                    Search["s" + str(i[0]) ] = 1
                else:
                    Search["s" + str(i[0]) ] += 1
            for k in p:
                if k[0] not in Search:
                    Search["p" + str(i[0]) ] = 1
                else:
                    Search["p" + str(i[0]) ] += 1
        self.displayfive(Search)

        

        #SearchP = []
        #SearchS= []


        #for k in x:
            #self.cursor.execute("SELECT * FROM songs WHERE title LIKE ? COLLATE NOCASE ;", ('%'+ k + '%',))
            #s = self.cursor.fetchall()
            #self.cursor.execute("SELECT * FROM playlists WHERE title LIKE ? COLLATE NOCASE ;", ('%'+ k+ '%',))
            #p = self.cursor.fetchall()

        #for i in s:
            #if i not in SearchS:
                #SearchS.append(i)
        #for i in p:
            #if i not in SearchP:
                #SearchP.append(i)

        # displays top five songs
        #print("\n\t")
        #if len(SearchS) < 5:
            #self.displayall(SearchS, "Songs:")
        #else:
            #self.displayfive(SearchS, "Songs:")
        
        #display top five playlists
        #print("\n\t")
        #if len(SearchP) < 5:
            #self.displayall(SearchP, "Playlist:")
        #else:
            #self.displayfive(SearchP,"Playlist:")
        
        #self.selection()
        
    #----------------------------------------------------------------------------------------------------------------------------------------
    def displayfive(self,spList):
    #prints top five songs and playlists

        c = 0
        while c < 5:
            for val in sorted(spList, key=spList.get, reverse=True):
                print (val , spList[val])
                if val[0] == "s":
                    v = val[1:]
                    self.cursor.execute("SELECT s.sid, s.title, s.duration FROM songs s WHERE s.sid = ?;", (int(v),))
                    song = self.cursor.fetchone()
                    print(song[0], song[1], song[2])
                elif val[0] == "p":
                    v = val[1:]
                    self.cursor.execute("SELECT p.pid, p.title, SUM(s.duration) FROM songs s, playlists p , plinclude l WHERE p.title = ? COLLATE NOCASE AND p.pid = l.pid AND l.sid = s.sid ;", (int(v),))
                    playlist = self.cursor.fetchone()
                    print(playlist[0], playlist[1], playlist[2])
    #------------------------------------------------------------------------------------------------------------------------------------
    def displayall(self,spList, type):
        c = 0
        if type == "Songs:":
            for s in spList:
                print(c,type, s[0], s[1], s[2])
                c = c+1
        else:
            for p in spList:
                self.cursor.execute("SELECT SUM(s.duration) FROM songs s, playlists p , plinclude l WHERE p.title = ? COLLATE NOCASE AND p.pid = l.pid AND l.sid = s.sid ;", (p[1],))
                total_duration = self.cursor.fetchone()
                print(c, type, p[0], p[1], total_duration[0])
    #-------------------------------------------------------------------------------------------------------------------------------

    def selection(self):
        """
        Based on user selection do appropriate action
        If user selects playlist, list all songs in the playlist with their title, duration and allow to perform song actions.
        If songs selected, id, title, duration and allow song actions
        """
        choice_type = ""
        while choice_type != "q":

            #options
            print("\n\tSELECTION MENU")
            choice_type = input("Enter p for playlist or s for songs and q to quit: ")

            #playlists(pid, title, uid)
            #plinclude(pid, sid, sorder)
            if choice_type == "p":
                choice_title = input("Enter title of playlist: ")
                self.cursor.execute("SELECT s.sid, s.title , s.duration FROM playlists p, plinclude l, songs s WHERE p.title = ? COLLATE NOCASE AND p.pid = l.pid AND l.sid = s.sid;",(choice_title,))
                songl = self.cursor.fetchall()
                self.displayall(songl, "Songs:")
                continue
            elif choice_type == "s":
                choice_title = input("Enter title of song: ")
                # call function that performs song actions to perform song actions

#=============================================================================================================================================  
    def Options(self):
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

            menuChoice = input("Choose an option: ")

            if menuChoice == "1":
                self.startSession()
            elif menuChoice == "2":
                keyword = input("Enter: ")
                self.searchSPlaylist(keyword)
            elif menuChoice == "3":
                self.searchArtiste()
            elif menuChoice == "4":
                self.endSession()
            elif menuChoice == "5":
                if(self.session_no is not None):
                    self.endSession()
                print("\nLogging out user...")
                break
            else:
                print("Invalid option, please input a number between x and x")

#================================================================================================================

def main():
    conn = sqlite3.connect('proj.db')

    c = conn.cursor()
    # execFile('prj-tables.sql',c)
    # execFile('test-data.sql',c )
    person = loginScreen(c , conn)
    if(person is not None):
        person.Options() 

    conn.commit()
    conn.close()


if __name__ ==  '__main__':
    main()
main
