num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum_nums = num1 + num2
difference = num1 - num2
product = num1 * num2
remainder = num1 % num2
print("The sum is :",sum_nums)
print("The difference is :",difference)
print("The product is :",product)
print("The remainder is :",remainder)

x = 10
print("start value" , x )
x += 5
print("after x += 5:",x )
x -= 3
print("after x -= 3:",x )
x *= 2
print("after x *= 2:",x )
x /= 4
print("after x /= 4:",x )
x %= 5
print("after x %= 2:",x )

age = int(input("how old are you? : "))
if age >= 18:
    print("You are old enough")
else : print("You are not old enough")

fruits = ["apple", "banana", "orange"]
user_fruits = input("Enter fruits:")
if user_fruits in fruits:
    print("The fruit is on the list")
else:
    print("The fruit is not on the list")

num1 = int(input("Insert number one: "))
num2 = int(input("Insert number two: "))
if num1 > 0 and num2 > 0 :
    print("The number is positive")
    if num1 > 0 or num2 > 0 :
        print("At least one of the numbers is positive")
        if not (num1 > 0 and num2 > 0):
            print("None of the numbers are positive")





