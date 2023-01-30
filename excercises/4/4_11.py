favorite_pizzas = ["pizza 1", "pizza 2", "pizza 3"]
my_friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append("pizza 4")
my_friends_pizzas.append("pizza 5")

print("My friend's favorite pizzas are")
for pizza in my_friends_pizzas:
    print(pizza)