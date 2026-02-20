from city_functions import get_city_country

print("Enter 'q' anytime to stop.")
while True:
    city = input("Enter a city name: ")
    if city == 'q':
        break
    country = input("Enter the country the city is in: ")
    if country == 'q':
        break
    formatted_name = get_city_country(city, country)
    print(f"{formatted_name}")