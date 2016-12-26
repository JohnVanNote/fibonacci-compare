#!usr/bin/env python
#
# fib_normal.py
#
# Calculates Fibonacci numbers WITHOUT memoization
#

import sys

def fib_norm(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib_norm(number-1) + fib_norm(number-2)

def main(argv=sys.argv):
    fib = fib_norm(int(argv[1]))
    print fib

if __name__ == "__main__":
    main()
