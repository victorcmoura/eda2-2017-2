import random

# Default binary search that returs always an index, even if the searched value was not found
def binary_search(values, searched_value):
    first = 0
    last = len(values) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2

        if values[midpoint] == searched_value:
            found = True
        else:
            if searched_value < values[midpoint]:
                last = midpoint - 1
            elif searched_value > values[midpoint]:
                first = midpoint + 1

    return midpoint

# Validates result for truck driver algorithm application, since the original binary search was customized
def binary_search_for_truck_driver(values, searched_value):
    result = binary_search(values, searched_value)

    # if it is not the first break point
    if result != 0:
        # if the result is bigger than the searched value, it becomes the previous break point
        if values[result] > searched_value:
            result = result - 1

    return result

# Returns the solution list. If there is no complete solution, there will be only the break points that the truck managed to reach
def truck_driver_algorithm(break_points, fuel_capacity):
    solution = []
    current_location = 0

    while current_location != break_points[-1]:
        index = binary_search_for_truck_driver(break_points, current_location + fuel_capacity)

        if current_location == break_points[index]:
            return {'solution':solution}

        current_location = break_points[index]
        solution.append(break_points[index])
    return {'solution':solution}


# Generate break points
break_points = random.sample(range(50), 20)
break_points = sorted(break_points)

print(break_points)

fuel_capacity = 2

solution = truck_driver_algorithm(break_points, fuel_capacity)

print(solution)
