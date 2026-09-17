
length = 20
width = 12
thickness = 0.1
concrete_price_per_m3 = 250
wall_height = 2.7
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

print("==== BUILD HOUSE ====")

print("HOUSE")
print(f"Dimensions: {length}m x {width}m\n")

print("FOUNDATION")
print(f"Concrete required: {calculate_volume(calculate_area(length, width), thickness)} m\u00B3")
print(f"Estimated concrete cost: ${calculate_cost(calculate_volume(calculate_area(length, width), thickness), concrete_price_per_m3)}\n")

print("WALLS")
print(f"Wall height: {wall_height}m")
print(f"Wall perimeter: {calculate_perimeter(length, width)}m")
print(f"Gross wall area: {calculate_gross_wall_area(calculate_perimeter(length, width), wall_height)}m\u00B2 \n")

print("WINDOWS")
print(f"Number of windows: {number_of_windows}")
print(f"Total area: {round(calculate_area(window_length, window_width) * number_of_windows, 1)}m\u00B2 \n")

print("DOORS")
print(f"Number of doors: {number_of_doors}")
print(f"Total area: {round(calculate_area(door_length, door_width) * number_of_doors, 2)}m\u00B2 \n")

print(f"Net wall area: {calculate_net_wall_area(calculate_gross_wall_area(calculate_perimeter(length, width), wall_height), round(calculate_area(window_length, window_width) * number_of_windows, 1), round(calculate_area(door_length, door_width) * number_of_doors, 2))}m\u00B2")