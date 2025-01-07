value1 = 15
value2 = 10

if value1 > value2:
    print("value1 is greater than value2")
elif value1 == value2:
    print("value1 is equal to value2")
else:
    print("value1 is less than value2")

if value1 >= 5 and value1 <=20:
    print("value1 is between 5 and 20")

sentence = input("Enter a sentence: ")
if len(sentence) >5:
    print("The sentence is more than 5 characters")
else:
    print("The sentence is less than 5 characters")

number = input("Enter a number: ")
if int(number) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")