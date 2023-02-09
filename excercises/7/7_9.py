sandwich_orders = ["sanguche de miga","pastrami",
                   "hamburguesa","pebete","pastrami",
                   "pastrami"]
finished_sandwiches = []

print("We are out of Pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    
while sandwich_orders:
    already_finished = sandwich_orders.pop()
    
    print("Finished your " + already_finished.title())
    finished_sandwiches.append(already_finished)
    
print("\nThe sandwiches we made are:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())