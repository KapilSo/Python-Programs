'''
1 for Snake
-1 for Water
0 for Gun
'''
import random
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]
# By now we have 2 numbers(variables), you and computer
print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")
if(computer == you):
    print("It's a draw.")
else:
    '''
    if(computer == -1 and you == 1): (computer - you) = -2
        print("You Win! Snake drinks water.")
    elif(computer == -1 and you == 0): (computer - you) = -1
        print("You Lose! Water destroys gun.")
    elif(computer == 1 and you == 0): (computer - you) = 2
        print("You Win! Gun shoots snake.")
    elif(computer == 1 and you == -1): (computer - you) = 1
        print("You Lose! Snake drinks water.")
    elif(computer == 0 and you == -1): (computer - you) = 1
        print("You Win! Water destroys gun.")
    elif(computer == 0 and you == 1): (computer - you) = -1
        print("You Lose! Gun shoots snake.")
    else:
        print("Invalid Input!")
        The below logic is written on the basis of the value of computer - you
        '''
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Lose!")
    else:
        print("You Win!")
