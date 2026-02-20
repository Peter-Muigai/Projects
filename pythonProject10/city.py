def name_city(city, country):
    """Return a neat display of city and country"""
    city_name = f"{city}, {country}"
    return city_name.title()
while True:
    print("\nEnter some cities and the country they are in:")
    print("(Enter 's' to stop)")
    c_name = input("Enter a city: ")
    if c_name == 's':
        break
    t_name = input("Enter its country: ")
    if t_name == 's':
        break
    full_display = name_city(c_name, t_name)
    print(f"{full_display}")