print("hello world")

ordering = True

while ordering:
    topping = input("Enter a pizza topping (type 'quit' to end): ")

    if topping == "":
        print("Please enter a valid topping.")

    if topping == "quit":
        ordering = False
    else:
        print(f"I'll add {topping} to your pizza.")

    