import parkir

if __name__ == "__main__":
    print("=== PROGRAM HITUNG TARIF PARKIR ===")
    
    # Mengambil input langsung dari pengguna di terminal
    input_jenis = input("Masukkan jenis kendaraan (motor/mobil): ")
    input_masuk = int(input("Masukkan jam masuk (angka 0-23): "))
    input_keluar = int(input("Masukkan jam keluar (angka 0-23): "))
    
    # Memanggil fungsi hitung_tarif_parkir dengan data yang diinput pengguna
    hasil_biaya = hitung_tarif_parkir(input_jenis, input_masuk, input_keluar)
    
    # Menampilkan hasil ke layar
    if isinstance(hasil_biaya, int):
        print(f"\n--- HASIL PERHITUNGAN ---")
        print(f"Kendaraan : {input_jenis.capitalize()}")
        print(f"Durasi    : {input_keluar - input_masuk} jam")
        print(f"Total Biaya: Rp {hasil_biaya:,}")
    else:
        print(f"\n{hasil_biaya}")