"""
-------------------------------------------------------
genres.py
Contains all the genre classes
-------------------------------------------------------
Author:  Sathusan Kandasamy
ID:      170408870
Email:   kand8870@mylaurier.ca
__updated__ = "2018-02-22"
-------------------------------------------------------
"""
# from copy import deepcopy

class Song:
    """
    Defines an object for a single song: track, name, genre, artist,
    album, release year, mood.
    """
    # Constants
    GENRE = ("Rock", "HipHop", "Pop", "Classical",
              "International", "R&B", "Soul", "Reggae",
              "Jazz", "Bollywood")

    @staticmethod
    def genres():
        """
        -------------------------------------------------------
        Creates a string list of genres in the format:
           0 Rock
           1 HipHop
           2 Pop
           ...
        Use: song = Song.genres()
        Use: print(Song.genres())
        -------------------------------------------------------
        Postconditions:
            returns
            string - A numbered list of valid musical genres.
        -------------------------------------------------------
        """
        string = ""
        
        for i in range(len(Song.GENRE)):
            string += """{:2d} {}
""".format(i, Song.GENRE[i])
        
        return string
    
    def __init__(self, track, name, genre, artist, album):
        """
        -------------------------------------------------------
        Initializes Song class.
        Use: song = Song(genre, name, artist, album, release_year, mood)
        -------------------------------------------------------
        Preconditions:
            track - The actual music itself
            name - The name of the song
            genre - The song's genre
            artist - The song's artist
            album - Album of which the song is from
        Postconditions:
            Initializes a song that contains the music file, name,
            genre, artist, album name, release year, and mood.
        -------------------------------------------------------
        """
        assert genre in range(len(Song.GENRE)), "Invalid genre ID"
        
        self.track = track
        self.name = name
        self.genre = genre
        self.artist = artist
        self.album = album
        
        return
    
    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares this song against another song for equality.
        Use: song == rs
        -------------------------------------------------------
        Preconditions:
            rs - [right side] song to compare to (Song)
        Postconditions:
            returns:
            result - True if track, name, genre, artist, album,
            release_year, and mood match False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.track, self.name, self.genre, self.artist,
                  self.album) == (
            rs.track, rs.name, rs.genre, rs.artist,
                  rs.album)
        return result
    
    def write(self, file_variable):
        """
        -------------------------------------------------------
        Writes a single line of food data to an open file.
        Use: f.write( file_variable )
        -------------------------------------------------------
        Preconditions:
            file_variable - an open file of food data (file)
        Postconditions:
            The contents of food are written as a string in the format
              name|origin|is_vegetarian to file_variable.
        -------------------------------------------------------
        """
        print("{}|{}|{}|{}|{}|{}|{}"
              .format(self.track, self.name, self.genre, self.artist,
                      self.album),
              file=file_variable)
        return