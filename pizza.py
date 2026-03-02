print("hello world")

ordering = True

while ordering:
    topping = input("topping: ")

    if topping == "q":
        break

    print(f"ill add {topping} to your pizza")