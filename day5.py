# read input file
file = open('input/day5.txt', 'r')
input = file.readlines()

# body of solution
vents = {}
for line in input:
    vent = [(int(y[0]), int(y[1])) for y in [x.split(',') for x in line.strip().split(' -> ')]]
    ishor = vent[0][0] == vent[1][0]
    isver = vent[0][1] == vent[1][1]
    if ishor:
        a = vent[0][1]
        b = vent[1][1]
        if a > b:
            c = a
            a = b
            b = c
        for i in range(a, b + 1):
            index = str(vent[0][0]) + "," + str(i)
            if index in vents:
                vents[index] = vents[index] + 1
            else:
                vents[index] = 1
    if isver:
        a = vent[0][0]
        b = vent[1][0]
        if a > b:
            c = a
            a = b
            b = c
        for i in range(a, b + 1):
            index = str(i) + "," + str(vent[0][1])
            if index in vents:
                vents[index] = vents[index] + 1
            else:
                vents[index] = 1

result = 0
for vent in vents:
    if vents[vent] > 1:
        result += 1
print(result)