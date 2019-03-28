import numpy as np

sheet = np.zeros((1000, 1000))
with open('fabric_claims.txt', 'r') as claims:
    for claim in claims:
        claim = claim.split()
        x, y = claim[2][:-1].split(',')
        x = int(x)
        y = int(y)
        w, h = claim[-1].split('x')
        w = int(w)
        h = int(h)

        for i in range(w):
            for j in range(h):
                sheet[x+i, y+j] += 1

with open('fabric_claims.txt', 'r') as claims:
    for claim in claims:
        claim = claim.split()
        cid = claim[0]
        x, y = claim[2][:-1].split(',')
        x = int(x)
        y = int(y)
        w, h = claim[-1].split('x')
        w = int(w)
        h = int(h)

        overlap = False
        for i in range(w):
            for j in range(h):
                if sheet[x+i, y+j] > 1:
                    overlap = True

        if not overlap:
            print(cid)
