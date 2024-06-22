

from __future__ import print_function
import time
from Tiling import Tiling

fp = open("test2.txt", 'r')
fulllines = fp.readlines()
lines = []
for line in fulllines:
    lines.append(line.strip())


# Call the tiling dino function passing in the
# contents of the file
start = time.time()
td = Tiling()
result = td.compute(lines)
end = time.time()

for i in range(len(result)):
    print(result[i])
print("time: "+ str(end-start))
