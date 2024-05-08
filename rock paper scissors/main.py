import random

done = False
wins, losses, ties = 0, 0, 0

names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
loses = {'R': 'S', 'P': 'S', 'S': 'R'}

while not done:
    choice = input('Please choose your next Move (R, P, S) (Q to quit): ').upper()
    cpu_choice = random.choice(['R', 'P', 'S'])
    if choice == cpu_choice:
        print(f"It's a tie! You both chose {names[choice]}")
        ties += 1
    elif choice in ['R', 'P', 'S']:
        if cpu_choice == loses[choice]:
            print(f'CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}')
            losses += 1
        else:
            print(f'You win! You chose {names[choice]}, CPU chose {names[cpu_choice]}')
            wins += 1

    elif choice == 'Q':
        done = True
    else:
        print('Invalid Command')

    print(f'Current Stats: {wins} Wins, {losses} Losses, {ties} Ties')
