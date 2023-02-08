prompt ="\nEnter the pizza topping you want!"
prompt += "\nWrite 'quit' to stop "

message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print ("\nAdding " + message)

    
    