from deque import Deque

def palchecker( word ):
    """编写一个算法来检查放入的字符串是否为回文词。"""
    charDeque = Deque()
    for char in word:
        charDeque.addRear(char)

    isPal = True 
    while isPal and charDeque.size() > 1:
        first = charDeque.removeFront()
        second = charDeque.removeRear()
        if first != second:
            isPal = False

    return isPal


