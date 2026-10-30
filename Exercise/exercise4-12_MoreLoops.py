my_foods = ['ayam geprek', 'bubur', 'cireng', 'donat']
friend_foods = my_foods[:]
friend_foods.append('gado-gado')

# Loop untuk mencetak makananmu
print("My favorite foods are:")
for food in my_foods:
    print(food)

# Loop untuk mencetak makanan temanmu
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)