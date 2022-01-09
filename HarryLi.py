# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:53:24 2022

@author: Harry
"""

# %%
import axelrod as axl

# Store the list of strategies as an array
first_players = [s() for s in axl.axelrod_first_strategies]
number_of_strategies = len(first_players)
for player in first_players:
     print(player)

first_tournament = axl.Tournament(
      players = first_players,
      turns = 200,
      repetitions = 5,
      seed = 1,
)

first_results = first_tournament.play()

for name in first_results.ranked_names:
     print(name)
     
plot = axl.Plot(first_results)
plot.boxplot();

# %% Harry's tournament with Lenient Grim Trigger
from axelrod import harry_tournament

players = [s() for s in harry_tournament]
number_of_strategies = len(players)
for p in players:
     print(p)
     
tournament = axl.Tournament(
      players = players,
      turns = 200,
      repetitions = 5,
      seed = 1,
)
results = tournament.play()

for name in results.ranked_names:
     print(name)

plot = axl.Plot(results)
plot.boxplot();