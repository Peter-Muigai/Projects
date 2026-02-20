def get_formatted_name(first_name, last_name, middle_name=''):
    """Display a neatly formatted name."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('justin', 'timberlake')
print(musician)
musician = get_formatted_name('mark', 'walter', 'white')
print(musician)