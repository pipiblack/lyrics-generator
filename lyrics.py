from imports import *
class music():
    def __init__(self, path):
        self.path = path
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.path)
        self.player.set_media(self.media)

        self.lyrics = [] 

    def load_lyrics(self, lyrics):
        self.lyrics = lyrics

    def get_lyrics_from_genius(self, title, artist):
        genius = lyricsgenius.Genius("YOUR_ACCESS_TOKEN_HERE")  
        song = genius.search_song(title, artist)
        if song:
            return song.lyrics
        else:
            return None

    def decode_lyrics(self):
        title = "Perfect" 
        artist = "Ed Sheeran" 

        lyrics_text = self.get_lyrics_from_genius(title, artist)

        if lyrics_text:
            self.lyrics = [line.split() for line in lyrics_text.split('\n')]

    def play_with_lyrics(self):
        self.player.play()

        for line in self.lyrics:
            for word in line:
                print(word, end=" ", flush=True)
                time.sleep(0.5) 
            print()
            time.sleep(1)  

    def stop_music(self):
        self.player.stop()

path = "/Users/georgengure/Downloads/y2mate.com - Ed Sheeran  Perfect Official Music Video.mp3"
my_music = music(path)

my_music.decode_lyrics()

my_music.play_with_lyrics()

# my_music.stop_music() # Uncomment this line to stop the music
