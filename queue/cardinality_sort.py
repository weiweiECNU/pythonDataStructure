# 实现基数排序。十进制的基数排序是一个使用了“箱的集合”(包括一个主箱和 10 个数字 箱)的机械分选技术。
# 每个箱像队列(Queue)一样，根据数据项的到达顺序排好并保持它们的值。 
# 算法开始时，将每一个待排序数值放入主箱中。然后对每一个数值进行逐位的分析。
# 每个从主箱最 前端取出的数值，将根据其相应位上的数字放在对应的数字箱中。
# 比如，考虑个位数字，534 被放置 在数字箱 4，667 被放置在数字箱 7。
# 一旦所有的数值都被放置在相应的数字箱中，所有数值都按照 从箱 0 到箱 9 的顺序，依次被取出，重新排入主箱中。
# 该过程继续考虑十位数字，百位数字，等等。当最后一位被处理完后，主箱中就包含了排好序的数值。

from queue import Queue
box_main = Queue()
box_zero = Queue()
box_one = Queue()
box_two = Queue()
box_three = Queue()
box_four = Queue()
box_five = Queue()
box_six = Queue()
box_seven = Queue()
box_eight = Queue()
box_nine = Queue()
numbers = [100,451,749,548,553,146,837,27,547,856,428,294,1697,5390,36879,78,9]
boxs = [box_zero, box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine]

def init():
    for number in numbers:
        box_main.enqueue(number)

def distribution( digit ):
    for i in range(box_main.size()):
        num_not_sort = box_main.dequeue()
        boxs[ num_not_sort % (10 ** (digit+1)) // (10 ** digit) ].enqueue(num_not_sort)

def merge():
    for box in boxs:
        for i in range( box.size() ):
            box_main.enqueue(box.dequeue())

def get_digit(num):
    count = 0
    while num>0 :
        num = num // 10 #实现位与位之间的遍历
        count += 1
    return count

def get_largest_digit(numberList):
    largest_digit = 0
    for number in numberList:
        digit = get_digit(number)
        if digit > largest_digit:
            largest_digit = digit
    
    return largest_digit




# for i in range(box_main.size()):
#     num_not_sort = box_main.dequeue()
#     boxs[ num_not_sort % 10 ].enqueue(num_not_sort)

# for box in boxs:
#     for i in range( box.size() ):
#         box_main.enqueue(box.dequeue())

# for i in range(box_main.size()):
#     num_not_sort = box_main.dequeue()
#     boxs[ num_not_sort % 100 // 10 ].enqueue(num_not_sort)

# for box in boxs:
#     for i in range( box.size() ):
#         box_main.enqueue(box.dequeue())

# for i in range(box_main.size()):
#     num_not_sort = box_main.dequeue()
#     boxs[ num_not_sort % 1000 // 100 ].enqueue(num_not_sort)

# for box in boxs:
#     for i in range( box.size() ):
#         box_main.enqueue(box.dequeue())

# for i in range(box_main.size()):
#     num_not_sort = box_main.dequeue()
#     boxs[ num_not_sort % 10000 // 1000 ].enqueue(num_not_sort)

# for box in boxs:
#     for i in range( box.size() ):
#         box_main.enqueue(box.dequeue())

# for i in range(box_main.size()):
#     num_not_sort = box_main.dequeue()
#     boxs[ num_not_sort % 100000 // 10000 ].enqueue(num_not_sort)

# for box in boxs:
#     for i in range( box.size() ):
#         box_main.enqueue(box.dequeue())




def cardinality_sort( numberList ):

    largest_digit = get_largest_digit( numberList )
    init()
    for digit in range(largest_digit+1):
        distribution(digit) 
        merge()
    
    print(box_main)

cardinality_sort(numbers)





