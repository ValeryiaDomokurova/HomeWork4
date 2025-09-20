def missing_statues(statues):
    statues.sort()
    miss = 0
    for i in range(1, len(statues)):
        gap = statues[i] - statues[i - 1]

        if gap > 1:
            miss += gap - 1

    return miss
