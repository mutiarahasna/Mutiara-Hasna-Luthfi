countries = ['Jepang', 'Kanada', 'Mesir', 'Brasil', 'Australia']
print("Daftar awal:", countries)

countries.append('Jerman')
print("Setelah append('Jerman'):", countries)

countries.insert(1, 'Prancis')
print("Setelah insert di indeks 1:", countries)

del countries[0]
print("Setelah del indeks 0:", countries)

popped_country = countries.pop()
print(f"Negara yang di-pop: {popped_country}")
print("List setelah pop():", countries)

countries.remove('Mesir')
print("Setelah remove('Mesir'):", countries)

print("\nUrutan sementara (sorted):", sorted(countries))
print("List asli tidak berubah:", countries)

countries.reverse()
print("\nSetelah reverse():", countries)

countries.sort()
print("Setelah sort():", countries)

print(f"\nJumlah negara yang tersisa di list saat ini ada {len(countries)} buah.")