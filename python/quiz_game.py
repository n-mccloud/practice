print("Welcome to the Quiz Game!")

play = input("Do you want to play? (yes/no): ")

if play == "yes":
    print("Let's start the quiz!")
else:
    print("Thank you for playing!")
    exit()

print("What is the capital of France?")

answer = input("Enter your answer: ")

if answer == "Paris":
    print("Correct!")
else:
    print("Incorrect!")

