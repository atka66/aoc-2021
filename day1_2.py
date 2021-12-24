# read input file
file = open('input/day1.txt', 'r')
input = file.readlines()

# body of solution
incs = 0
prev = []
prevSum = None
for line in input:
    measurement = int(line.strip())
    prev.insert(0, measurement)
    if len(prev) >= 3:
        if prevSum:
            if prevSum < sum(prev):
                incs += 1
        prevSum = sum(prev)
        prev.pop()
print(incs)