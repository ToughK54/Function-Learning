def greet_users(names):
    """Print a greeting to each user in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")

user_names = ['alice', 'bob', 'charlie']
greet_users(user_names)