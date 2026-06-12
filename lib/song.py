class Song:
    total_songs = 0
    unique_artists = set()
    unique_genres = set()
    genre_count = {}
    artist_count = {}

    def __init__(self,title,artist,genre):
        self.title = title
        self.artist = artist
        self.genre = genre

        song.total_songs += 1

        song.unique_artists.add(self.artist)
        song.unique_genres.add(self.genre)

        song.genre_counts[self.genre] = song.genre_counts.get(self.genre, 0) + 1
        song.artist_counts[self.artist] = song.artist_counts.get(self.artist, 0) + 1

        @classmethod
        def get_library_stats(cls):
            """Class method to access the global statistics."""
            return {
                "Total Songs": cls.total_songs,
                "Unique Artists": sorted(list(cls.unique_artists)),
                "Unique Genres": sorted(list(cls.unique_genres)),
                "Songs per Genre": cls.genre_counts,
                "Songs per Artist": cls.artist_counts
            }