# 8-7
def make_album(artist_name, album_title, track_number=''):
    album = {
        'artist_name': artist_name,
        'album_title': album_title,
        }
    if track_number:
        album['track_number'] = int(track_number)
    return album

album_1 = make_album(artist_name='Maichael Jackson', album_title='Bad')
album_2 = make_album(artist_name='Maichael Jackson', album_title='Bad', track_number = 12)
print(album_1)
print(album_2)

# 8-8
active = True 

while active:
    stop = input("Do you want to continue? (yes/no)")
    if stop.lower() == "yes":
        artist = input("Please enter an artist name: ")
        album = input("Please enter his/her album name: ")
        album_dict = make_album(artist_name=artist, album_title=album)
        print(album_dict)
    else:
        active = False