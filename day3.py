# read input file
file = open('input/day3.txt', 'r')
input = file.readlines()

# body of solution
gamma = []
epsilon = []

for i in range(len(input[0]) - 1):
    zeros=0
    ones=0
    for line in input:
        if line[i] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
