from curses.ascii import NUL, isdigit
from multiprocessing import connection
import sqlite3
from sqlite3 import OperationalError
from datetime import date
import sys
import getpass
import random
from turtle import title

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
    return None

class People:
    def __init__(self, id , cursor , conn):
        self.id = id
        self.cursor = cursor
        self.conn = conn
        self.session_no = None

class Artiste(People):
    def addSong(self):
        while(True):
            # prompts user for song name and duration they would like to add
            song_name = input("Enter the name of your song: ").lower()
            while(True):
                try:
                    song_dur = int(input("Enter the duration of your song: "))
                except:
                    print("You must enter an integer")
                    continue
                break

            # check if the song and duration already exists for this artist
            self.cursor.execute("""
                                SELECT s.title
                                FROM songs s, perform p
                                WHERE p.aid = ?
                                AND p.sid = s.sid
                                AND lower(s.title) = ?
                                AND s.duration = ?;
                                """, (self.id, song_name, song_dur,))
            result = self.cursor.fetchone()
            if(result == None):
                # checks if song id exists before inserting into table
                self.cursor.execute("""
                                    SELECT sid
                                    FROM songs;
                                    """)
                id_list = self.cursor.fetchall()
                while(True):
                    new_id = random.randint(0, 500)
                    if new_id not in id_list:
                        break
                    else:
                        continue
                
                # add new song to the 'songs' table
                self.cursor.execute("""
                                    INSERT INTO songs VALUES (?, ?, ?)
                                    """, (new_id, song_name, song_dur))
                
                # adds a new entry to 'perform' table with current artist id and the new song id
                self.cursor.execute("""
                                    INSERT INTO perform VALUES (?, ?)
                                    """, (self.id, new_id))
                
                # prompts user for any additional artists that performed the song
                while(True):
                    add_perform = input("Did another artist perform this song with you? (y/n): ").lower()
                    if add_perform == 'y':
                        while(True):
                            add_aid = input("Enter their Artist ID: ")

                            # check if the inputted Artist ID exists
                            self.cursor.execute("""
                                                SELECT aid
                                                FROM artists
                                                WHERE aid = ?;
                                                """, (add_aid,))
                            aid_search = self.cursor.fetchone()
                            if aid_search == None:
                                print("\nThat is not a valid Artist ID, please try a different one")
                                continue
                            # if the Artist ID exists, adds a new entry to 'perform' table for the inputted Artist ID
                            else:
                                self.cursor.execute("""
                                                    INSERT INTO perform VALUES (?, ?)
                                                    """, (add_aid, new_id))
                            break
                    elif add_perform == 'n':
                        break
                    else:
                        print("Invalid option, please enter 'y' or 'n'")
                break
            else:
                print("\nThis song already exists in your discography")
                continue
        self.conn.commit()

    def findTopFan(self):
        rank = 1

        # finds fans who have listen to this artist, ordered by total listening time
        self.cursor.execute("""
                            SELECT l.uid, sum(s.duration * l.cnt) as total_listen
                            FROM listen l, songs s, perform p
                            WHERE l.sid = s.sid
                            AND s.sid = p.sid
                            AND p.aid = ?
                            GROUP BY l.uid, p.aid
                            ORDER BY total_listen desc
                            LIMIT 3;
                            """, (self.id,))
        fans = self.cursor.fetchall()

        if not fans:
            print("\nNobody has listened to your music")
        else:
            # prints (at most) the top 3 fans for this artist
            print("\nTop Fans for " + self.id)
            for fan in fans:
                print(str(rank) + ") " + "User ID: " + fan[0] + " | Listening Time: " + str(round(fan[1], 2)))
                rank += 1
            

    def findTopPlaylist(self):
        rank = 1

        # finds playlists that contain songs by this artist
        self.cursor.execute("""
                            SELECT i.pid, pl.title, COUNT(*) as in_playlist
                            FROM plinclude i,  perform p, playlists pl
                            WHERE p.aid = ?
                            AND p.sid = i.sid
                            AND i.pid = pl.pid
                            GROUP BY i.pid, pl.title
                            ORDER BY in_playlist DESC
                            LIMIT 3;
                            """, (self.id,))
        playlists = self.cursor.fetchall()

        if not playlists:
            print("\nThere are no playlists that contain your songs")
        else:
            # prints (at most) the top 3 playlists based on amount of songs by this artist included in the playlist
            print("\nTop Playlists for " + self.id)
            for pl in playlists:
                print(str(rank) + ") " + "Playlist ID: " + str(pl[0]) + " | Title: " + str(pl[1]) + " | Number of your songs in this playlist: " + str(pl[2]))
                rank += 1

    def Options(self):
        """
        Presents the menu options for an ARTIST. 
        Calls the appropriate function according to the menu choice.
        """
        while(True):
            menuChoice = 0

            # menu options
            print("\n\tARTIST MENU")
            print("1) Add a song")
            print("2) Find your top fans")
            print("3) Find your top playlists")
            print("4) Log Out")

            menuChoice = input("Choose an option: ")

            if menuChoice == "1":
                self.addSong()
            elif menuChoice == "2":
                self.findTopFan()
            elif menuChoice == "3":
                self.findTopPlaylist()
            elif menuChoice == "4":
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
                    
        # Stores songs
        Search_S = {}
        # Stores Playlist
        Search_P = {}
        x = keywords.split(" ")
        for k in x:
            self.cursor.execute("SELECT * FROM songs s WHERE title LIKE ? COLLATE NOCASE ;", ('%'+ k + '%',))
            s = self.cursor.fetchall()
            self.cursor.execute("SELECT * FROM playlists WHERE title LIKE ? COLLATE NOCASE ;", ('%'+ k+ '%',))
            p = self.cursor.fetchall()

            # Checks for how many times a song occurs
            for i in s:
                if i[0] not in Search_S:
                    # Creates Class to store song in dictionary
                    song = Track_Song_Playlist(i[0] ,i[1] , i[2], 1 , "song")
                    Search_S[i[0]] = song
                else:
                    # Adds one to the number of matches in the Track_Song_Playlist class
                    Search_S[i[0]].no_of_matches += 1

            for k in p:
                if k[0] not in Search_P:
                    # Creates Class to store playlist in dictionary
                    duration = self.total_duration(k[0])
                    playlist = Track_Song_Playlist(k[0] ,k[1] , duration, 1 , "playlist")
                    Search_P[k[0]] = playlist
                else:
                    # Adds one to the number of matches in the Track_Song_Playlist class
                    Search_P[k[0]].no_of_matches += 1


        sortedPSlist = self.Create_new_table_p_s_duration(Search_S,Search_P)

        if len(sortedPSlist) < 5:
            self.displayall(sortedPSlist)
        else:
            self.displayfive(sortedPSlist)
        
        self.selection(sortedPSlist)

#-------------------------------------------------------------------------------------------
    def total_duration(self, id):
        #total duration of playlist
        self.cursor.execute("SELECT SUM(s.duration) FROM songs s, playlists p , plinclude l WHERE p.pid = ? AND p.pid = l.pid AND l.sid = s.sid ;", (id,))
        t_duration = self.cursor.fetchone()
        return t_duration[0]            
#--------------------------------------------------------------------------------------------------------------------
    # Returns tuple of ordered matches of songs and playlists
    def Create_new_table_p_s_duration(self , songs , playlist):
        # Create table to store songs and playlists
        self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS songs_playlist(
                                    id INT,
                                    title CHAR,
                                    duration INT,
                                    Match INT ,
                                    type CHAR,
                                    PRIMARY KEY(id,type)
                                )
                             """)
        
        # Insert songs into the new table
        for s in songs:
            self.cursor.execute(""" 
                                    INSERT INTO songs_playlist VALUES (?,?,?,?,?)
                                """, (songs[s].id , songs[s].title, songs[s].duration , songs[s].no_of_matches , songs[s].type,))
        
        #  Insert playlist into the playlist
        for p in playlist:
            self.cursor.execute(""" 
                                    INSERT INTO songs_playlist VALUES (?,?,?,?,?)
                                """, (playlist[p].id , playlist[p].title, playlist[p].duration , playlist[p].no_of_matches , playlist[p].type,))
        
        # Order the table based on number of matches
        self.cursor.execute("""SELECT id , title , duration , type 
                                FROM songs_playlist
                                ORDER BY Match
                                DESC ;   
                                """)
        
        songs_playlist_combine = self.cursor.fetchall()
        # Deletes table after search

        self.cursor.execute("""
                                DROP TABLE songs_playlist ;
        """)

        return songs_playlist_combine
    #----------------------------------------------------------------------------------------------------------------------------------------
    def displayfive(self,SPlist):
        #prints top five songs and playlists
         # id ,title, duration, type
        indx = 1
        for sp in SPlist:
            if indx <= 5:
                print(indx, ") " + "| Type: "+ sp[3] + "| ID:", sp[0], "| Title:", sp[1], "| Duration:", sp[2])
                indx += 1
            else:
                break

    #------------------------------------------------------------------------------------------------------------------------------------
    def displayall(self,SPlist):
        indx = 1
        for sp in SPlist:
            print(str(indx) + ") " + "Type: "+ sp[3] + " | ID:", sp[0], "| Title:", sp[1], "| Duration:", sp[2])
            indx += 1
    # #-------------------------------------------------------------------------------------------------------------------------------

    def selection(self, SPList):
        """
        Based on user selection do appropriate action.
        """
        choice = ""
        while choice != "q":

            #options
            print("\n\tSELECTION MENU")
            print("Select a Playlist or Song (input a number")
            print("Input 's' to Display All Results")
            print("Input 'q' to Exit Selection Menu")
            choice = input("Select: ")

            if choice.isdigit():
                c = int(choice) - 1
                item = SPList[c]
                if item[3] == "song":
                    self.songSelected(item)
                    break
                elif item[3] == "playlist":
                    self.playlistSelected(item)
                    break
            elif choice.lower() == "q":
                print("\nQuitting selection menu...")
                break
            elif choice.lower() == "s":
                self.displayall(SPList)
            else:
                print("Invalid option! Try again.")
                continue
    #-----------------------------------------------------------------------------------------
    def songSelected(self, song):
        # song actions: 
        # (1) listen to it: listening event is recorded within the current session of the user (if a session has already started for the user) or within a new session (if not)
        #                   : When starting a new session, follow the steps given for starting a session.
        #                   : A listening event is recorded by either inserting a row to table listen or increasing the listen count in this table by 1.
        #  (2) see more information: Artist: [name] SongId:[id] , STitle:[title], SDuration:[duration] ,PlaylistSongIncluded [list].
        #  (3) add it to a playlist: When adding a song to a playlist, the song can be added to an existing playlist owned by the user (if any) or to a new playlist.
        #                           :When it is added to a new playlist, a new playlist should be created with a unique id (created by your system) and the uid set to the id of the user and a title should be obtained from input. 
        entered = ""
        while entered != "4":

            #options
            print("\n\tSONGS")
            print(" 1) Listen to song \n 2)See more information\n 3) Add song to playlist\n 4)Exit this menu")
            entered = input("Enter you choice: ")

            if entered == "1":
                print("Listen to song function")
            elif entered == "2":
                self.moreInfo(song)
            elif entered == "3":
                print("Add song to playlist function")
            elif entered == "4":
                print("\nQuitting songs menu...")
                break
            else:
                print("Invalid option! Try again.")
                continue
    #-----------------------------------------------------------------------------------
    def moreInfo(self,song):
        # song (id, title, duration, type)
        #songs(sid, title, duration)
        #playlists(pid, title, uid)
        #plinclude(pid, sid, sorder)
        # see more information about it: Artist: [name] SongId:[id] , STitle:[title], SDuration:[duration] ,PlaylistSongIncluded [list].
        self.cursor.execute("SELECT a.name FROM songs s, artists a, perform p WHERE s.sid = ? AND s.sid = p.sid AND p.aid = a.aid;", (song[0],))
        Aname = self.cursor.fetchone()

        self.cursor.execute("SELECT p.title FROM playlists p, songs s, plinclude l WHERE s.sid = ? AND s.sid = l.sid AND l.pid = p.pid;",(song[0],) )
        songIncluded = self.cursor.fetchall()

        

        print()
        pass


    #-----------------------------------------------------------------------------------
    def playlistSelected(self, playlist):
        # query to return all songs in playlist.
        # using fetchall create a list of them
        # ask the user to enter which song to play and call songSelected to do song actions
        # if user doesnt want to play any song in playlist, quit menu
        #songs(sid, title, duration)

        self.cursor.execute("SELECT s.sid, s.title, s.duration FROM playlists p, songs s, plinclude l WHERE p.title = ? AND p.pid = l.pid AND l.sid = s.sid", (playlist[1],))
        l = self.cursor.fetchall()
        tohold = []
        for i in l:
            song = Track_Song_Playlist(i[0] ,i[1] , i[2], 1 , "song")
            tohold.append((song.id,song.title,song.duration, song.type))
        self.displayall(tohold)
        self.selection(tohold)
        

        pass
#=============================================================================================================================================  
    def Options(self):
        """
        Presents the menu options for a USER. 
        Calls the appropriate function according to the menu choice.
        """
        while(True):
            menuChoice = 0

            # menu options
            print("\n\tUSER MENU")
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

class Track_Song_Playlist:
    def __init__(self, id , title , duration, no_of_matches ,type):
        self.id = id
        self.title = title
        self.duration = duration
        self.no_of_matches = no_of_matches
        self.type = type
        self.session_no = None
#================================================================================================================

def main():
    conn = sqlite3.connect('proj.db')

    c = conn.cursor()
    execFile('prj-tables.sql',c)
    execFile('test-data.sql',c )
    
    while(True):
        person = loginScreen(c , conn)
        if(person is not None):
            person.Options()
        else:
            break

    conn.commit()
    conn.close()


if __name__ ==  '__main__':
    main()
