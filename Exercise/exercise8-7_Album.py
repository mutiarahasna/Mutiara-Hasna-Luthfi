def make_album(artist_name, album_title, songs=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if songs:
        album['num_songs'] = songs
    return album

album_1 = make_album('tulus', 'manusia')
album_2 = make_album('sheila on 7', 'kisah klasik untuk masa depan', 12)
album_3 = make_album('coldplay', 'A Head Full of Dreams')

print(album_1)
print(album_2)
print(album_3)