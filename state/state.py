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
        pass

    def game_playing(self):
        pass

    def game_pause(self):
        pass

    def game_end(self):
        pass

class PlayingState(State):

    def game_welcome_screen(self):
        pass

    def game_playing(self):
        pass

    def game_pause(self):
        pass

    def game_end(self):
        pass

class PauseState(State):

    def game_welcome_screen(self):
        pass

    def game_playing(self):
        pass

    def game_pause(self):
        pass

    def game_end(self):
        pass

class EndState(State):

    def game_welcome_screen(self):
        pass

    def game_playing(self):
        pass

    def game_pause(self):
        pass

    def game_end(self):
        pass