available_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding " + requested_topping + ".")
    else:
        print("we dont have" + requested_topping + ".")

print("\n Finished making your pizza")