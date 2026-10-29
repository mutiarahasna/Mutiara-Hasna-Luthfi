guests = ['Edo', 'Andi', 'Fara', 'Dewi', 'Citra', 'Gita']

print("Maaf, meja baru tidak tiba tepat waktu. Kami hanya bisa mengundang 2 orang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, kami harus membatalkan undangan Anda.")

print(f"\n{guests[0]}, Anda masih diundang.")
print(f"{guests[1]}, Anda masih diundang.")

del guests[0]
del guests[0] 

print("\nDaftar tamu akhir:", guests)