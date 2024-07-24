n = int(input())

hexagon = 1
distance = 1

while hexagon < n:
    hexagon = 6 * distance + hexagon
    distance = 1 + distance
print(distance)
