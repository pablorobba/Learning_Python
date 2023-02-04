favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
friends = ["phil","sarah"]
for name in favorite_languages:
    print(name)
    
    if name in friends:
        print ("hi ".title() + name.title() +
               ". Your favorite langue is " + 
               favorite_languages[name].title())
        
if "erin" not in favorite_languages:
    print("ERIN TAKE THE DAMN POLL!")