# read input file
file = open('input/day3.txt', 'r')
input = file.readlines()

# body of solution
bitlen = len(input[0])

oxylist = input.copy()
while len(oxylist) > 1:
    for i in range(bitlen - 1):
        if len(oxylist) <= 1:
            break
        zeros=0
        ones=0
        for line in oxylist:
            if line[i] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            oxylist = [x for x in oxylist if x[i] == '0']
        elif zeros < ones:
            oxylist = [x for x in oxylist if x[i] == '1']
        else:
            oxylist = [x for x in oxylist if x[i] == '1']

colist = input.copy()
while len(colist) > 1:
    for i in range(bitlen - 1):
        if len(colist) <= 1:
            break
        zeros=0
        ones=0
        for line in colist:
            if line[i] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            colist = [x for x in colist if x[i] == '1']
        elif zeros < ones:
            colist = [x for x in colist if x[i] == '0']
        else:
            colist = [x for x in colist if x[i] == '0']

print(int(''.join(oxylist[0].strip()), 2) * int(''.join(colist[0].strip()), 2))