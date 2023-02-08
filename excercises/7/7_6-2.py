prompt ="\nEnter the pizza topping you want!"
prompt += "\nWrite 'quit' to stop "

while True:
    message = input(prompt)
    
    if message == "quit":
        break
    else:
        print("\nAdding " + message) 