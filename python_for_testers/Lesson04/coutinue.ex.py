words = []
while True :
    word = input("Enter a word: ")
    if word.lower()=="stop":
        print(f"You entered : {word}")
        break
    if len(word)<3:
        continue
    words.append(word)
    print(f"words with 3 or more letters:{words}")
    for w in words:
        print(w)