def fibonacciRecurion( num ):
    """写一个递归函数来计算斐波那契数列。递归函数的性能和利用迭代计算的方法来比较，效果如何?
    num 斐波那契数列的总项数
    
    基本结束条件 : num == 2
    演进: 前两项之和
    """
    if num <= 2:
        return 1
    else:
        return fibonacciRecurion(num - 2) + fibonacciRecurion(num - 1)

def fibonacciIteration( num , historyList):
    """利用迭代计算"""
    for i in range( num + 1):
        if i == 0:
            historyList[i] = 0
        elif i <= 2:
            historyList[i] = 1
        else:
            historyList[i] = historyList[ i-1 ] + historyList[i-2]
    
    return historyList[num]



#print(fibonacciRecurion(5)) #0.063 seconds
#print(fibonacciRecurion(10)) # 0.053 seconds
#print(fibonacciRecurion(20)) # 0.049 seconds
#print(fibonacciRecurion(50))
#print(fibonacciIteration(5,[0]*6))

#print(fibonacciIteration(10,[0]*11)) 
#print(fibonacciIteration(20,[0]*21)) 
#print(fibonacciIteration(50,[0]*51))

