def add_item(order, item):
    """Add an item to the order."""
    order.append(item)
    print(f"Added {item} to the order.")

def summarize_order(order):
    """Summarize the current order."""
    if not order:
        print("The order is empty.")
    else:
        print("Current order summary:")
        for item in order:
            print(f"- {item}")

# Example usage:
order = []
add_item(order, 'Pizza')
add_item(order, 'Burger')
summarize_order(order)