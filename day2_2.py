# read input file
file = open('input/day2.txt', 'r')
input = file.readlines()

# body of solution
hor = 0
depth = 0
aim = 0

for line in input:
    if line.startswith("forward"):
        val = int(line[8:])
        hor += val
        depth += val * aim
    if line.startswith("down"):
        val = int(line[5:])
        aim += val
    if line.startswith("up"):
        val = int(line[3:])
        aim -= val

print(hor * depth)