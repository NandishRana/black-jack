#from art import logo
import random
#import os

def ace(deck):
    if 11 in deck and sum(deck) > 21:
        deck[deck.index(11)] = 1 

def card_gen(u, c):
    for _ in range(u):
        usr_cards.extend([random.choice(cards)])
    for _ in range(c):
        cmp_cards.extend([random.choice(cards)])


def move(turn):
    if turn == 'y':
        card_gen(1, 0)
        ace(usr_cards)
        print(
            f"	Your cards: {usr_cards}. current score: {sum(usr_cards)}\n	Computer's first card: {cmp_cards[0]}"
        )
    elif turn == 'n':
        while sum(cmp_cards) < 17:
            card_gen(0, 1)
            ace(cmp_cards)
        print(
            f"	Your final hand: {usr_cards}, final score: {sum(usr_cards)}\n	Computer's final hand: {cmp_cards}, final score: {sum(cmp_cards)}"
        )


def win_lose():
    if sum(usr_cards) == 21 and len(usr_cards) == 2:
        print("Win with a BlackJack 😎")
    elif sum(cmp_cards) == 21 and len(cmp_cards) == 2:
        print("Lose, opponent has BlackJack 😱")
    elif sum(usr_cards) > sum(cmp_cards):
        if sum(usr_cards) > 21:
            print("You went over, You lose 😭")
        else:
            print("You win 😃")
    elif sum(usr_cards) < sum(cmp_cards):
        if sum(cmp_cards) > 21:
            print("Opponent went over, You win 😁")
        else:
            print("You lose 😤")
    else:
        print("It's a Draw 🙃")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play_game == 'y':

    usr_cards = []
    cmp_cards = []

    #os.system("clear")
    #print(logo)

    if play_game == 'n':
        break
    else:
        card_gen(2, 2)
        print(
            f"	Your cards: {usr_cards}. current score: {sum(usr_cards)}\n	Computer's first card: {cmp_cards[0]}"
        )
        if sum(usr_cards) == 21 or sum(cmp_cards) == 21:
            win_lose()
            

    while sum(usr_cards) <= 21 and sum(cmp_cards) < 17:
        next_move = input("Type 'y' to get another card, type 'n' to pass: ")
        move(next_move)

    win_lose()

    play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")