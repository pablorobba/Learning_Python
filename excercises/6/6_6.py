favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
people_that_should_the_poll = ["erin","jen"]

for people in people_that_should_the_poll:
    if people in favorite_languages.keys():
        print(people.title() + ", thanks to take the pool")
    else:
        print(people.upper() + ", TAKE THE DAMN POOL" )