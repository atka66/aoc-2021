# read input file
file = open('input/day1.txt', 'r')
input = file.readlines()

# body of solution
incs = 0
prev = None
for line in input:
    measurement = int(line.strip())
    if prev:
        if prev < measurement:
            incs += 1
    prev = measurement
print(incs)