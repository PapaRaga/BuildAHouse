import math

length = 20
width = 12
thickness = 0.1
concrete_price_per_m3 = 250
wall_height = 2.7
wall_length = 20
stud_spacing = 0.6
window_length = 1.5
window_width = 1.2
door_length = 2.1
door_width = 0.9
number_of_windows = 3
number_of_doors = 2

def calculate_area(length, width):

    area = length * width
    return area

def calculate_perimeter(length, width):

    perimeter = 2 * (length + width)

    return perimeter

def calculate_net_wall_area(gross_wall_area, window_area, door_area):

    net_wall_area = gross_wall_area - window_area - door_area

    return net_wall_area

def calculate_gross_wall_area(perimeter, wall_height):

    gross_wall_area = wall_height * perimeter

    return gross_wall_area

def calculate_volume(area, thickness):

    volume = area * thickness
    return volume

def calculate_cost(volume, price_per_m3):

    total_concrete_price = volume * price_per_m3
    return total_concrete_price

def calculate_stud_count(wall_length, stud_spacing):

    number_of_studs = wall_length / stud_spacing
    return math.ceil(number_of_studs)

print("==== BUILD HOUSE ====")

print("HOUSE")
print(f"Dimensions: {length}m x {width}m\n")

area_of_house = calculate_area(length, width)
concrete_needed = calculate_volume(area_of_house, thickness)
concrete_cost = calculate_cost(concrete_needed, concrete_price_per_m3)
print("FOUNDATION")
print(f"Concrete required: {concrete_needed} m\u00B3")
print(f"Estimated concrete cost: ${concrete_cost}\n")

perimeter = calculate_perimeter(length, width)
gross_wall_area = calculate_gross_wall_area(perimeter, wall_height)
print("WALLS")
print(f"Wall height: {wall_height}m")
print(f"Wall perimeter: {perimeter}m")
print(f"Gross wall area: {gross_wall_area}m\u00B2 \n")

total_area_windows = round(calculate_area(window_length, window_width) * number_of_windows, 1)
print("WINDOWS")
print(f"Number of windows: {number_of_windows}")
print(f"Total area: {total_area_windows}m\u00B2 \n")

total_area_doors = round(calculate_area(door_length, door_width) * number_of_doors, 2)
print("DOORS")
print(f"Number of doors: {number_of_doors}")
print(f"Total area: {total_area_doors}m\u00B2 \n")

net_wall_area = calculate_net_wall_area(gross_wall_area, total_area_windows, total_area_doors)
print(f"Net wall area: {net_wall_area}m\u00B2\n")

studs_needed = calculate_stud_count(wall_length, stud_spacing)
print("FRAMING")
print(f"Stud spacing: {stud_spacing}m")
print(f"Approximate studs needed: {studs_needed}")