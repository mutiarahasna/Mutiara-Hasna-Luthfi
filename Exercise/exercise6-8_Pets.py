pet_1 = {
    'kind' : 'anjing',
    'owner' : 'budi',
}

pet_2 = {
    'kind' : 'kucing',
    'owner' : 'siti',
}

pet_3 ={
    'kind' : 'burung',
    'owner' : 'andi',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Jenis hewan peliharaan: {pet['kind'].title()}")
    print(f"Pemilik hewan peliharaan: {pet['owner'].title()}\n")