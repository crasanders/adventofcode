import numpy as np

frequencies = np.loadtxt('frequencies.txt')
nfreq = len(frequencies)
reached = {0 : True}
cur = 0
i = 0
while True:
    f = frequencies[i]
    cur += f
    if cur in reached:
        print(cur)
        break
    else:
        reached[cur] = True
    i += 1
    if i >= nfreq:
        i = 0