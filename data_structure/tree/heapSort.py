from binheap import BinHeap
def heapSort(alist):
    """堆排序 O(nlogn)"""
    heap = BinHeap(len(alist))
    heap.buildHeap(alist)
    sort = []

    for i in range( len(alist),0,-1):
        sort.append( heap.delMin())
    
    return sort
alist = [9,5,6,2,3]
print(heapSort(alist))

