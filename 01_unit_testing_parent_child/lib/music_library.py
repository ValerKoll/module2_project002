class MusicLibrary():
    def __init__(self):
        self.tracks_list = []

    def add(self, track):
        self.tracks_list.append(track)

    def search(self, keyword):
        #for i in self.tracks_list:
        #    if i in 
        return [(i.artist, i.title) for i in self.tracks_list if keyword in i.artist]