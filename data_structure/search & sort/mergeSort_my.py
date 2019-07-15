def mergeSort(alist, first, last):
    """递归实现
    
    停止条件， list 的长度为1 或0 : last = first
    递进：

    """

    if last > first:
        mid = ( last - first + 1) // 2

        mergeSort(alist, first, mid-1)
        mergeSort(alist, mid, last)

        leftMark = 0
        rightMark = 0
        listMark = 0

        blist = [0]*len(alist)

        while first + leftMark < mid and mid + rightMark < last:
            if alist[first + leftMark] < alist[mid + rightMark]:
                blist[listMark] = alist[first + leftMark]
                leftMark += 1
            else:
                blist[listMark] = alist[mid + rightMark]
                rightMark += 1

            listMark += 1
        
        while first + leftMark < mid: 
            blist[listMark] = alist[first + leftMark]
            leftMark += 1
            listMark += 1

        while mid + rightMark < last:
            blist[first+listMark] = alist[mid + rightMark]
            rightMark += 1
            listMark += 1
        
        alist[first:last] = blist[first:last]
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist,0,len(alist)-1)
print(alist)


            


    