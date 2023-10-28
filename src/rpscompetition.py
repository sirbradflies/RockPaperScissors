"""
Class to simulate a competition between two rps bots
"""

import argparse

import rpsbot
from naivebot import NaiveBot
from randombot import RandomBot
from frequency import FrequencyBot
from bayesbot import BayesBot

BOTS = {
    "random": RandomBot,
    "naive": NaiveBot,
    "frequency": FrequencyBot,
    "bayes": BayesBot
}


def main():
    parser = argparse.ArgumentParser(description="Simulate a competition between two rps bots.")
    parser.add_argument("-b1", "--bot1", type=str,
                        help="Bot 1 to use in the competition.",
                        default="naive")
    parser.add_argument("-b2", "--bot2", type=str,
                        help="Bot 2 to use in the competition.",
                        default="random")
    parser.add_argument("-r", "--rounds", type=int,
                        help="Number of rounds to simulate.",
                        default=100)
    args = vars(parser.parse_args())
    bot1 = BOTS[args["bot1"]]()
    bot2 = BOTS[args["bot2"]]()
    scores = []
    last_play1, last_play2 = None, None
    for i in range(args["rounds"]):
        play1 = bot1.next_play(last_play2)
        play2 = bot2.next_play(last_play1)
        scores += [calculate_score(play1, play2)]
        last_play1, last_play2 = play1, play2
        print(f"Round {i+1}: {play1} vs {play2} -> {scores[-1]}")

    b1_wins = len(list(filter(lambda x: x == 1, scores)))
    b2_wins = len(list(filter(lambda x: x == 2, scores)))
    ties = len(list(filter(lambda x: x == 0, scores)))
    print(f"Final score: "
          f"{bot1} Wins {b1_wins} times ({b1_wins/args['rounds']:.1%}), "
          f"{bot2} Wins {b2_wins} times, ({b2_wins/args['rounds']:.1%}), "
          f"Ties {ties} times ({ties/args['rounds']:.1%}).")


def calculate_score(play1, play2):
    if rpsbot.WINS[play1] == play2:
        return 1
    elif rpsbot.LOSES[play1] == play2:
        return 2
    else:
        return 0


if __name__ == "__main__":
    main()
