# python3
from random import randint


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def my_max_pairwise_product(numbers):
    n = len(numbers)
    first_max = 0
    second_max = 0

    for i in range(n):
        if numbers[i] > second_max:
            second_max = numbers[i]
            if numbers[i] > first_max:
                second_max = first_max
                first_max = numbers[i]

    return first_max * second_max


def stress_test(max_rand_size, max_rand_value):
    while True:
        size = randint(1,max_rand_size)
        numbers = [None] * size
        for i in range(size):
            numbers[i] = randint(1, max_rand_value)
        print(numbers)

        result_1 = max_pairwise_product(numbers)
        result_2 = my_max_pairwise_product(numbers)

        if result_1 == result_2:
            print("OK")
        else:
            print("Wrong answer: ", result_1, result_2)
            return


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(my_max_pairwise_product(input_numbers))

    # Stress Test #
    # max_size = 500
    # max_value = 100000
    # stress_test(max_size, max_value)
