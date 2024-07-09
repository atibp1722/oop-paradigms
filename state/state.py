#program acts as a state machine
#implementations can onl exists in a certain number of states and cannot deviate from them
#state itself in encapsulated in an obect, so it can be passed around the program
#objct changes it behavior accoording to the behavior of internal state
#programs are able to switch according throught he invoking of methods defined in interface pattern
#it is used when program uses many if-else statements that might cause chnage in behvior of object
#it helps to reduce conditional complexity by reducing bulky codes related to condiitonal logic
#it allows to create new states without affeting already existing ones

from __future__ import annotations
import random
from abc import ABC,abstractmethod

class Game:

    def __init__(self):
        self.state=WelcomeScreenState(self)

    def change_state(self,state):
        self.state=state

class State(ABC):

    def __init__(self,game):
        self.game=game

        print(f"Current status is {self} state")

    @abstractmethod
    def game_welcome_screen(self):
        pass

    @abstractmethod
    def game_playing(self):
        pass

    @abstractmethod
    def game_pause(self):
        pass

    @abstractmethod
    def game_end(self):
        pass

class WelcomeScreenState(State):

    def game_welcome_screen(self):
        print('This is the game load screen...')

    def game_playing(self):
        self.game.change_state(PlayingState(self.game))

    def game_pause(self):
        print('You cannot go from load screen to pause screen...')

    def game_end(self):
        print('You cannot go from load screen to end screen...')

class PlayingState(State):

    def game_welcome_screen(self):
        print('You canot go from play screen to load screen...')

    def game_playing(self):
        print('Game is currently being played...')

    def game_pause(self):
        self.game.change_state(PauseState(self.game))

    def game_end(self):
        self.game.change_state(EndState(self.game))

class PauseState(State):

    def game_welcome_screen(self):
        print('You canot go from pause screen to load screen...')

    def game_playing(self):
        self.game.change_state(PlayingState(self.game))

    def game_pause(self):
        print('Game is currently on pause...')

    def game_end(self):
        print('You canot go from pause screen to end screen...')

class EndState(State):

    def game_welcome_screen(self):
        self.game.change_state(WelcomeScreenState(self.game))

    def game_playing(self):
        print('You canot go from end screen to play screen...')

    def game_pause(self):
        print('You canot go from end screen to pause screen...')

    def game_end(self):
        print('End screen currently in use...')

if __name__=='__main__':
    game=Game()
    for i in range(25):
        state=random.randrange(4)
        if state==0:
            print('Go to load screen...')
            game.state.game_welcome_screen()
        elif state==1:
            print('Go to playing screen...')
            game.state.game_playing()
        elif state==2:
            print('Go to pause screen...')
            game.state.game_pause()
        else:
            print('Go to end screen...')
            game.state.game_end()
            