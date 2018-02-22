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
from copy import deepcopy

class Song:
    def __init__(self, track, genre, artist, album, release_year, mood):
        """
        -------------------------------------------------------
        Initializes Song class.
        Use: song = Song(genre, name, artist, album, release_year, mood)
        -------------------------------------------------------
        Preconditions:
            _track - The actual music itself
            _name - The name of the song
            _genre - The song's genre
            _artist - The song's artist
            _album - Album of which the song is from
            _release_year - The year when the song was released
            _mood - How does it make you feel?
        Postconditions:
            Initializes a song that contains the music file, name,
            genre, artist, album name, release year, and mood.
        -------------------------------------------------------
        """
        assert track is string
    
        return