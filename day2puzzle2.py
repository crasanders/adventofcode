import numpy as np

boxids = np.loadtxt('boxids.txt', dtype=str)

for i, id1 in enumerate(boxids[:len(boxids)-1]):
    for j, id2 in enumerate(boxids[i+1:]):
        ids = np.array(list(zip(id1, id2)))
        diff = (ids[:, 0] != ids[:, 1])
        if diff.sum() == 1:
            ans = ''.join([id1[i] for i in range(len(id1)) if not diff[i]])
            print(ans)
            break
    else:
        continue
    break




