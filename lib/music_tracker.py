class MusicTracker:
    def __init__(self):
        self.tracks = []

    def add_tracks(self, track):
        self.tracks.append(track)
    
    def get_tracks(self):
        return self.tracks