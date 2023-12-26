H, W = map(int, input().split())
blocks = list(map(int, input().split()))

water_blocks = 0

for top in range(1, W - 1):
    left_top = max(blocks[:top])
    right_top = max(blocks[top + 1:])

    dam = min(left_top, right_top)

    if blocks[top] < dam:
        water_blocks += dam - blocks[top]

print(water_blocks)