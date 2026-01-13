#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']
    my_move = None
    their_move = None

    def move(self):
        self.their_move = random.choice(self.moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, Paper, Scissors?\n"
                           "(Type 'exit' to leave the game)\n").lower()
            if choice in self.moves:
                print(f"You played {choice}\n")
                return choice
            elif choice == 'exit':
                print("That's all folks!\n")
                exit()
            else:
                print("Invalid Input, please try again...\n")

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)

    def learn(self, my_move, their_move):
        pass


class CopyPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(self.moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if self.beats(move1, move2):
            print("*** PLAYER ONE WINS! ***")
            self.p1.score += 1
        elif self.beats(move2, move1):
            print("*** PLAYER TWO WINS! ***")
            self.p2.score += 1
        else:
            print("*** TIE! ***")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        while True:
            try:
                playrounds = int(input("How many rounds would "
                                 "you like to play? (max 10)\n"))
                if playrounds > 0 and playrounds <= 10:
                    print(f"Playing {playrounds} rounds\n")
                    break
                else:
                    print("choose again....")
            except ValueError:
                print("Invalid Input, please try again...\n")
        print("Game start!")
        for round in range(playrounds):
            print(f"Round {round + 1}:")
            self.play_round()
            print(f"Score: {self.p1.score} : {self.p2.score}\n")
        self.results()

    def results(self):
        if self.p1.score > self.p2.score:
            print("\n\n*** PLAYER ONE WON THE GAME!! *** ")
        elif self.p1.score < self.p2.score:
            print("\n\n*** PLAYER TWO WON THE GAME!! *** ")
        else:
            print("TIE!!!")
        print("Game over!")


if __name__ == '__main__':
    npc = random.choice([RockPlayer(), RandomPlayer(),
                         CopyPlayer(), CyclePlayer()])
    game = Game(HumanPlayer(), npc)
    print(npc)
    game.play_game()
