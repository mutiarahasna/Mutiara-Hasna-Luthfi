buah = "apel"
print("--- 1. Tes Kesamaan dan Ketidaksamaan ---")
print("Apakah buah == 'apel'? Prediksi True.")
print(buah == 'apel')

print("Apakah buah == 'jeruk'? Prediksi False.")
print(buah == 'jeruk') 

print("Apakah buah != 'mangga'? Prediksi True.")
print(buah != 'mangga') 


nama_depan = "Mutiara"
print("\n--- 2. Tes Menggunakan lower() ---")
print("Apakah nama_depan.lower() == 'mutiara'? Prediksi True.")
print(nama_depan.lower() == 'mutiara') 

print("Apakah nama_depan.lower() == 'hasna'? Prediksi False.")
print(nama_depan.lower() == 'hasna') 


umur = 18
print("\n--- 3. Tes Numerik ---")
print("Apakah umur == 18? True")
print(umur == 18) 

print("Apakah umur != 20? True")
print(umur != 20) 

print("Apakah umur > 21? False")
print(umur > 21) 

print("Apakah umur < 25? True")
print(umur < 25) 

print("Apakah umur >= 18? True")
print(umur >= 18) 

print("Apakah umur <= 17? False")
print(umur <= 17) 


nilai_teori = 85
nilai_praktik = 90
print("\n--- 4. Tes 'and' dan 'or' ---")
print("Apakah teori > 80 and praktik > 80? True")
print(nilai_teori > 80 and nilai_praktik > 80) 

print("Apakah teori > 90 or praktik > 80? True")
print(nilai_teori > 90 or nilai_praktik > 80) 


hobi_list = ["membaca", "menulis", "bernyanyi"]
print("\n--- 5. Tes Item di Dalam List ('in') ---")
print("Apakah 'bernyanyi' ada di dalam hobi_list? True")
print('bernyanyi' in hobi_list)  

print("Apakah 'memasak' ada di dalam hobi_list? False")
print('memasak' in hobi_list)  


print("\n--- 6. Tes Item Tidak di Dalam List ('not in') ---")
print("Apakah 'menggambar' tidak ada di dalam hobi_list? True")
print('menggambar' not in hobi_list) 

print("Apakah 'membaca' tidak ada di dalam hobi_list? False")
print('membaca' not in hobi_list) 