"""
Naive Rock-Paper-Scissors bot plays randomly.
"""

import random
from rpsbot import RPSBot, Play


class RandomBot(RPSBot):
    def next_play(self, last_opponent_move: Play = None) -> Play:
        return random.choice(list(Play))