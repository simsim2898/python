word = input()
time = 0
for n in word:
    if n in "ABC":
        time += 3
    elif n in "DEF":
        time += 4
    elif n in "GHI":
        time += 5
    elif n in "JKL":
        time += 6
    elif n in "MNO":
        time += 7
    elif n in "PQRS":
        time += 8
    elif n in "TUV":
        time += 9
    elif n in "WXYZ":
        time += 10
    elif n in " ":
        time += 2
    else:
        time += 11
print(time) 
