for i in range(3):
    a, b, c, x, y, z = map(int, input().split())
    start = a * 3600 + b * 60 + c
    end = x * 3600 + y * 60 + z
    end -= start
    print(end // 3600, (end % 3600) // 60, end  % 60)