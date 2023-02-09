responses = {}
bandera = True

while bandera:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world" +
                    ", where would you go? ")
    responses [name] = response

    repeat = input("Would you like to let another person respond (yes/no) ")
    if repeat == "no":
        bandera = False
    
print ("\nRESULTS:")
for name, response in responses.items():
    print(name + " would like to go to " + response + ".") 