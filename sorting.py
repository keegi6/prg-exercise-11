import random
import matplotlib.pyplot as plt


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


def bubble_sort(values):
    plt.ion()
    plt.show()
    print(values)
    numbers = values.copy()
    count = len(values)-1
    while count > 0:
        for i in range(count):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

                index_highlight1 = i
                index_highlight2 = i + 1
                colors = ["steelblue"] * len(values)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(values)), values, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)

        count -= 1
    print(numbers)
    plt.ioff()
    plt.show()


def main():
    seznam1 = random_numbers(10, low=0, high=100)
    selection_sort(seznam1)
    seznam2 = random_numbers(10, low=0, high=100)
    bubble_sort(seznam2)

main()