# Simulate several games of war to determine its properties

from sys import path as pythonpath
pythonpath.append('../')
from war.game import play_war
import pickle
import time

num_turns = []
num_sims = int(2.5e4)
t1 = time.time()

for i in range(num_sims):
    try:
        num_turns.append(play_war(debug=False,
                                  index=i))
    except:
        pass

t2 = time.time()

print("Simulation time: {duration:.2f} seconds".format(
    duration = t2 - t1
))

print("{ratio:.2f}% of games were undetermined".format(
    ratio = 100. * (num_sims - len(num_turns)) / num_sims
))

output_file = open("results.pickle", "wb")
pickle.dump(num_turns, output_file)
output_file.close()