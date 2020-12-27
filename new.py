import random
def play():
    comp = random.choice(['r', 'p', 's'])
    human = input('please choose either (r), (p), or (s): ')
    if human == comp:
        print('it\'s a tie')
    elif human == 'r' and comp == 'p':
        print('you have lost')
    elif human == 'p' and comp == 'r':
        print('you win')
    elif human == 's' and comp == 'p':
        print('you win')
    elif human == 'p' and comp == 's':
        print('you have lost')
    elif human == 'r' and comp == 's':
        print('you win')
    elif human == 's' and comp == 'r':
        print('you have lost')

def quit():
    print('thanks for playing with me')

play()
while True:
    go_on = input('would you like to play again?: yes or no: ')
    if go_on == 'yes':
        play()
    else:
        quit()
        break
