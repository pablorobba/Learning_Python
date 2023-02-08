prompt ="\nEnter the pizza topping you want!"
prompt += "\nWrite 'quit' to stop "

active = True

while active:
    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print("\nAdding " + message) 