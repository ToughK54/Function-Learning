def get_full_name(first_name, last_name):
    """Generate a neatly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
def build_user_profile(first_name, last_name, age, **user_info): # Build a dictionary containing everything we know about a user.
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first_name.title() # Add the first and last name to the profile dictionary.
    profile['last_name'] = last_name.title() # Add the first and last name to the profile dictionary.
    profile['age'] = age # Add the age to the profile dictionary.
    for key, value in user_info.items():
        profile[key] = value # Add any additional key-value pairs to the profile dictionary.
    return profile # Return the completed dictionary.
# This function accepts a first and last name, and an arbitrary number of keyword arguments.
# It builds a dictionary containing the user's profile information.
# The function returns the completed dictionary.
# Example usage:
user_profile = build_user_profile('john', 'wick', 35)
print(user_profile)