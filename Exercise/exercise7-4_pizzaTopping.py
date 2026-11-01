prompt = "\nMasukkan topping pizza yang kamu inginkan:"
prompt += "\n(Ketik 'quit' jika sudah selesai) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        print("\nTerima kasih! Pizza kamu sedang disiapkan.")
        break
    else:
        print(f"Menambahkan {topping} ke pizza kamu!")