def create_character(name, role, level):
    return {
        "name": name,
        "role": role,
        "level": level
    }

def add_to_party(party, character):
    party.append(character)

def add_to_inventory(character, item):
    if "inventory" not in character:
        character["inventory"] = []
    character["inventory"].append(item)
    return character

def display_party(party):
    for character in party:
        print(f"Name: {character['name']}, Role: {character['role']}, Level: {character['level']}")

# Example usage
party = []
hero = create_character("Aria", "Warrior", 5)
mage = create_character("Luna", "Mage", 4)
add_to_party(party, hero)
add_to_party(party, mage)
add_to_inventory(hero, "Sword")
add_to_inventory(mage, "Staff")
add_to_inventory(mage, "Spellbook")
display_party(party)
