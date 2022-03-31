import re
import matplotlib.pyplot as plt
import argparse


cities_set = []
cities_tups = []
cities_dict = {}

def read_tsp_data(tsp_name): 
    with open(tsp_name) as f:
        content = f.read().splitlines()
        cleaned = [x.lstrip() for x in content if x != ""]
        return cleaned
    
    

ls = read_tsp_data(r"C:\...\a280.tsp")


def detect_dimension(in_list):
    for item in ls:
        if item.startswith('DIMENSION'):
            dim = item.split(' ')[2]
            break
    return dim

def get_cities(ls, dimension):
    dimension = int(dimension)
    for item in ls:
        for num in range(1, dimension + 1):
            if item.startswith(str(num)):
                index, space, rest = item.partition(' ')
                if rest not in cities_set:
                    cities_set.append(rest)
        return cities_set
    
    
def city_tup(list):
    for item in list:
        first_coord, space, second_coord = item.partition(' ') # Get the first and the second coordinate
        cities_tups.append((first_coord.strip(), second_coord.strip())) # Insert them as tuple after calling strip to ignore the spaces at the start and at the end of each string
    return cities_tups


def create_cities_dict(cities_tups):

    for num in range(1, len(cities_tups) + 1):
        cities_dict[num] = cities_tups[num - 1]

    return cities_dict

def produce_final(file = r"C:\...\a280.tsp"):
    data = read_tsp_data(file)
    print(data)
    dimension = detect_dimension(data)
    print(dimension)
    cities_set = get_cities(data, dimension)
    print(cities_set)
    cities_tups = city_tup(cities_set)
    print(cities_tups)
    cities_dict = create_cities_dict(cities_tups)
    print(cities_dict)
    return cities_dict
    
    
    
    
    
data = read_tsp_data(r"C:\...\a280.tsp")
print(data)
dimension = detect_dimension(data)
print(dimension)
cities_set = get_cities(data, dimension)
print(cities_set)
