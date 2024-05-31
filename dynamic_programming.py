import random
import math
def dynamic_programming(n, c, w, v):
    if n == -1 or c == 0:
        result = 0
    elif w[n] > c:
        result = dynamic_programming(n-1, c, w, v)
    else:
        tmp1 = dynamic_programming(n-1, c, w, v)
        tmp2 = v[n] + dynamic_programming(n-1, c-w[n], w, v)
        result = max(tmp1, tmp2)
    return result

w = []
v = []

for i in range(0, 100):
    w.append(random.randint(0, 1000))
for i in range(0, 100):
    v.append(random.randint(0, 500))
print(dynamic_programming(len(w) - 1, 1000, w, v))
print(math.pow(2, 100))