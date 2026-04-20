import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    print(values)
    for min_index in range(len(values)):
        # print(values)
        min_value = values[min_index]
        min_ind = min_index
        for i in range(min_index, len(values)):
            if values[i] < min_value:
                min_value = values[i]
                min_index = i
        values[min_ind], values[min_index] = values[min_index], values[min_ind]
    print(values)
print(selection_sort(random_numbers(10)))
