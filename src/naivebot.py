"""
Naive Rock-Paper-Scissors bot that always plays the same play.
"""

from rpsbot import RPSBot, Play


class NaiveBot(RPSBot):
    def __init__(self, play: Play=Play.Rock):
        self.play = play

    def next_play(self, last_opponent_move: Play = None) -> Play:
        return self.play