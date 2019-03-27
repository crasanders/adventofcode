import numpy as np
from collections import defaultdict

boxids = np.loadtxt('boxids.txt', dtype=str)

counts = {2: 0, 3: 0}

for id in boxids:
    lettercounts = defaultdict(int)
    for letter in id:
        lettercounts[letter] += 1
    if 2 in lettercounts.values():
        counts[2] += 1
    if 3 in lettercounts.values():
        counts[3] += 1

print(counts[2] * counts[3])