def string_length(word):
    return len(word)

def first_last_two(word):
    if len(word) < 2:
        return word[2] + word[-2]

def add_ing(word):
    if len(word) < 3:
        return word
    if word.endswith("ing"):
        return word + "ly"
    return word + "ing"

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)

def odd_index_characters(word):
    result = ""
    for index in range(len(word)):
        if index % 2 != 0:
            result += word[index]
    return result


def find_minimum(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def find_maximum(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def repeat_string(word, number):
    if isinstance(number, float):
        return word
    result = ""
    for i in range(number):
        result += word
    return result

def square_elements(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

print(string_length("semicolon"))
print(first_last_two("semicolon"))
print(add_ing("semicolon"))
print(longest_word("word"))
print(index in range(len(word))
print(find_minimum(numbers))
print(find_maximum(numbers))
print(repeat_string(word, number))
print(square_elements(numbers))







