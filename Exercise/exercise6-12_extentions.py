cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '580.000 jiwa',
        'currency': 'Rupiah (IDR)',
        'language': 'Bahasa Indonesia / Jawa',
        'fact': 'Dikenal sebagai Kota Batik dan pusat budaya Jawa yang kental.',
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'currency': 'Yen (JPY)',
        'language': 'Bahasa Jepang',
        'fact': 'Merupakan salah satu wilayah metropolitan paling padat dan modern di dunia.',
    },
    'paris': {
        'country': 'perancis',
        'population': '2,1 juta jiwa',
        'currency': 'Euro (EUR)',
        'language': 'Bahasa Perancis',
        'fact': 'Terkenal dengan Menara Eiffel dan dijuluki sebagai Kota Cinta.',
    },
}

print("=" * 45)
print("  INFORMASI KOTA-KOTA BESAR DI DUNIA (DATABASE)")
print("=" * 45)

for city_name, city_info in cities.items():
    print(f"\n🏙️ Kota: {city_name.upper()}")
    print(f"   • Negara       : {city_info['country'].title()}")
    print(f"   • Populasi     : {city_info['population']}")
    print(f"   • Mata Uang    : {city_info['currency']}")
    print(f"   • Bahasa Utama : {city_info['language']}")
    print(f"   • Fakta Unik   : {city_info['fact']}")
    print("-" * 45)