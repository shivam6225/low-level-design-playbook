from song import Song
from typing import List
from PlaylistIterator import PlaylistIterator

class Playlist:
    def __init__(self):
        self.__playlist:List[Song] = []

    def add_song(self, song:Song):
        self.__playlist.append(song)

    def create_iterator(self) -> PlaylistIterator:
        return PlaylistIterator(self.__playlist)


playlist = Playlist()
playlist.add_song(Song("song1"))
playlist.add_song(Song("song2"))
playlist.add_song(Song("song3"))
playlist.add_song(Song("song4"))

iterator = playlist.create_iterator()

while iterator.has_next():
    print(iterator.next().get_title())
