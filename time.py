#!usr/bin/env python
#
# John Van Note
#
# Calculates time for fib_norm and fib_mem functions
#

import timeit
import fib_normal
import fib_memory

def main():
    for i in range(0, 31):
        normTime = timeit.Timer("fib_norm(i)", "from fib_normal import fib_norm; from __main__ import i")
        memTime = timeit.Timer("fib_mem(i)", "from fib_memory import fib_mem, a; from __main__ import i")
        num = str(i)
        nTime = str(normTime.timeit(1))
        mTime = str(memTime.timeit(1))
        print num + " " + nTime + "\t" + mTime

    f= open("mydata.txt", "w")
    for i in range(0, 101):
        fastTime = timeit.Timer("fib_mem(i)", "from fib_memory import fib_mem, a; from __main__ import i")
        f.write(str(i) + " " + str(fastTime.timeit(1)) + "\n")
    f.close()

if __name__ == '__main__':
    main()
