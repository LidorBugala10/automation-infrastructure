import math_quiz
import Time_Trave_Adventure
import survival_game
import true_or_false
while True :
     print("\n ---Manu Page---")
     print("choose one of the options:")
     print("1. Time Trave Adventure")
     print("2. Survival Game")
     print("3. math quiz")
     print("4. true or false")
     print("5. Exit")
     choice = input("Enter your choice: ")
     if choice == "1" :
      Time_Trave_Adventure.run()
     elif choice == "2" :
         survival_game.run()
     elif choice == "3" :
         math_quiz.run()
     elif choice == "4" :
         true_or_false.run()
     elif choice == "5" :
         print("Thank you for playing!")
         break
     else :
      print("Invalid choice! please try again.")




