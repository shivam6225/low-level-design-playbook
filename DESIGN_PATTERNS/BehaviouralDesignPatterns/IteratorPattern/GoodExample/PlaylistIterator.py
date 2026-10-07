from typing import List

from Iterator import Iterator
from song import Song

class PlaylistIterator(Iterator):
    def __init__(self,song_list:List[Song]):
        self.__song_list = song_list
        self.__position = 0

    def has_next(self):
        return self.__position < len(self.__song_list)

    def next(self) -> Song|None:
        while self.has_next():
            song = self.__song_list[self.__position]
            self.__position += 1
            return song
        return None

