print("==== BUILD HOUSE ====")
length = 20
width = 12
thickness = 0.1
concrete_price_per_m3 = 250

def calculate_area(length, width):

    area = length * width
    return area

def calculate_volume(area, thickness):

    volume = area * thickness
    return volume

def calculate_cost(volume, price_per_m3):

    total_concrete_price = volume * price_per_m3
    return total_concrete_price


print(f"Dimensions: {length}m x {width}m x {thickness}m")
print(f"Concrete required: {calculate_volume(calculate_area(length, width), thickness)} m\u00B3")
print(f"Estimated concrete cost: ${calculate_cost(calculate_volume(calculate_area(length, width), thickness), concrete_price_per_m3)}")