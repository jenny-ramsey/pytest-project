from lib.music_tracker import MusicTracker

"""As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
"""

# Start with the example:

# When we create a new music tracker it should start with no tracks 
# then we can add tracks we have listened to and then see a list of all added tracks

def test_no_tracks_start(): 
    tracker =  MusicTracker()
    assert tracker.get_tracks() == [] 

def test_add_one_track():
    tracker =  MusicTracker()
    tracker.add_tracks("Waterloo by ABBA") 
    assert tracker.get_tracks() == ["Waterloo by ABBA"]

def test_add_multiple_tracks():
    tracker =  MusicTracker()
    tracker.add_tracks("Waterloo by ABBA") 
    tracker.add_tracks("Believe by Cher")
    assert tracker.get_tracks() == ["Waterloo by ABBA", "Believe by Cher"]

