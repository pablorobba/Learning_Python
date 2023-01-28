guests = ["Plato","Aquiles","Napoleon"]

print(guests[0] + " can you come to a dinner")
print(guests[1] + " can you come to a dinner")
print(guests[2] + " can you come to a dinner")


print(guests[0] + " doesnt come")

del guests [0] 
guests.insert(0,"Maradona")

print(guests[0] + " can you come to a dinner")
print(guests[1] + " can you come to a dinner")
print(guests[2] + " can you come to a dinner")


print("we found a bigger table, so more guests")

guests.insert(0, "Alexander")
guests.insert(3, "Julius Cesar")
guests.append("Djokovic")

print(guests[0] + " can you come to a dinner")
print(guests[1] + " can you come to a dinner")
print(guests[2] + " can you come to a dinner")
print(guests[3] + " can you come to a dinner")
print(guests[4] + " can you come to a dinner")
print(guests[5] + " can you come to a dinner")


print("sorry, we'll invite only two guests")

alexander_sorry = guests.pop(0)
maradona_sorry = guests.pop(0)
aquiles_sorry = guests.pop(0)
julius_cesar_sorry = guests.pop(0)

print ("sorry, we cant invite you, mr " + alexander_sorry)
print ("sorry, we cant invite you, mr " + maradona_sorry)
print ("sorry, we cant invite you, mr " + aquiles_sorry)
print ("sorry, we cant invite you, mr " + julius_cesar_sorry )

print(guests[0] + " you re still invited")
print(guests[1] + " you re still invited")

guests.clear()
print(guests)