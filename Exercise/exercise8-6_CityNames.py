def city_country(city, country):
    """Mengembalikan string dengan format 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"

city1 = city_country('santiago', 'chile')
city2 = city_country('surakarta', 'indonesia')
city3 = city_country('tokyo', 'jepang')

print(city1)
print(city2)
print(city3)