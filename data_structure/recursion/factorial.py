def factorial( num ):
    """写一个递归函数来计算一个数的阶乘。

    基本结束条件 : num 为 1
    演进: 乘数 递减 1
    """
    if num == 1:
        return 1
    else:
        return num * factorial( num - 1)
    
print(factorial(1))