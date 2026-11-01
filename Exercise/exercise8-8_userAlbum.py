def make_album(artist_name, album_title, num_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_songs:
        album['songs'] = num_songs
    return album

print("Masukkan informasi album musik Anda.")
print("(Ketik 'q' kapan saja untuk keluar)\n")

while True:
    artist = input("Nama Artis: ")
    if artist.lower() == 'q':
        break
        
    title = input("Judul Album: ")
    if title.lower() == 'q':
        break
        
    songs_input = input("Jumlah lagu (tekan Enter jika tidak tahu): ")
    if songs_input.lower() == 'q':
        break
        
    if songs_input:
        album_info = make_album(artist, title, int(songs_input))
    else:
        album_info = make_album(artist, title)
        
    print("\nDictionary Album yang Berhasil Dibuat:")
    print(album_info)
    print("-" * 40)