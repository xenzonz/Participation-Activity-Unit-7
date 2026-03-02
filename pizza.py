#print("hello world")

#flag
ordering = True

while ordering:
    topping = input("Enter a pizza topping (type 'quit' to end): ").strip()

    #blank input guard clause
    if topping == "":
        print("Please enter a valid topping.")
        continue #reset loop

    if topping.lower() == "quit":
        ordering = False #set flag false to end loop
        print("Program ended.")
    else:
        print(f"I'll add {topping} to your pizza.")

    