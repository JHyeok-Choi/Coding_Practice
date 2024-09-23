from heapq import heappush, heappop
import sys

N, *M = map(int, sys.stdin.read().split())
heap = []

for i in M:
    if not i :
        print(heappop(heap)[1] if heap else 0)
        continue

    heappush(heap, (abs(i), i))