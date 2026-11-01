def describe_city(city, country='indonesia'):
    """Mencetak informasi kota dan negara tempatnya berada."""
    print(f"{city.title()} terletak di negara {country.title()}.")

describe_city('surakarta')
describe_city('yogyakarta')
describe_city('tokyo', 'jepang')