# music

## request
As user
I want be able to ADD tracks to my music library and search tracks
The search should match either the track or Artist

## integration
```
class MusicLibrary:
    parameters: none
    public properties: 1.a list of instances of Track

    def add(self, track):
        paramenters: 1.an instance of Track
        actions:     1.append to the tracks list
        returns:     nothing

    def search(self, keyword):
        paramenters: 1.string contaning either the artist or tittle
        actions:     1.get tracks list
        returns:     a list of instances of track that match the keyword

class Track:
    paramenters: 1.string title 2.string artist 
    public properties: none

    def matches(self, keyword):
        paramenters: 1.string contaning either the artist or tittle
        returns:    true if the keyword matches either the title or artist
```
    
## code signature
```python
class MusicLibrary():
    def __init__(self):
        pass

    def add(self, track):
        pass

    def search(self, keyword):
        pass

class Track():
       def __init__(self, title, artist):
        pass

    def matches(self, keyword):
        pass
```

## tests
```python
"""
given a track or multple tracks - add it to the list in the music library
"""
def test_add_track(): pass
"""
given a keyword - search for the match/es track/s
"""
def test_search_for_track(): pass
"""
given a  - y
"""
```
