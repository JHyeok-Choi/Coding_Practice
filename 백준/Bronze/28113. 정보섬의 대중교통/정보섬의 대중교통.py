N, A, B = map(int, input().split())
C = B if B > N else N
print("Subway" if C < A else "Anything" if C == A else "Bus")