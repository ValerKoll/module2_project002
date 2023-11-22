from lib.music_library import *
from unittest.mock import Mock


def test_add_track():
    musiclibrary = MusicLibrary()
    
    fake_track = Mock()
    fake_track.artist = 'Hered'
    fake_track.title = 'Not my cup of tea'
    
    musiclibrary.add(fake_track)
    assert musiclibrary.tracks_list[0].artist == "Hered"
    
def test_search_for_track():
    musiclibrary = MusicLibrary()
    
    fake_track1 = Mock()
    fake_track2 = Mock()
    fake_track3 = Mock()
    fake_track1.artist = 'Hered'
    fake_track1.title = 'Not my cup of tea'
    fake_track2.artist = 'Robert'
    fake_track2.title = 'Not my cup of tea'
    fake_track3.artist = 'Mike'
    fake_track3.title = 'Not my cup of tea'
    musiclibrary.add(fake_track1)
    musiclibrary.add(fake_track2)
    musiclibrary.add(fake_track3)
    
    assert musiclibrary.search('Mike') == [("Mike", 'Not my cup of tea')]