# classe principal
class Item:
    def __init__(self, title: str, playing_time: str, comment: str):
        self._title = title
        self._playing_time = str(playing_time)
        self._got_it = False # se possuimos esse item
        self._comment = comment

    # adicionar um comentario sobre este item
    def setComment(self, comment: str):
        self._comment = comment

    def getComment(self) -> str:
        return self._comment

    # configura o flag que indica se possuimos esse item
    def setOwn(self, own_it: bool):
        self._got_it = own_it

    def getOwn(self) -> bool:
        return self._got_it


class Cd(Item):
    def __init__(self, title: str, playing_time: str, comment: str, artist: str, number_of_tracks):
        super().__init__(title, playing_time, comment)
        self._artist = artist
        self._number_of_tracks = number_of_tracks

    def getArtist(self) -> str:
        return self._artist

    def getNumberOfTracks(self):
        return self._number_of_tracks

    def print(self):
        print(f"CD: {self._title} ({self._playing_time} min)")
        if self._got_it:
            print("*")
        else:
            print()

        print(f"    Artista: {self._artist}")
        print(f"    tracks: {self._number_of_tracks}")
        print(f"    comentario: '{self._comment}'")


class Video(Item):
    def __init__(self, title: str, playing_time: str, comment: str, director: str):
        super().__init__(title, playing_time, comment)
        self._director = director

    def getDirector(self) -> str:
        return self._director

    def print(self):
        print(f"Video: {self._title} ({self._playing_time} min)")
        if self._got_it:
            print("*")
        else:
            print()

        print(f"    Artista: {self._director}")
        print(f"    comentario: '{self._comment}'")


class Game(Item):
    def __init__(self, title: str, playing_time: str, comment: str, number_of_players):
        super().__init__(title, playing_time, comment)
        self._number_of_players = number_of_players

    def print(self):
        print(f"Game: {self._title} ({self._playing_time})")
        if self._got_it:
            print("*")
        else:
            print()

        print(f"    Number of players: {self._number_of_players}")
        print(f"    comentario: '{self._comment}'")

