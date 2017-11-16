import random

def mergesort(values):
    if len(values) > 2:
        first_half = values[:len(values)//2]
        second_half = values[len(values)//2:]

        first_half = mergesort(first_half)
        second_half = mergesort(second_half)

        first_half.reverse()
        second_half.reverse()

        dump_first = False
        dump_second = False

        result = []

        while not dump_first and not dump_second:
            if len(first_half) == 0:
                dump_second = True
                pass
            elif len(second_half) == 0:
                dump_first = True
                pass
            else:
                if first_half[-1] < second_half[-1]:
                    result.append(first_half.pop())
                else:
                    result.append(second_half.pop())

        if dump_first:
            while len(first_half) != 0:
                result.append(first_half.pop())
        elif dump_second:
            while len(second_half) != 0:
                result.append(second_half.pop())

        return result

    else:
        if len(values) == 0:
            return []
        elif len(values) == 1:
            return values
        elif len(values) == 2:
            if values[0] > values[1]:
                return [values[1], values[0]]
            else:
                return values

# Generate random list
values = random.sample(range(100000), 10)

print(len(values))
print(values)

values = mergesort(values)

print(len(values))
print(values)
