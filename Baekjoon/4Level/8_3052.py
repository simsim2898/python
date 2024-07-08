aa = []
for i in range(10):
    a = int(input())
    if a % 42 not in aa:
        aa.append(a % 42)
print(len(aa))