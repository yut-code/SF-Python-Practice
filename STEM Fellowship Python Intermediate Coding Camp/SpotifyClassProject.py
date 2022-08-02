#PROJECT: SPOTIFY CLASS

#In this project you will build classes to mimic a spotify (or any music library) database! You should implement classes for users, playlists, and songs. Feel free to ignore the methods we ask for below and go your own direction. Make sure to consider user errors (ex. making a playlist with the same name as an existing one, trying to remove a song from a playlist that doesn't have that song, etc.)

class User:
  accountType = 'Spotify Premium'
  numUsers = 0
  def __init__(self, username, password):
    #TODO: I suggest storing their playlists in a list of playlist objects. Note that their "liked songs" should operate like a playlist and can just be a playlist object. 
    self.liked_songs = []
    self.numUsers += 1
    self.followers = 0
    self.following = 0
    self.username = username
    self.password = password
    self.playlists = []
    
  def like_song(self,song):
    #TODO: add song to liked songs playlist
      self.liked_songs.append(song)
    
  def get_liked_songs(self):
    #TODO: retrieve all liked songs
      return self.liked_songs
    
  def new_playlist(self,name):
    #TODO: make a new playlist for the user
      self.playlists.append(name)
    
  def get_playlist(self,name):
    #TODO: return a playlist object by looking for its name
    return self.playlists.index(name)
    
  def start_following(self, artist):
    self.following += 1
    
  def __str__(self):
    output

class Playlist:
  def __init__(self,name):
    #TODO: I suggest storing the songs as a list of song objects.

  def add(self,song):
    #TODO: add song to the playlist

  def remove(self,song):
    #TODO: remove song from the playlist if it's in the playlist

  def get_duration(self):
    #TODO: return total duration of playlist in seconds

  def __str__(self):
    #TODO

class Song:
  
  def __init__(self,name, artist, duration):
    #TODO
  
  def __str__(self):
    #TODO

#Uncomment the following to begin testing your code! This is definitely not comprehensive testing. You should add your own code to test your work!

# song1 = Song("Mistletoe","Justin Bieber","120")
# song2 = Song("Bohemian Rhapsody","Queen","320")
# song3 = Song("Butter","BTS","200")
# song4 = Song("Cool","Jonas Brothers","90")
# song5 = Song("Blue Suede Shoes","Carl Perkins","150")

# user1 = User("ilovecats","cats4life")
# print(user1)
# user1.new_playlist("Party Music")
# user1.get_playlist("Party Music").add(song1)
# print(user1)
# user1.like_song(song2)
# print(user1)

