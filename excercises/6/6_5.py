rivers = {
    "river plate": "argentina",
    "nile": "egypt",
    "amazonian":"brazil",
}

for river, country in rivers.items():
    print("\nThe " + river.title() + 
          " runs though " + country.title())
    
for river in rivers:
    print("\n" + river.title())
    
for country in rivers.values():
    print("\n" + country.title())