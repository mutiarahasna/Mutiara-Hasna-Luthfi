favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

coders_to_poll = ['jen', 'sarah', 'budi', 'edward', 'siti', 'phil', 'andi']

for coder in coders_to_poll:
    if coder in favorite_languages.keys():
        print(f"Halo {coder.title()}, terima kasih sudah meluangkan waktu untuk mengisi polling!")
    else:
        print(f"Halo {coder.title()}, ayo ikuti polling bahasa pemrograman favorit sekarang!")