number = input("Masukkan sebuah angka, dan saya akan cek kelipatannya: ")
number = int(number)

if number % 10 == 0:
    print(f"\nAngka {number} adalah kelipatan 10.")
else:
    print(f"\nAngka {number} bukan kelipatan 10.")