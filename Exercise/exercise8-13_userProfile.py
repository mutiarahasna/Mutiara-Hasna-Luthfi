def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal yang kita ketahui tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'mutiara', 'luthfi',
    major='Teknik Industri',
    university='Universitas Sebelas Maret',
    hobby='Memasak'
)

print(my_profile)