# Fromual? F(N)= ((N(N + 1))/2) + 1
# Using Triangular Number formula + 1

def walk(N):
    return int((((N * N) + N) / 2) + N)


T = int(input())
A = []
for i in range(T):
    A.append(int(input()))

for x in A:
    print(walk(x))