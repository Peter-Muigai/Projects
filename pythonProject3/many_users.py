users = {
    'muigaipeter': {
        'first': 'peter',
        'last': 'muigai',
        'location': 'nyeri',
        },

    'jaymuk': {
        'first': 'james',
        'last': 'mukima',
        'location': 'nairobi',
        },

    }
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"{full_name.title()}")
    print(f"{location.title()}")
