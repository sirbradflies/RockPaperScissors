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
        self.plays = pd.DataFrame()
        self.model = MultinomialNB()

    def next_play(self, last_opponent_play: Play = None) -> Play:
        round = len(self.plays)
        if last_opponent_play:
            self.plays.loc[round - 1, "opponent"] = last_opponent_play.value

        if round > self.memory:
            X = pd.concat([self.plays.shift(l).add_suffix(f"_{l}")
                           for l in range(self.memory)], axis=1).dropna()
            y = X["opponent_0"].shift(-1).dropna()
            clean_idx = X.index.intersection(y.index)
            self.model.fit(X.loc[clean_idx], y.loc[clean_idx])

            X_pred = X.iloc[-1:]
            next_play = rpsbot.LOSES[Play(self.model.predict(X_pred)[0])]
        else:
            next_play = random.choice(list(Play))
        self.plays.loc[round, "self"] = next_play.value
        return next_play
