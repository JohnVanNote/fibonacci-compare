#!usr/bin/env python
#
# fib_memoize.py
#
# John Van Note
#
# Calculates Fibonacci numbers WITH memoization
#

import sys

def fib_mem(number, memo=None):
    if number < 0:
        return 0
    if memo is None:
        memo = [0, 1]
    if len(memo) <= number:
        memo.append(fib_mem(number-2, memo) + fib_mem(number-1, memo))
    return memo[number]

def main(argv=sys.argv):
    num = int(argv[1])
    fib = fib_mem(num)
    print fib

if __name__ == "__main__":
    main()
