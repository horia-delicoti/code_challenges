# Astronaut 

# Full line of planets: 0 - 1000
# ----(xx5xx)(xx7xx)(x9x)(xx11xx)-----
# Input: [(5,2), (7, 2), (9,1), (11,2)]
#          | |-> gravity strenght
#          |-> position of the planet on the 0-1000 axis 
# Output: (1,3)(13,1000)
def common_data(list1, list2):
    result = False
    # traverse in the first list
    for x in list1:
        # traverse in the second list
        for y in list2:
            if x == y:
                result = True
                return result
    
    return result

def calculate_gravity(list_of_planets):
    list_of_planets_ranges = []
    for planet in list_of_planets:
        position = planet[0]
        strenght_planet = planet[1]
        list_of_planets_ranges.append([*range(position-strenght_planet, position+strenght_planet+1)])
    return list_of_planets_ranges

def concatenate_range_result(list_of_planets):
    list_of_planets_merged = []

input = [[5,2], [7, 2], [9,1], [11,2], [17,1], [234,4]]
list_of_planets_ranges_unmerged = calculate_gravity(input)
print("full list: ", list_of_planets_ranges_unmerged)

#print({*range(2, 5), *range(3, 7)})

for i in range(len(list_of_planets_ranges_unmerged)):
    if common_data(list_of_planets_ranges_unmerged[i], list_of_planets_ranges_unmerged[i+1]):
        print({*list_of_planets_ranges_unmerged[i], *list_of_planets_ranges_unmerged[i+1]})