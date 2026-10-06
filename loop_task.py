


for number in range(1,100,1):
    if number % 2 == 0:
     print(number)
        



for number in range(50,100,1):
    if number % 2 == 1:
     print(number)
            
 


for number in range(100,1,-1):
    print(number)




for number in range(1,20,1):
    print(number*number)




for number in range(1,50,1):
    print(number*3)




for number in range(1,100,1):
    if number%3 == 0 and number% 5 ==0:
     print(number)




for number in range(1,100,1):
        if number % 7 == 0:
            print(number)




total = 0
for number in range(1,50,1):
    total = total + number
    print(total)





product = 1
for number in range(1,10,1):
    product = product * number
    print(product)




for letter in range(ord('A'),ord('Z'),+1):
    print(chr(letter))




    number = int(input('Enter number'))



for count in range(1,11):
    print(number,"X",count,"=", number*count)




word = input("Enter word:")
for character in word:
    print(character)




word = input("Enter word: ")
result = ""
for letter in word:
    result = result+ letter.upper()
    print(result)





word = input("Enter a word:")
result = "" 
for letter in word:
    result = result + letter.lower()
    print(result)





word = input ("Enter a word:")
result = 0
for letter in word:
    if letter.lower()in "aeiou":
        result = result + 1
        print("number of vowels:",result)




number = int(input("Enter a number:"))
count = 0 
for digit in str(number):
    count = count + 1 
    print("number of digit:",count)




number = int(input("Enter number:"))
count = 0 
for largest in str(number):
    count = count + 1
    print("number of largest:",count)





numbers = [23,45,65,12,21,24,41,52]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
        print("The largest of the number is:", largest)



numbers = [23,45,65,12,21,24,41,52]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
     smallest = number
     print("The smallest of the number is:", smallest)