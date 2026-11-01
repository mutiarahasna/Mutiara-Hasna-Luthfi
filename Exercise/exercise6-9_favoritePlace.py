favorite_places = {
    'andi': ['bali', 'bandung', 'yogyakarta'],
    'siti': ['raja ampat', 'lombok'],
    'budi': ['malang'],
}

for name, places in favorite_places.items():
    print(f"\nTempat-tempat favorit {name.title()} adalah:")
    for place in places:
        print(f"\t- {place.title()}")