def solution(absolutes, signs):
    return sum([j if signs[i] else -j for i, j in enumerate(absolutes)])