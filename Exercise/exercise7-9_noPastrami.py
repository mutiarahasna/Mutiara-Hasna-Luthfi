sandwich_orders = [
    'tuna sandwich', 'pastrami sandwich', 'turkey sandwich', 
    'pastrami sandwich', 'cheese sandwich', 'pastrami sandwich'
]
finished_sandwiches = []

print("Mohon maaf, toko roti sedang kehabisan pastrami hari ini!\n")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Membuat {current_sandwich}...")
    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang berhasil disiapkan:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")