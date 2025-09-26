def create_character(name, role, level):
    character = {
        "name": name,
        "role": role,
        "level": level,
        "inventory": [],
        "stats": {
            "strength": 10,
            "agility": 10,
            "intelligence": 10
        }
    }
    return character

def display_character(character):
    print(f"\nName: {character['name']}")
    print(f"\nRole: {character['role']}")
    print(f"\nLevel: {character['level']}")
    print("Stats:")
    for stat, value in character["stats"].items():
        print(f" {stat}: {value}")
    print("Inventory:", ", ".join(character["inventory"]) if character["inventory"] else "Empty")

def add_to_inventory(character, item):
    character["inventory"].append(item)
    print(f"Added {item} to {character['name']}'s inventory.")
def level_up(character):
    character["level"] += 1
    character["stats"]["strength"] += 2
    character["stats"]["agility"] += 2
    character["stats"]["intelligence"] += 2
    print(f"{character['name']} leveled up to {character['level']}!")
    print(f"New stats: {character['stats']}")
# Example usage:
hero = create_character("Artemis", "Archer", 5)
display_character(hero)
add_to_inventory(hero, "Bow")
add_to_inventory(hero, "Arrow")
display_character(hero)
level_up(hero)
