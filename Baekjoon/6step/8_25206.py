grade1 = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade2 = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
totalgrade = 0
Gradescale = 0

for _ in range(20):
    s, g1, g2 = input().split()
    g1 = float(g1)
    if g2 != 'P':
        totalgrade += g1
        Gradescale += g1 * grade2[grade1.index(g2)]

if totalgrade > 0:
    print(format(Gradescale / totalgrade, ".6f"))
else:
    print("0.000000")