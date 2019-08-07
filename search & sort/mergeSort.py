def mergeSort(alist):
    """归并排序是一种递归算法，它持续地将一个列表分成两半。
    如果列表是空的或者 只有一个元素，那么根据定义，它就被排序好了(最基本的情况)。
    如果列表里的元素超过一 个，我们就把列表拆分，然后分别对两个部分调用递归排序。
    一旦这两个部分被排序好了，那么 这种被叫做归并的最基本的操作，就被执行了。


    如果列表的长度小于或等于 一，那么我们已经有了一个排好序的列表并不需要做任何更多的过程了
    。如果不是，即列表长度 大于一，那么我们用Python的切片操作将左右两部分拆开



    归并是这样一个过程:把两个排序好了的列表结 合在一起组合成一个单一的，有序的新列表
    
    函数(11-31行)是用来把两个小的有序列表合成一个大的有序列表的。注意归并操作是 重复地把两个小的有序列表中的最小元素一一放回原列表的。

    第一步，列表被拆分，我们已经 (在二分查找中)计算过，我们能通过logn的数量级的计算将长度为n的列表拆分。
    而第二个过 程是合并。每个列表中的元素最终将被处理并被放置在排序好的列表中，所以合并操作对一个长 度为n的列表需要n的数量级的操作。
    因此分析结果就是，拆分需要logn数量级的操作而每次拆分 需要n数量级的操作因此最终操作的复杂度为nlogn。归并排序是一种O(nlogn) 的算法。
    

    拆分列表时归并排序函数需要额外的空间来存放被拆分出来的两个部 分。
    如果列表很大的话，这额外空间将是一个很重要的因素，可能使得这种排序被运用在大数据 集合时出现错误。
    
    """
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
