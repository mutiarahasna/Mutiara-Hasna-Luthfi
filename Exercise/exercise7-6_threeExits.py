prompt = "\nMasukkan topping pizza:"
prompt += "\n(Ketik 'quit' untuk selesai) "

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"Menambahkan {topping}!")