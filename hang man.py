import random
word=["fruit","meat","lunch","work","bead"]
computer=random.choice(word)
clue=["_" for _ in computer]
lives=6
previous=set()


while True:
    print("\n"," ".join(clue))
    guess=input("choose a letter: ")
    if guess in previous:
        print("try another letter")
        continue

    previous.add(guess)

    if guess in computer:
        print("found a letter")
        for i in range(len(computer)):
            if computer[i]==guess:
                clue[i]=guess
    elif "_" not in clue:
        print(" ".join(clue))
        print("YOU WIN!")
        break
    else:
        print("nope, not in there")
        lives-=1
        if lives==0:
            print("you lose!the word was",computer)
            break    
