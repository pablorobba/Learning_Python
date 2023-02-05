fav_numb = {
    "pablo" : [9,8,8],
    "pedrito" : [9,8,9],
    "diego" : [9,8,9],
    "marselo" : [9,8,6],
    "fer" : [9,8,5],
    }

for name, numbers in fav_numb.items():
    print("\n" + name.title() + "'s favorite languages are")
    for number in numbers:
        print("\t" + str(number).title())