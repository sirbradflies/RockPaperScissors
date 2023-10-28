"""
Bayes based bot.
"""

import random
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

import rpsbot
from rpsbot import RPSBot, Play


class BayesBot(RPSBot):
    def __init__(self, memory=10):
        self.memory = memory
        self.last_opponent_plays = []
        self.last_own_play = []
        self.model = MultinomialNB()
        self.plays = pd.DataFrame(columns=['opponent', 'own'])
        self.last_own_play = None

    def next_play(self, last_opponent_play: Play = None) -> Play:
        if last_opponent_play:
            self.plays.loc[len(self.plays)] = [last_opponent_play.value, self.last_own_play.value]
        if len(self.plays) > self.memory+1:
            X_train = self.plays[-self.memory-1:-1]
            y_train = self.plays[-self.memory:]['opponent']
            self.model.fit(X_train, y_train)
            X_pred = self.plays[-self.memory:]
            next_play = rpsbot.LOSES[Play(self.model.predict(X_pred)[0])]
        else:
            next_play = random.choice(list(Play))
        self.last_own_play = next_play
        return next_play
