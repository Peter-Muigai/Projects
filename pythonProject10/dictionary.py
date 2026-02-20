def build_person(first_name, last_name, age=None):
    """Return a dictionary with a full name."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']=age
    return person

wrestler = build_person('seth', 'rollins', age=39)
print(wrestler)
