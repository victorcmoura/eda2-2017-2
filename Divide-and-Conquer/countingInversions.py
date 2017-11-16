import random

def count_inversions(values):
    if len(values) == 1:
        return 0

    # Divide and conquer
    first_half = values[:len(values)//2]
    second_half = values[len(values)//2:]

    # count recursively the inversions in each half
    first_result = count_inversions(first_half)
    second_result = count_inversions(second_half)

    # sort both halves
    first_half = sorted(first_half)
    second_half = sorted(second_half)

    # Sets different halves inversion counter
    different_halves_inversions = 0

    # Count inversions of different halves
    for second_half_value in second_half:
        for first_half_value in first_half:
            if second_half_value < first_half_value:
                different_halves_inversions += 1

    return first_result + second_result + different_halves_inversions

# Sets random values
values = random.sample(range(100), 10)

# print results
print('Original values')
print('Values:', values)
print('Inversions:', count_inversions(values))
