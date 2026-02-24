numbers = [3,7,10,15]
user_input = int(input("Enter a number: "))
if user_input in numbers:
    print("The number is on the list.")
else:
    print("The number is not listed.")

scores = float(input("Enter a score between 0-100: "))
if scores >= 90 :
    print("grade : A")
elif scores >= 80 :
    print("grade : B")
elif scores >= 70 :
    print("grade : C")
elif scores >= 60 :
    print("grade : D")
else :
    print("grade : F")

