import random 
def compare(a,b):
    if a == "Rock" and b =="Scissors":
        return("a")
    elif a == "Rock" and b =="Paper":
        return("b")
    elif a == "Paper" and b =="Scissors":
        return("b")
    elif a == "Paper" and b =="Rock":
        return("a")
    elif a == "Scissors" and b =="Rock":
        return("b")
    elif a == "Scissors" and b =="Paper":
        return("a")
    elif a == b :
        return("c")


def main():
    options = ["Rock","Paper","Scissors"]
    userChoice = input("Rock, Paper or Scissors ")
    cpuNumber = random.randint(0,3)
    cpuChoice=options[cpuNumber]
    print(cpuChoice)
    result = compare(userChoice,cpuChoice)
    if result == "a":
        print("Player wins")
    elif result == "b":
        print("Computer wins")
    elif result == "c":
        print("It's a draw")


main()