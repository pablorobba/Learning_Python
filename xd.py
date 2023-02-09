responses ={}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which montain would you like to climb someday ")
    
    responses [name] = response

    repeat = input ("Would you like to continue answering? (yes/no) ")

    if repeat == "no":
     polling_active = False
    
print("\n POLL RESULTS:")
for name, response in responses.items():
    print (name + " would like to climb " + response + ".")