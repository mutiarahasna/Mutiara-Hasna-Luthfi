guests = ['Andi', 'Dewi', 'Citra']

print("Kabar gembira! Kami menemukan meja makan yang lebih besar.")

guests.insert(0, 'Edo')

guests.insert(2, 'Fara')

guests.append('Gita')

# 5. Mencetak ulang pesan undangan untuk semua tamu
print(f"\nTotal tamu saat ini ada {len(guests)} orang:")
for guest in guests:
    print(f"Halo {guest}, Anda diundang untuk makan malam.")