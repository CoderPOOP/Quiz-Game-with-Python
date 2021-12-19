import time

questions = 0
print("Welcome to my Quiz Game")
time.sleep(2)
start = input("Do you want to play?\n")
if start.lower() != "yes":
    print("Ok! Bye!!")
    quit()

time.sleep(2)
print("Ok! lets play the game")
time.sleep(2)
print("You'll get 1 points for a correct answer and 0 points for a incorrect answer")
score = 0

answer = input("What is the full form of CPU?\n")
questions += 1
if answer.lower() == "central processing unit":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer!")
time.sleep(2)
print("Score = " , score)

answer = input("What is the full form of GPU?\n")
questions += 1
if answer.lower() == "graphics processing unit":
    print("Correct Answer!")
    score += 1
    print("Score increased by 1")
else:
    print("Incorrect Answer!")
    print("Score remains " , score)
    
print("Score = " , score)

answer = input("What is the full form of RAM?\n")
questions += 1
if answer.lower() == "random access memory":
    print("Correct Answer!")
    score += 1
    print("Score increased by 1")
else:
    print("Incorrect Answer!")
    print("Score remains " , score)
    
print("Score = " , score)

#ending
print("You got " , str(score) , "out of " , str(questions) , "questions correct")