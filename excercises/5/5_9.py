usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello " + username.title())
        else:
            print("Greetings " + username.title())
            
else:
    print("\nWe need to find users")
