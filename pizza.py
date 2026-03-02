print("hello world")

ordering = True

while ordering:
    topping = input("Enter a pizza topping (type 'quit' to end): ")

    if topping == "quit":
        break

    if topping == "":
        print("Please enter a valid topping")

    print(f"ill add {topping} to your pizza")