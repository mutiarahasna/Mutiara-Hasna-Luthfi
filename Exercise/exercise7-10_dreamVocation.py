dream_vacations = {}

polling_active = True

while polling_active:
    name = input("\nSiapa nama kamu? ")
    response = input("Jika kamu bisa mengunjungi satu tempat di dunia, kamu ingin pergi ke mana? ")
    
    dream_vacations[name] = response
    
    repeat = input("Apakah ada orang lain yang ingin mengikuti survei? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- HASIL SURVEI LIBURAN IMPIAN ---")
for name, place in dream_vacations.items():
    print(f"{name.title()} ingin sekali berlibur ke {place.title()}.")