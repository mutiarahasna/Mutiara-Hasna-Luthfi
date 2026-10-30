buffet_foods = ('fried rice', 'fried chicken', 'soup', 'noodles', 'salad')

print("Original Menu:")
for food in buffet_foods:
    print(food)

# Saat mencoba mengubah item error
# buffet_foods[0] = 'burger' 

#Mengubah menu dengan menulis ulang tuple-nya
buffet_foods = ('fried rice', 'fried chicken', 'soup', 'steak', 'sushi')

print("\nRevised Menu:")
for food in buffet_foods:
    print(food)