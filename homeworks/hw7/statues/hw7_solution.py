def miss_statues(statues):
    statues.sort()
    missing = 0
    for i in range(1, len(statues)):
        miss = statues[i] - statues[i - 1]

        if miss > 1:
            missing += miss - 1

    return missing
