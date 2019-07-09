import random
from printer import *

def isTask( taskRate):
    """平均每小时就有 20 个打印任务平均每 180 秒生成一个打印任务,
    每一秒钟我们可以生成 1-180 之间的随机数来模拟生成一个打印任务的可能性。如果生成的随机 数是 180，即认为生成了一个打印任务"""
    target = 3600 / taskRate
    return random.randint(1,target) == target
    

def simulation( numSeconds, ppm, taskRate = 20):
    """我们借助布尔数学体系的方法 决定是否生成新的打印任务。
    同时我们再 一次调用 random 模块中的 randrange 函数来得到一个 1 到 180 之间的随机整数(32 行)
    据此模拟这 个随机事件。模拟函数让我们可以为打印机设置总时长和单位时间打印张数"""

    printer = Printer(ppm)
    taskQueue = TaskQueue()
    waitingtimes = []
    taskRate = taskRate

    for second in range(numSeconds):
        if isTask(taskRate):
            task = Task(second)
            taskQueue.enqueue(task)
        if (not printer.isBusy()) and (not taskQueue.isEmpty() ):
            waitingtimes.append( task.waitTime(second) )
            printer.startTask( taskQueue.dequeue() )
        
        printer.tick()

    avgWatingTime = sum(waitingtimes)/ len(waitingtimes)
    remainTaskNum = taskQueue.size()

    print("Average Waiting time: ", "%.2f" %avgWatingTime, "secs", remainTaskNum, "tasks remains." )





