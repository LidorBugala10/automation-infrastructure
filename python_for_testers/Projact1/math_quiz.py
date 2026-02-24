import random
def run():
    print("\n--- Math Quiz ---")
    level = input("Choose difficulty (easy, medium, hard): ").lower()
    if level not in ["easy", "medium", "hard"]:
        print("Error: Invalid difficulty level.")
        return
    operation = input("Choose operation (+, -, *): ")
    if operation not in ["+", "-", "*"]:
        print("Error: Invalid operation.")
        return
    if level == "easy":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    elif level == "medium":
        a = random.randint(10, 50)
        b = random.randint(10, 50)
    else:
        a = random.randint(50, 100)
        b = random.randint(50, 100)
    if operation == "+":
        answer = a + b
    elif operation == "-":
        answer = a - b
    else:
        answer = a * b
    try:
        guess = int(input(f"What is {a} {operation} {b}? "))
    except ValueError:
        print("Error: You must enter a number.")
        return
    if guess == answer:
        print("Correct! You win!")
    else:
        print(f"Wrong! The answer is: {answer}")
