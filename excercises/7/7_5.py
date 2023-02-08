promt = "\nTell me your age"
promt += "\nWritte 'quit' to stop it "

active = True

while active:
    message = input(promt)
    
    if message == "quit":
        active = False
    else:
        message = int(message)
        if  message <3:
            print("it costs 3 $")
        elif message >3 and message <12:
            print ("it costs 10 $")
        else:
            print("its costs 15$")