# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def print_details(self):
# #          print("Name:", self.name)
# #          print("Age:", self.age)
# #     def is_adult(self):
# #          if self.age >= 18 :
# #              print("Adult")
# #          else:
# #              print("Minor")
# # person1 = Person("Lidor", 24)
# # person2 = Person("Messi", 38)
# # person1.print_details()
# # person1.is_adult()
# # print("=======================")
# # person2.print_details()
# # person2.is_adult()
#
# # class Book:
# #     def __init__(self, title, author, pages):
# #         self.title = title
# #         self.author = author
# #         self.pages = pages
# #     def print_details(self):
# #         print(f"Book title: {self.title},  by author: {self.author} , pages: {self.pages}.")
# #     def is_long_book(self):
# #         if self.pages > 300 :
# #             print("Long Book")
# #         else :
# #             print("Short Book")
# # book1=Book("Leo Messi", "lidor b ", 50)
# # book1.print_details()
# # book1.is_long_book()


# import random
# def survival_game():
#     print("\n--- Survival Game ---")
#     print("You wake up alone in a dark forest...\n")
#     print("1 - Enter the cave")
#     print("2 - Keep walking in the forest")
#     print("3 - Hide behind a tree")
#     choice1 = input("Choose 1, 2 or 3: ")
#     if choice1 == "1":
#         print("\nYou entered the cave.")
#         print("Inside the cave there is a sleeping bear!")
#         print("1 - Try to escape quietly")
#         print("2 - Shout and run")
#         print("3 - Jump into a river")
#         choice2 = input("Choose 1, 2 or 3: ")
#         if choice2 == "1":
#             print("\nYou managed to escape quietly! You win ")
#         elif choice2 == "2":
#             print("\nThe bear woke up... You lose ")
#         elif choice2 == "3":
#             print("\nYou jumped into the river and escaped safely! You win ")
#         else:
#             print("\nInvalid choice. Game over.")
#     elif choice1 == "2":
#         print("\nYou keep walking in the forest.")
#         print("You fall into a deep pit. You lose ")
#     elif choice1 == "3":
#         print("\nYou hid behind a tree and the bear didn't see you. You survive! ")
#     else:
#         print("\nInvalid choice. Game over.")
# def guess_number():
#     print("\n--- Guess the Number ---")
#     level = input("Choose difficulty (easy, medium, hard): ").lower()
#     if level == "easy":
#         number = random.randint(1, 10)
#         attempts = 5
#     elif level == "medium":
#         number = random.randint(1, 50)
#         attempts = 7
#     else:
#         number = random.randint(1, 100)
#         attempts = 10
#     print(f"You have : {attempts} attempts to guess the number.")
#     for i in range(attempts):
#         guess = int(input("Your guess: "))
#         if guess == number:
#             print("Correct! You win! ")
#             return
#         elif guess < number:
#             print("The number is too low!")
#         else:
#             print("The number is too high!")
#     print(f"Sorry, you ran out of attempts. The number was : {number} ")
#
# def math_quiz():
#     print("\n--- Math Quiz ---")
#     level = input("Choose difficulty (easy, medium, hard): ").lower()
#     operation = input("Choose operation (+, -, *): ")
#     if level == "easy":
#         a = random.randint(1, 10)
#         b = random.randint(1, 10)
#     elif level == "medium":
#         a = random.randint(10, 50)
#         b = random.randint(10, 50)
#     else:
#         a = random.randint(50, 100)
#         b = random.randint(50, 100)
#     if operation == "+":
#         answer = a + b
#     elif operation == "-":
#         answer = a - b
#     else:
#         answer = a * b
#     guess = int(input(f"What is {a} {operation} {b}? "))
#     if guess == answer:
#         print("Correct!" )
#     else :
#         print(f"Wrong! The answer is : {answer} ")
# while True:
#     print("\n=== Main Menu ===")
#     print("1 - Survival Game")
#     print("2 - Guess the Number")
#     print("3 - Math Quiz")
#     print("4 - Exit")
#     choice = input("Choose a game (1-4): ")
#     if choice == "1":
#         survival_game()
#     elif choice == "2":
#         guess_number()
#     elif choice == "3":
#         math_quiz()
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Try again.")













