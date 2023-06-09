import sys
import heapq as hq

inp = sys.stdin.readline
N = int(inp())
heap = []

for _ in range(N):
    x = int(inp())
    if x == 0:
        if heap == []:
            print(0)
        else:
            print(hq.heappop(heap)[1])
    else:
        hq.heappush(heap, (-x, x))