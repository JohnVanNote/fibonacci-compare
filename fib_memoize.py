#!usr/bin/env python
#
# fib_memoize.py
#
# Calculates Fibonacci numbers WITH memoization
#

import sys

def fib_mem(n, memo):
    print memo
    n = n - 1
    if n < 3:
        memo[n] = 1
    if memo[n] != 0:
      return memo[n]
    memo[n] = fib_mem(n-1, memo) + fib_mem(n-2, memo)
    return memo[n]
    #else:
    #    a = [0, 1]
    #    a.append(fib_mem(n-1) + fib_mem(n-2))
    #return a

def init_default_array(size, value):
    l = list()
    for i in range(size):
        l.append(value)
    return l

def main(argv=sys.argv):
    num = int(argv[1])
    memo = init_default_array(num, 0)
    fib = fib_mem(num, memo)
    print fib

if __name__ == "__main__":
    main()
