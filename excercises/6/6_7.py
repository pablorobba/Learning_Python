person_0 = {
    "name":"Pablo",
    "lastname": "Robba",
    "age": "24",
    "city":"BsAs",
}
person_1 = {
    "name":"Steve",
    "lastname": "Vai",
    "age": "58",
    "city":"NY",
}
person_2 = {
    "name":"John",
    "lastname": "Petrucci",
    "age": "56",
    "city":"NY",
}

people = [person_0,person_1,person_2]

for person in people:
    print("\n" + person["name"])
    print("\n" + person["lastname"])
    print("\n" + person["age"])
    print("\n" + person["city"])