def make_shirt(size='large', message='I love Python'):
    """Membuat kaos dengan nilai default ukuran large dan pesan I love Python."""
    print(f"\nMembuat kaos ukuran {size.upper()} dengan tulisan: '{message}'")

make_shirt()

make_shirt(size='medium')

make_shirt(size='small', message='Industrial Engineering UNS')