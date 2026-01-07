logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def user(lst):
    lst.append(random.choice(cards))
    return lst

def comp(lst):
    lst.append(random.choice(cards))
    return lst

def check_comp(comp_cards):
    while sum(comp_cards)<17:
        comp_cards = comp(comp_cards)
    return comp_cards

def winner(you,com,userCards,compCards):
    print(f" Your final hand: {userCards}, final score: {sum(userCards)}")
    print(f"Computer's final hand: {compCards}, final score: {sum(compCards)}")
    if com==21 and len(compCards)==2:
        print("Lose, opponent has Blackjack 😱")
    elif you==21:
        print("you won with a Blackjack!😎")
    elif you>21:
        print("You went over. You lost!")
    elif com>21:
        print("Computer went over. you win!")
    elif you>com:
        print("You win.🥳")
    elif you==com:
        print("It's a Draw. 🙃")
    else:
        print("You lost!😭")



def play_game():
    print(logo)
    user_cards = user(user([]))
    computer_cards = comp([])

    pass_or_hit='y'
    while pass_or_hit=='y':
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card {computer_cards[0]}")

        if sum(user_cards)==21 or sum(computer_cards)==21:
            winner(sum(user_cards), sum(computer_cards), user_cards, computer_cards)
            break

        pass_or_hit = input("Type 'y' to get another card, type 'n' to pass:").lower()


        if pass_or_hit=='y':
            user_cards = user(user_cards)
            if sum(user_cards)>21 and 11 in user_cards:
                user_cards[user_cards.index(11)]=1
            elif sum(user_cards)>21:
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's first card {computer_cards[0]}")

                winner(sum(user_cards), sum(computer_cards), user_cards, computer_cards)
                pass_or_hit='n'
        else:
            pass_or_hit='n'
            computer_cards = check_comp(computer_cards)
            winner(sum(user_cards),sum(computer_cards),user_cards,computer_cards)
    
while input("\n Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=='y':
    print("\n"*50)
    play_game()

