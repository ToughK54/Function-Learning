def get_full_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# Full Name Formatter
# This program formats a full name using a function.
name = get_full_name("john", "wick")
print(name)
