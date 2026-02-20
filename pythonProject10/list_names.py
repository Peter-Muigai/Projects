def greet_users(names):
    """Print a greeting message to each  user."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
usernames = ['mark', 'ty', 'candice']
greet_users(usernames)