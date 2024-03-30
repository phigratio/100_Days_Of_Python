t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    s = input()
    for j in range(n):
        if int(s[j]) < d:
            s = s[:j] + str(d) + s[j:]
            break
    else:
        s += str(d)
    print(s)