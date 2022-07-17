# Simulate several games of war to determine its properties

from sys import path as pythonpath
pythonpath.append('../../')
from war.game import play_war
import pickle
import time
import multiprocessing as mp

num_turns = []
num_sims = int(1e6)
t1 = time.time()

def simulate(i):
    try:
        var = play_war(debug=False, index=i)
    except:
        var = 0
    return var

# Let's get fancy with parallel processing
pool = mp.Pool(mp.cpu_count())

# This will include zeros, showing we ran into an exception
num_turns = pool.map(simulate, range(num_sims))

# This will not include zeros from exceptions
num_turns = [i for i in num_turns if i != 0]

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