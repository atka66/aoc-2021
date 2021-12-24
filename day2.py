# read input file
file = open('input/day2.txt', 'r')
input = file.readlines()

# body of solution
hor = 0
depth = 0

for line in input:
    if line.startswith("forward"):
        hor += int(line[8:])
    if line.startswith("down"):
        depth += int(line[5:])
    if line.startswith("up"):
        depth -= int(line[3:])

print(hor * depth)