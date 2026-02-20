def get_city_country(city, country, population=0):
    """Generate a city and the country it's from."""
    if population:
        full_name = f"{city}, {country}-population:{population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()