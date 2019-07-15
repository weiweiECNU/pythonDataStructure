def quickSort(alist):
    """快速排序
    
    调用了递归函数，quickSortHelper。
    """

    quickSortHelper(alist, 0, len(alist)-1 )


def quickSortHelper(alist, first, last):
    """从与归并排序相同的最基本的情况开始。如果列表长度小于或者等于1，那么它已经排过序。如果列表的长度更大，那么列表可以被分割并进行递归排序
    
    列表就可以在分割 点被分成两半然后快速排序可以在这两个部分被分别调用了。
    
    """
    if first < last:
        splitPostion = partition(alist, first, last)

        quickSortHelper(alist, first, splitPostion -1 )
        quickSortHelper(alist, splitPostion + 1, last)


def partition(alist, first, last):
    """
    分区过程
    快速排序首先选择一个中值。虽然有很多不同的方法来选择这个数值，我们将会简单地选择 列表里的第一项。
    分区过程由设置两个位置标记开始——让我们叫它们左标记和右标记——在列表的第一项和 最后一项。
    分区过程的目标是把相对于中值在错误的一边的数据放到正确的一边，同时找到分割 点。

    我们不断把左标记向右移动直到它指向了一个比中值更大的数字。我们 然后把右标记向左移动直到我们找到一个比中值更小的数字。
    在这个时候我们就找到了两个相对于最终的分割点在错误的位置的元素。在我们的例子中，就是93和20。现在我们可以交换这两个 元素，然后重复这个步骤了。

    在右标记变得比左标记小的时候，我们停止，此时右标记在的位置就是分割点在的位置。而 中值就可以和分割点的内容互换位置而被放置在正确的位置上了
    每个分割点左边的元素都比中值小，每个右边的都比它大了。这个列表就可以在分割 点被分成两半然后快速排序可以在这两个部分被分别调用了。


    注意一个长度为n的列表，如果每次分裂都发生在列表的中央，那么 将会重复logn次分裂。
    为了找到分割点，n个项目中的每一个都需要和中值进行对比。那么，综 合起来是nlogn。此外，快速排序不需要像在归并排序时所需的额外内存。
    在最坏的情况下，分割点可能不在中间，可以是非常偏左或偏右.用以上所述的递归过程，成了时间复 杂度为O(n^2)的排序。
    """
    pivotValue = alist[first]
    #pivotValue = median_three(alist,first,last)

    leftMark = first + 1
    rightMark = last
    done = False

    while not done:

        while   leftMark <= rightMark and alist[leftMark] <= pivotValue:
            leftMark += 1
        while rightMark >= leftMark and alist[rightMark] >= pivotValue:
            rightMark -= 1
        
        if  leftMark > rightMark:  # 交叉
            done = True
            
        else:
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]
        
    alist[rightMark], alist[first] = alist[first], alist[rightMark]
    return rightMark


def median_three(alist,first,last):
    """我们可以通过使用一种名为 “三点取样”的方法，来尝试着降低不均匀分割的可能性。
    为了选择中值，我们要考虑列表中第一 个、中间一个以及最后一个三个元素。
    在我们的例子中，它们分别是54,77和20。现在选取中间 值 作为 pivotValue"""
    values = [alist[first], alist[(first + last + 1)//2] ,alist[last]]
    values.sort()
    return values[1]



alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


from timeit import Timer

t1 = Timer("quickSort(alist)","from __main__ import quickSort; alist = [54,26,93,17,77,31,44,55,20]")
print("",t1.timeit(number=1000),"milliseconds") #median_three 0.005091133003588766

#0.009391350962687284

