# Fromual? F(N)= ((N(N + 1))/2) + N
# Using Triangular Number formula + N

def walk(N):
    return int((((N * N) + N) / 2) + N)


T = int(input())
A = []
for i in range(T):
    A.append(int(input()))

for x in A:
    print(walk(x))