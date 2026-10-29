def hitung_tarif_parkir(jenis_kendaraan, jam_masuk, jam_keluar):
    # Menghitung lama waktu parkir (dalam satuan jam)
    durasi = jam_keluar - jam_masuk
    
    # Antisipasi jika jam keluar melewati tengah malam (format 24 jam)
    if durasi < 0:
        durasi += 24
        
    # Mengubah teks jenis kendaraan menjadi huruf kecil semua
    jenis = jenis_kendaraan.lower()
    
    # Menentukan tarif dasar berdasarkan jenis kendaraan
    if jenis == "motor":
        tarif_awal = 2000   # Biaya jam pertama untuk motor
        tarif_per_jam = 1000 # Biaya tambahan per jam berikutnya
    elif jenis == "mobil":
        tarif_awal = 5000   # Biaya jam pertama untuk mobil
        tarif_per_jam = 3000 # Biaya tambahan per jam berikutnya
    else:
        return "Maaf, jenis kendaraan tidak dikenali (gunakan 'motor' atau 'mobil')."
        
    # Jika parkir kurang dari atau sama dengan 0 jam, dibulatkan menjadi 1 jam
    if durasi <= 0:
        durasi = 1
        
    # Menghitung total biaya keseluruhan
    if durasi == 1:
        total_tarif = tarif_awal
    else:
        sisa_jam = durasi - 1
        total_tarif = tarif_awal + (tarif_per_jam * sisa_jam)
        
    return total_tarif