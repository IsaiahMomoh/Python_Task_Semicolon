
def sum_of_squares(numbers):
    total = 0

    for number in numbers:
        total += number ** 2
    return total

import random
def random_numbers():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 50))
    return numbers

def list_length(numbers):
    count = 0
    for number in numbers:
        count += 1
    return count

def sum_even_positions(numbers):
    total = 0
    for index in range(1, len(numbers), 2):
        total += numbers[index]
    return total

def sum_odd_positions(numbers):
    total = 0
    for index in range(0, len(numbers), 2):
        total += numbers[index]
    return total

def multiply_every_third(numbers):
    result = 1
    for index in range(2, len(numbers), 3):
        result *= numbers[index]
    return result

def calculate_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    if count == 0:
        return 0
    return total / count

def largest_element(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def smallest_element(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def count_matching_strings(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

def create_list():
    numbers = []
    for number in range(1, 16):
        numbers.append(number)
    return numbers

def sum_every_third(numbers):
    total = 0
    for index in range(2, len(numbers), 3):
        total += numbers[index]
    return total

def first_middle_last_sum(numbers):
    size = len(numbers)
    if size == 0:
        return 0
    first = numbers[0]
    last = numbers[-1]
    if size % 2 == 1:
        middle = numbers[size // 2]
    else:
        middle = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    return first + middle + last


print(sum_of_squares(numbers))
print(random_numbers())
print(list_length(numbers))
print(sum_even_positions(numbers))
print(sum_odd_positions(numbers))
print(multiply_every_third(numbers))
print(calculate_average(numbers))
print(largest_element(numbers))
print(smallest_element(numbers))
print(count_matching_strings(words))
print(create_list())
print(sum_every_third(numbers))
print(first_middle_last_sum(numbers))















