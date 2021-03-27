def numPairsDivisibleBy60(self, time: List[int]) -> int:

    pairs = 0
    count = dict()

    for t in time:
        remainder = t % 60
        target = 60 - remainder if remainder != 0 else 0
        pairs += count.get(target, 0)
        count[remainder] = count.get(remainder, 0) + 1

    return pairs