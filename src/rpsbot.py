"""
Abstract class for a Rock-Paper-Scissors bot.
"""

import enum
from abc import ABC, abstractmethod


class Play(enum.Enum):
   Rock = 1
   Scissor = 2
   Paper = 3


WINS = {Play.Rock: Play.Scissor,
        Play.Scissor: Play.Paper,
        Play.Paper: Play.Rock}

LOSES = {Play.Rock: Play.Paper,
         Play.Scissor: Play.Rock,
         Play.Paper: Play.Scissor}


class RPSBot(ABC):
    @abstractmethod
    def next_play(self, last_opponent_move: Play = None) -> Play:
        pass

    def __repr__(self):
        return self.__class__.__name__
