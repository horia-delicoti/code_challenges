# Astronaut 

# Full line of planets: 0 - 1000
# Input: [(5,2), (7, 3), (9,1), (11,2)]
#          | |-> gravity strenght
#          |-> position of the planet on the 0-1000 axis 
# Output: 

def calculate_gravity(list_of_planets):
    list_of_planets_ranges = []
    for planet in list_of_planets:
        position = planet[0]
        strenght_planet = planet[1]
        list_of_planets_ranges.append([*range(position-strenght_planet, position+strenght_planet+1)])
    return list_of_planets_ranges

def concatenate_range_result(list_of_planets):
    list_of_planets_merged = []

input = [[5,2], [7, 3], [9,1], [11,2], [17,1], [234,4]]
list_of_planets_ranges_unmerged = calculate_gravity(input)


for i in list_of_planets_ranges_unmerged:
    print(i)