from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000
MAX_CIVS = 5000
TRIALS = 1000
CIV_STEP_SIZE = 100


x=[]
y=[]

for num_civs in range(2,MAX_CIVS+2,CIV_STEP_SIZE):
    civs_per_vol = (num_civs/NUM_EQUIV_VOLUMES)
    num_single_civ=0
    for trial in range(TRIALS):
        locations=[]
        while len(locations)<num_civs:
            location=randint(1,NUM_EQUIV_VOLUMES)
            locations.append(location) #randomly allocating locations
        overlap_count=Counter(locations)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civ += overlap_rollup[1]

    prob = 1-(num_single_civ/(num_civs*TRIALS))

    print("{:.4f} {:.4f}".format(civs_per_vol,prob))

    x.append(civs_per_vol)
    y.append(prob)

print(x)
print(y)

