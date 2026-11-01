favorite_numbers = {
    'mutilara': [7, 20],
    'budi': [5, 12, 99],
    'siti': [3],
    'andi': [8, 11],
    'dewi': [19, 45, 77],
}

for name, numbers in favorite_numbers.items():
    print(f"\nNomor favorit {name.title()} adalah:")
    for number in numbers:
        print(f"\t{number}")