def count_candles(candles, leftover):

    total = 0
    make_new = 0

    while candles > 0:
        total += candles
        make_new += candles
        candles = make_new // leftover
        make_new %= leftover
    return total
