from typing import List
class Song:

    def __init__(self, title:str):
        self.__title = title

    def get_title(self):
        return self.__title


class Playlist:
    def __init__(self):
        self.__playlist:set[Song] = set()

    def add_song(self, song:Song):
        self.__playlist.add(song)

    def get_playlist(self):
        return self.__playlist

playlist = Playlist()
playlist.add_song(Song("song1"))
playlist.add_song(Song("song2"))
playlist.add_song(Song("song3"))

##This doesn't work with Set
#Client will need to change their Iterator Pattern 
for i in range(len(playlist.get_playlist())):
    print(playlist.get_playlist()[i].get_title())
