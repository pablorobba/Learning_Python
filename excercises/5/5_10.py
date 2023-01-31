current_usernames = ["myoshin","pcrcovers","ultragrison","admin"]
new_usernames = ["myoshin","PCRCOVERS","pepito","pavel","peron"]

for new_username in new_usernames:
    if new_username.lower() in current_usernames:
        print("the name is already used")
    else:
        print("the name is available")