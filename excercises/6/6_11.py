cities = {
    "buenos aires": {
        "country": "argentina",
        "population": "3 million",
        "pseud": "paris of america",
    },
    "rome": {
        "country": "italy",
        "population": "4 million",
        "pseud": "eternal city",
    },
    "new york": {
        "country": "usa",
        "population": "4 million",
        "pseud": "world's capital",
    }
}

for name, information in cities.items():
    print ("\nThe name of the city is " + name.title())
    print("It's in " + information["country"])
    print("Tt's has " + information["population"] + " habitants")
    print("It's pseudonim is " + information["pseud"].title())