aliens = []

for alien_number in range(15):
    new_alien = {"color":"green", "points": 5, 
                 "speed":"slow"}
    aliens.append(new_alien)
    
for alien_number_2 in range(15):
    new_alien_2 = {"color":"yellow", "points": 5, 
                 "speed":"slow"}
    aliens.append(new_alien_2)
    
for alien in aliens [:5]:
    print(alien)
    
print("number: " + str(len(aliens)))

for alien in aliens [0:3]:
    if alien ["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
        
for alien in aliens [15:18]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
for alien in aliens [:5]:
    print(alien)
    
print("number: " + str(len(aliens)))

for alien in aliens [15:20]:
    print(alien)