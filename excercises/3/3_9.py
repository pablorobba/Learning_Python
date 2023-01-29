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

len_guests = len(guests)
print(len_guests)

