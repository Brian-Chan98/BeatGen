"""
-------------------------------------------------------
song_utilities.py
Utilities for working with a Song object.
-------------------------------------------------------
Author:  Sathusan Kandasamy
ID:      170408870
Email:   kand8870@mylaurier.ca
__updated__ = "2018-02-24"
-------------------------------------------------------
"""
#[import statements]
from song import Song

#[constants]
# self, track, name, genre, artist, album, release_year, mood
def get_song():
    """
    -------------------------------------------------------
    Creates a Song object by requesting data from a user.
    Use: song = get_song()
    -------------------------------------------------------
    Postconditions:
        returns
        song - a completed song object (Song).
    -------------------------------------------------------
    """
    track = input("Track: ")
    name = input("Name: ")
    print("Genre")
    print(Song.genres())
    genre = int(input(": "))
    artist = input("Artist: ")
    album = input("Album: ")
    release_year = int(input("Release year (int): "))
    mood = int(input("Mood: "))
    song = Song(track, name, genre, artist, album, release_year, mood)
    return song

def read_song(line):
    """
    -------------------------------------------------------
    Creates and returns a song object from a line of string data.
    Use: song = read_song(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of song data in the format
          track|name|genre|artist|album|release_year|mood (str)
    Postconditions:
        returns
        song - contains the data from line (Song)
    -------------------------------------------------------
    """
    data = line.strip().split("|")
    song = Song(data[0], data[1], data[2], data[3], data[4], int(data[5]), data[6])
    return song

def read_songs(file_variable):
    """
    -------------------------------------------------------
    Reads a file of song strings into a list of Song objects.
    Use: songs = read_songs(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - a file of song data (file)
    Postconditions:
        returns
        songs - a list of song objects (list of Songs)
    -------------------------------------------------------
    """
    file_variable.seek(0)
    songs = []

    for line in file_variable:
        song = read_song(line)
        songs.append(song)
    return songs

def write_songs(file_variable, songs):
    """
    -------------------------------------------------------
    Writes a list of song objects to a file.
    Use: write_songs(file_variable, songs)
    -------------------------------------------------------
    Preconditions:
        file_variable - an open file of food data (file)
        songs - a list of Song objects (list of Songs)
    Postconditions:
        file_variable contains the objects in songs as strings in the format
          track|name|genre|artist|album|release_year|mood (str)
    -------------------------------------------------------
    """
    for song in songs:
        song.write(file_variable)
    return

def by_genre(songs, genre):
    """
    -------------------------------------------------------
    Creates a list of songs by genre.
    Use: v = by_genre(songs, genre)
    -------------------------------------------------------
    Preconditions:
        songs - a list of Song objects (list of Song)
        genre - a song's genre (int)
    Postconditions:
        returns
        genres - Song objects from songs that are of a particular genre (list of Songs)
    -------------------------------------------------------
    """
    assert genre in range(len(Song.GENRE))
    
    genres = []
    
    for i in songs:
        if i.genre == genre:
            genres.append(i)

    return genres

def by_artist(songs, artist):
    """
    -------------------------------------------------------
    Creates a list of songs by artist.
    Use: v = by_artist(songs, artist)
    -------------------------------------------------------
    Preconditions:
        songs - a list of Song objects (list of Song)
        artist - a song's artist (str)
    Postconditions:
        returns
        artists - Song objects from songs that are by a particular artist (list of Songs)
    -------------------------------------------------------
    """
#     assert genre in range(len(Song.GENRE))
    
    artists = []
    
    for i in songs:
        if i.artist == artist:
            artists.append(i)

    return artists

def by_album(songs, album):
    """
    -------------------------------------------------------
    Creates a list of songs by album.
    Use: v = by_album(songs, album)
    -------------------------------------------------------
    Preconditions:
        songs - a list of Song objects (list of Song)
        album - a song's album (str)
    Postconditions:
        returns
        albums - Song objects from songs that are from a particular album (list of Songs)
    -------------------------------------------------------
    """
#     assert genre in range(len(Song.GENRE))
    
    albums = []
    
    for i in songs:
        if i.album == album:
            albums.append(i)

    return albums

def by_release_year(songs, release_year):
    """
    -------------------------------------------------------
    Creates a list of songs by origin.
    Use: v = by_release_year(songs, release_year)
    -------------------------------------------------------
    Preconditions:
        songs - a list of Song objects (list of Song)
        release_year - a song's release year (int)
    Postconditions:
        returns
        release_years - Song objects from songs that are from a particular year (list of Songs)
    -------------------------------------------------------
    """
#     assert genre in range(len(Song.GENRE))
    
    release_years = []
    
    for i in songs:
        if i.release_year == release_year:
            release_years.append(i)

    return release_years

def by_mood(songs, mood):
    """
    -------------------------------------------------------
    Creates a list of songs by mood.
    Use: v = by_mood(songs, mood)
    -------------------------------------------------------
    Preconditions:
        songs - a list of Song objects (list of Song)
        mood - a song's mood (str)
    Postconditions:
        returns
        moods - Song objects from songs that are a particular mood (list of Songs)
    -------------------------------------------------------
    """
#     assert genre in range(len(Song.GENRE))
    
    moods = []
    
    for i in songs:
        if i.mood == mood:
            mood.append(i)

    return moods

'''
Unfinished universal search below
'''
# def food_search(foods, origin, max_cals, is_veg):
#     """
#     -------------------------------------------------------
#     Searches for foods that fit certain conditions.
#     Use: result = food_search(foods, origin, max_cals, is_veg)
#     -------------------------------------------------------
#     Preconditions:
#         foods - a list of Food objects (list of Food)
#         origin - the origin of the food; if -1, accept any origin (int)
#         max_cals - the maximum calories for the food; if 0, accept any calories value (int)
#         is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
#     Postconditions:
#         returns
#         result - a list of foods that fit the conditions (list of Food)
#             foods parameter must be unchanged
#     -------------------------------------------------------
#     """
#     assert origin in range(-1, len(Food.ORIGIN))
#     
#     if origin != -1:
#         v = by_origin(foods, origin)
#     else:
#         v = foods
#     
#     result = []
#     for i in v:
#         if max_cals == 0:
#             if is_veg == True and i.is_vegetarian == True:
#                 result.append(i)
#             elif is_veg == False:
#                 result.append(i)
#         elif i.calories <= max_cals:
#             if is_veg == True and i.is_vegetarian == True:
#                 result.append(i)
#             elif is_veg == False:
#                 result.append(i)
#     return result