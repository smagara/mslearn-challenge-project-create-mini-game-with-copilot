# write 'hello world' to the console
print('hello world')

#implement a rock/paper/scissors game
import random
#prompt user to enter a choice
user_choice = input('Enter rock, paper, or scissors: ')
#generate a random choice for the computer
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f'Computer choice: {computer_choice}')
#determine the winner
if user_choice == computer_choice:
    print('It is a tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:
    print('Computer wins!')



