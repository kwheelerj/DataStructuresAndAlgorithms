# python3


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


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(my_max_pairwise_product(input_numbers))
