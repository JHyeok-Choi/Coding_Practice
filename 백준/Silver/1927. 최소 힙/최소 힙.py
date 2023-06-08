import sys, heapq
inp = sys.stdin.readline

N = int(inp())
heap = []

for _ in range(N):
    x = int(inp())
    if x == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
            