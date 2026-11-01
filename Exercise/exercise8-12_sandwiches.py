def make_sandwich(*items):
    """Mencetak ringkasan pesanan sandwich dengan berbagai topping."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"  - {item}")

make_sandwich('keju', 'selada', 'tomat')
make_sandwich('daging asap', 'keju cheddar', 'saus barbecue', 'mayones')
make_sandwich('telur dadar')