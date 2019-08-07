from unorderedList import UnorderedList
from timeit import Timer
from stack_with_linked_list import StackLinkedList

def test1():
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93) 
    mylist.add(26)
    mylist.add(54)

    mylist.search(93)
    mylist.remove(17)

    mylist.remove(31)

    mylist.remove(54)

    mylist.append(9)

    mylist.insert(1,54)

    mylist.insert(0,5)

    mylist.index(4)

    mylist.pop()
    mylist.slice(0,2)

def test2():
    mylist = []

    mylist.append(31)
    mylist.append(77)
    mylist.append(17)
    mylist.append(93) 
    mylist.append(26)
    mylist.append(54)

    93 in mylist
    mylist.remove(17)

    mylist.remove(31)

    mylist.remove(54)

    mylist.append(9)

    mylist.insert(1,54)

    mylist.insert(0,5)

    mylist[4]

    mylist.pop()
    mylist[0:2]

t1 = Timer("test1()","from __main__ import test1")
print("linked list", t1.timeit(number=1000),"ms")

t2 = Timer("test2()","from __main__ import test2")
print("list", t2.timeit(number=1000),"ms")

s  = StackLinkedList()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
s.pop()
s.pop()
print(s.size())
print(s)
