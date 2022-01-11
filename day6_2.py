# read input file
import numpy

dayMap = numpy.bincount(numpy.fromfile('input/day6.txt', dtype=int, sep=','), minlength=9)
for i in range(256):
    dayMap = numpy.roll(dayMap, -1)
    dayMap[6] += dayMap[8]
print(dayMap.sum())
