# read input file
from collections import defaultdict


file = open('input/day6.txt', 'r')
input = file.readlines()

dayMap = defaultdict(int)

def iterate():
    for i in range(0, 9):
        dayMap[i-1] = dayMap[i]
    dayMap[6] += dayMap[-1]
    dayMap[8] = dayMap[-1]

# body of solution
for i in list(map(int, input[0].strip().split(','))):
    dayMap[i] += 1

for i in range(80):
    iterate()

del dayMap[-1]
print(sum(dayMap.values()))