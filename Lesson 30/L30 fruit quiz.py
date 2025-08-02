import random
class FruitQuiz:
    #create a constructor
    def __init__(self):
        #create a dictionary of fruits as keys and color as value
        self.fruits={'apple':'red',
                     'grape':'purple',
                     'watermelon':'green',
                     'banana':'yellow'}
        
    #function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))

            print(f"What is the color of {fruit}")
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("Enter 0, if you want to play again otherwise enter 1: "))
            if (option):
                break

print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()