import random

print("Snake 🐍  Water 💧  Gun 🔫 Game")
choices = ['s', 'w', 'g']

user = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

if user == computer:
    print("It's a Draw!")

# Snake conditions
elif user == 's' and computer == 'w':
    print("You Win! Snake drinks water.")
elif user == 's' and computer == 'g':
    print("You Lose! Gun shoots snake.")

# Water conditions
elif user == 'w' and computer == 'g':
    print("You Win! Water destroys gun.")
elif user == 'w' and computer == 's':
    print("You Lose! Snake drinks water.")

# Gun conditions
elif user == 'g' and computer == 's':
    print("You Win! Gun shoots snake.")
elif user == 'g' and computer == 'w':
    print("You Lose! Water destroys gun.")

else:
    print("Invalid Input! Please enter s, w, or g.")
