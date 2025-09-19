# Lets write a function called favorite_pizza that prints three different sentences about pizzas that you like.
def favorite_pizza():
    pizza = input("What is your favorite pizza? ")
    second_favorite = input("What is your second favorite pizza? ")
    comfort_food = input("What pizza do you consider the best comfort food? ")
    print(f"I like {pizza} pizza.")
    print(f"I also like {second_favorite} pizza.")
    print(f"{comfort_food} is the best comfort food!")
# Call the function to see the messages about favorite pizza
favorite_pizza()
