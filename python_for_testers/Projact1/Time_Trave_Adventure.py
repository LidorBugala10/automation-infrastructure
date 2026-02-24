def get_choice(options):
    while True:
        choice = input("Choose: ").lower()
        if choice in options:
            return choice
        print("Invalid choice, try again.")
def time_travel_adventure():
    print("\n--- Time Travel Adventure ---")
    print("You are standing in front of a mysterious time machine.")
    print("Where do you want to travel?\n")
    print("a - Far future")
    print("b - Middle Ages")
    print("c - Ancient Egypt")
    choice1 = get_choice(["a", "b", "c"])
    if choice1 == "a":
        print("\nYou arrive in the future! Robots run the world.")
        print("What will you do?")
        print("a - Talk to the robots")
        print("b - Explore an abandoned city")
        print("c - Return to the time machine immediately")
        choice2 = get_choice(["a", "b", "c"])
        if choice2 == "a":
            print("\nThe robots teach you advanced technologies. Adventure successful! ")
        elif choice2 == "b":
            print("\nYou discover mysterious ancient buildings. Fascinating adventure! ")
        else:
            print("\nYou safely return to the time machine. Mysterious mission ended.")
    elif choice1 == "b":
        print("\nYou arrive in the Middle Ages! Castles, knights, and busy markets.")
        print("What will you do?")
        print("a - Join a knight tournament")
        print("b - Visit the market and try some food")
        print("c - Escape the city to the time machine")
        choice2 = get_choice(["a", "b", "c"])
        if choice2 == "a":
            print("\nYou win the tournament! You are a hero of your time.")
        elif choice2 == "b":
            print("\nYou taste local food. An unforgettable experience!")
        else:
            print("\nYou escape the mysteries and return to the time machine.")
    else:
        print("\nYou arrive in Ancient Egypt! Pyramids and endless sand.")
        print("What will you do?")
        print("a - Visit a pyramid")
        print("b - Talk to a local resident")
        print("c - Return to the time machine")
        choice2 = get_choice(["a", "b", "c"])
        if choice2 == "a":
            print("\nYou discover mysterious artifacts inside the pyramid! Magical experience ")
        elif choice2 == "b":
            print("\nThe local resident tells you ancient secrets. Fascinating adventure!")
        else:
            print("\nYou safely return to your own time. Time journey ended.")
def run():
  time_travel_adventure()
