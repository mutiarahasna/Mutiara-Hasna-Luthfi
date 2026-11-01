rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

print("--- Informasi Sungai dan Negara ---")
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\n--- Nama-nama Sungai ---")
for river in rivers.keys():
    print(river.title())

print("\n--- Nama-nama Negara ---")
for country in rivers.values():
    print(country.title())