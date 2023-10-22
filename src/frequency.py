"""
Frequency based bot playing the winning move of the most frequent opponent move.
"""

import random
from collections import Counter

import rpsbot
from rpsbot import RPSBot, Play


class FrequencyBot(RPSBot):
    def __init__(self, memory=10):
        self.memory = memory
        self.last_opponent_plays = []

    def next_play(self, last_opponent_move: Play = None) -> Play:
        if last_opponent_move:
            self.last_opponent_plays += [last_opponent_move]
        if len(self.last_opponent_plays) > 0:
            count = Counter(self.last_opponent_plays[-self.memory:])
            most_recurring = max(count, key=count.get)
            next_play = rpsbot.LOSES[most_recurring]
        else:
            next_play = random.choice(list(Play))
        return next_play