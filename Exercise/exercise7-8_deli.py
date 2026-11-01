sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'turkey sandwich', 'cheese sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sedang membuat {current_sandwich} kamu.")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich berikut telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")