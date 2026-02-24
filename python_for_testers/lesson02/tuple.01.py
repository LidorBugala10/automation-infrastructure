num1 = input("enter first number")
num2 = input("enter second number")
num3 = input("enter third number")
numbers = (num1, num2,num3)
a,b,c = numbers
print("first number is",1)
print("second number is",2)
print("third number is",3)

person = {"name": "lidor", "age": 24,"city":"kiryat malachi"}
new_age = int(input("enter new age"))
person["age"] = new_age
print(person)

fruits = []
for i in range(5):
    fruit = input(f"enter fruit")
    fruits.append(fruit)
fruits_tuple = tuple(fruits)
print("fruits_tuple",fruits_tuple)
print("length",len(fruits_tuple))
