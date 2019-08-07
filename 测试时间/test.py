from timeit import Timer

def test1():
    l = []
    for i in range(10000):
        l = l + [i]

def test2():
    l = []
    for i in range(10000):
        l.append(i)

    
t1 = Timer("test1()","from __main__ import test1")
print("",t1.timeit(number=1000),"milliseconds")

import profile

