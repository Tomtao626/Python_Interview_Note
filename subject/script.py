m = [1, 2, [3]]
n = m[:]
n[1] = 4
n[2][0] = 5
print(f"m={m}")
print(f"n={n}")