def make_sandwich(bread, filling):
    """Make a sandwich with the given bread and filling."""
    sandwich = f"You ordered a {filling} on {bread} bread."
    return sandwich.title()
# Make a Sandwich
# This program makes a sandwich using a function.
sandwich = make_sandwich("wheat", "turkey")
print(sandwich)
