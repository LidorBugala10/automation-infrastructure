def run():
    print("\n--- Survival Game ---")
    print("You wake up alone in a dark forest...\n")
    print("what you gonna do ?!")
    print("1 - Enter the cave")
    print("2 - Keep walking in the forest")
    print("3 - Hide behind a tree")
    choice1 = input("Choose 1, 2 or 3: ")
    if choice1 == "1":
        print("\nYou entered the cave.")
        print("Inside the cave there is a sleeping bear!")
        print("1 - Try to escape quietly")
        print("2 - Shout and run")
        print("3 - Jump into a river")
        choice2 = input("Choose 1, 2 or 3: ")
        if choice2 == "1":
            print("\nYou managed to escape quietly! You win!")
        elif choice2 == "2":
            print("\nThe bear woke up... You lose!")
        elif choice2 == "3":
            print("\nYou jumped into the river and escaped safely! You win!")
        else:
            print("\nInvalid choice. Game over.")
    elif choice1 == "2":
        print("\nYou keep walking in the forest.")
        print("You fall into a deep pit. You lose! ")
    elif choice1 == "3":
        print("\nYou hid behind a tree and the bear didn't see you. You survive! ")
    else:
        print("\nInvalid choice. Game over.")
