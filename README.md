This was an exercise for CS260: Data Structures & Algorithms. There is
almost no error handling due to the scope of the class.

Files included:
* README
* fib_normal.py
* fib_memoize.py
* time.py
* makefile 

##fib_normal.py
fib_normal.py demostrates calculating fibonacci numbers without memoizaion. An environment variable called NUM has to be defined to work. In order to do this you can define the variable then call the command.
```
NUM=4 make problem1
```

##fib_memoize.py
fib_memoize.py demostrates calculating fibonacci numers with memoization. An
enviornment variable called NUM has to be defined to work. In order to do
this you can define the variable then call the command.
```
NUM=5 make problem2
```

##time.py
time.py demonstrates the speed memoization has over normal fibonacci
calculation. Environmental variables are unnecessary. 
```
make problem3
```

######All three can be demonstrated by running:
```
NUM=7 make run
````
