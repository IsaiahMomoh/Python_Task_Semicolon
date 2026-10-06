
def isEven(number):
    return number % 2 == 0
    
def isPrimeNumber(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
            return True


def subtract(firstNumber, secondNumber):
    return (firstNumber - secondNumber)


def divide(firstNumber, secondNumber):
    if secondNumber == 0:
        return 0
        return firstNumber / secondNumber
    
def factorOf(number):
    if number <= 0:
        return 0

    count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1
    return count

def isSquare(number):
    if number < 0:
        return False

    i = 0

    while i * i <= number:
        if i * i == number:
            return True

        i += 1

    return False
    
def isPalindrome(number):
    numberString = str(number)
    return numberString == numberString[::-1]

def factorialOf(number):
    if number < 0:
        return 0
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
return factorial

def squareOf(number):
    return number * number
