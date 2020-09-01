def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
x=fib(5)
for i in x:
    print i
