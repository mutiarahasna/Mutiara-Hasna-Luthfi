person_1 = {
    'first_name': 'Mutiara',
    'last_name': 'Luthfi',
    'age': 18,
    'city': 'Surakarta',
}

person_2 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 20,
    'city': 'Yogyakarta',
}

person_3 = {
    'first_name': 'Siti',
    'last_name': 'Rahma',
    'age': 19,
    'city': 'Semarang',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"\nNama: {full_name}")
    print(f"\tUmur: {age} tahun")
    print(f"\tKota: {city}")