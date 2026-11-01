glossary = {
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'dictionary': 'Kumpulan pasangan key-value (kunci dan nilai) untuk menyimpan informasi terkait.',
    'list': 'Kumpulan item yang disimpan dalam urutan tertentu.',
    'loop': 'Blok kode yang digunakan untuk mengulang sekumpulan instruksi secara otomatis.',
    'if statement': 'Pernyataan kondisional yang digunakan untuk memeriksa apakah suatu kondisi bernilai True atau False.',
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"\t{meaning}")