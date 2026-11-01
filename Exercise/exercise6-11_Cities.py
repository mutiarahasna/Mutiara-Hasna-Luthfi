cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '580.000 jiwa',
        'fact': 'dikenal sebagai Kota Batik dan pusat budaya Jawa.',
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'merupakan salah satu wilayah metropolitan paling padat di dunia.',
    },
    'paris': {
        'country': 'perancis',
        'population': '2,1 juta jiwa',
        'fact': 'terkenal dengan Menara Eiffel dan julukan Kota Cinta.',
    },
}

city_name, city_info = '', '' 

for city_name, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    
    print(f"\nKota: {city_name.title()}")
    print(f"\tNegara: {country.title()}")
    print(f"\tPerkiraan Populasi: {population}")
    print(f"\tFakta Menarik: {fact}")