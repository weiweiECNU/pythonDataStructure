import random
def randomIntList( num ):
    """随机生成包含 num 个整数的数组"""
    alist = []
    for i in range(num):
        alist.append(random.randint(1,100))
    
    return alist

alist = randomIntList(20)


def selection_sort(alist,ascending = True):
    """𝑂(𝑛2). However, due to the reduction in the number of exchanges, 
    the selection sort typically executes faster in benchmark studies. 
    In fact, for our list, the bubble sort makes 20 exchanges, while the selection sort makes only 8.
    
    它每遍历一次列表只交换一次数据，即进行一次遍历时找 到最大的项，完成遍历后，再把它换到正确的位置。
    和冒泡排序一样，第一次遍历后，最大的数 据项就已归位，第二次遍历使次大项归位。
    这个过程持续进行，一共需要n-1次遍历来排好n个数 据，因为最后一个数据必须在第n-1次遍历之后才能归位。
    
    """

    for fillslot in range(len(alist)-1,0,-1):
        maxLocation = 0
        for location in range(1, fillslot+1):
            if ascending:
                if alist[location] > alist[maxLocation]:
                    maxLocation = location
            else:
                if alist[location] < alist[maxLocation]:
                    maxLocation = location
        
        alist[fillslot], alist[maxLocation] = alist[maxLocation], alist[fillslot]

    return alist

print(selection_sort(alist,ascending= False))
