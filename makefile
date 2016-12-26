# makefile
#
# John Van Note
#

fib_norm=fib_normal.py
fib_mem=fib_memoize.py
time=timer.py

view: 
	cat $(fib_norm) $(fib_mem) $(time) | less

problem1:
	python $(fib_norm) $$NUM 

problem2: 
	python $(fib_mem) $$NUM

problem3: $(time)
	python $(time)
	
run: problem1 problem2 problem3

clean: 
	rm -r *.pyc
