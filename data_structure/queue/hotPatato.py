###
#为了模拟这个环状结构，我们会用到队列(见图 3.5)。假设拿着土豆的孩子位于队首，当开始传递土豆时，
#模拟器会将那个孩子从队首移出队列然后立即让他从队尾进入队列。所有在他前面的 人都轮过一遍后才会再次轮到他传土豆。
#每经过“num”次出队入队的过程后，站在队首的孩子就会永 久离开队列，游戏将在新的圆圈中继续进行。
#这个过程会一直持续到只有一个名字剩下(即队列规 格为 1 时)。
###
from queue import Queue
def hotPatato(nameList, num):
    """我们的程序将要读入一个名字列表 和用作计数的常数“num”。在经过多次基于 num 的计数后，程序将返回最终剩下的人的姓名"""
    circle = Queue()
    for name in nameList:
        circle.enqueue(name)

    while circle.size() > 1:   
        for i in range(num):
            circle.enqueue( circle.dequeue() )
        
        circle.dequeue()

    return circle.queue

        
