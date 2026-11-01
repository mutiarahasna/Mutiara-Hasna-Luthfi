glossary = {
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'dictionary': 'Kumpulan pasangan key-value untuk menyimpan informasi terkait.',
    'list': 'Kumpulan item yang disimpan dalam urutan tertentu.',
    'loop': 'Blok kode yang digunakan untuk mengulang sekumpulan instruksi.',
    'if statement': 'Pernyataan kondisional untuk memeriksa apakah suatu kondisi True atau False.',
    # 5 istilah baru
    'key': 'Nama unik yang digunakan untuk mengakses nilai dalam sebuah dictionary.',
    'value': 'Data yang diasosiasikan dengan sebuah key di dalam dictionary.',
    'tuple': 'List yang sifatnya permanen atau tidak dapat diubah (immutable).',
    'function': 'Blok kode terisolasi yang dirancang untuk menjalankan tugas tertentu.',
    'module': 'File berisi kode Python yang dapat diimpor ke program lain.',
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"\t{meaning}")