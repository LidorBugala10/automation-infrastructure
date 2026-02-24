class SportTruthOrLie:
    def __init__(self):
        self.score = 0
    def play_the_game(self):
        print("🏆Truth or Lie – Sports Edition Game🏆")
        print("Answer each question with: true / false")
        print("Good luck!\n")
        answer = input("A soccer match lasts 90 minutes: ").lower()
        if answer == "true":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("Basketball was invented before soccer: ").lower()
        if answer == "false":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("The Olympics are held every 4 years: ").lower()
        if answer == "true":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("Was Israel ever in the World Cup: ").lower()
        if answer == "true":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("Women's football became an Olympic sport in 1996: ").lower()
        if answer == "true":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("In soccer, a red card means a temporary timeout: ").lower()
        if answer == "false":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("A soccer team has 11 players on the field: ").lower()
        if answer == "true":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("A goalkeeper can use hands anywhere on the field: ").lower()
        if answer == "false":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("A yellow card is a warning: ").lower()
        if answer == "true":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        answer = input("Extra time is always played in every soccer match: ").lower()
        if answer == "false":
            print("✅Correct!")
            self.score += 1
        else:
            print("❌Wrong!")
        self.show_results()
    def show_results(self):
        print("\n🎯Final score:", self.score, "/ 10")
        if self.score == 10:
            print("you're a true genius")
        elif self.score >= 5:
            print("Great job!")
        else:
            print("Nice try! Keep practicing.")
def run():
      game = SportTruthOrLie()
      game.play_the_game()


