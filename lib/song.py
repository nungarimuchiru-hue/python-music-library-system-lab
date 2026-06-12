from os import name


class Song:
    count = 0
    total_songs = 0 
    artists = set()
    genres = set()
    genre_counts = {} # Added 's' to match the constructor usage
    artist_counts = {} # Added 's' to match the constructor usage

    def __init__(self,title,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.total_songs += 1
        Song.artists.add(self.artist)
        Song.genres.add(self.genre)

        Song.genre_counts[self.genre] = Song.genre_counts.get(self.genre, 0) + 1
        Song.artist_counts[self.artist] = Song.artist_counts.get(self.artist, 0) + 1

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