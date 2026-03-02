print("hello world")

#flag
ordering = True

while ordering:
    topping = input("Enter a pizza topping (type 'quit' to end): ")

    #blank input guard clause
    if topping == "":
        print("Please enter a valid topping.")
        continue #reset loop

    if topping.lower().strip() == "quit":
        ordering = False #set flag false to end loop
    else:
        print(f"I'll add {topping} to your pizza.")

    