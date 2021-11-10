import time

def edit_recursive(x,y):
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    elif x[-1] == y[-1]:
        return edit_recursive(x[:-1], y[:-1])
    else:
        return 1 + min(
            edit_recursive(x, y[:-1]),         # Insertion
            edit_recursive(x[:-1], y[:-1]),    # Substitution
            edit_recursive(x[:-1], y)          # Deletion
        )

def edit_dynamic(x,y):

    if len(x) > len(y):
        x, y = y, x

    distances = range(len(x) + 1)
    for i2, c2 in enumerate(y):
        distances_ = [i2+1]
        for i1, c1 in enumerate(x):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1],
                                           distances[i1 + 1],
                                           distances_[-1]))
                                  )
        distances = distances_
    return distances[-1]



s = {"ACTGTTTGGTC" : "ACTGTCTGGTC","ACTGTTTGGTCAC" : "ACTGTCTGGTCCA","ACTGTTTGGTCACCT" : "ACTGTCTGGTCACCC","ACTGTTTGGTCATATAT" : "ACTGTCTGGTCATTATA",}
counter = 1

for x in s:
    y = s[x]

    start = time.time()
    edit_recursive(x,y)
    print(str(counter),"Recursive:", "Time: ", time.time() - start, "Seq_length:", len(x))

    start = time.time()
    edit_dynamic(x,y)
    print(str(counter),"Dynamic:", "Time: ", time.time() - start,"Seq_length:", len(x))
    counter += 1




