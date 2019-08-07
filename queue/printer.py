from queue import Queue
import random

class Printer:
    """
    """
    def __init__(self, ppm):
        self.printRate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        """
        方法 tick 用于减去内设任务的完成所需时间，并在一次任务结束后将打印机设为闲置(11 行)。
        """
        if self.currentTask != None:
            self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            self.currentTask = None
    
    def isBusy(self):
        """实时监测是否正在执行打印任务。如果是，则表示打印机正忙"""
        return self.currentTask != None

    def startTask(self, task):
        """需要的等待时间可以由当前任务的打印张数求得。"""
        self.currentTask = task
        self.timeRemaining = task.getPages()*60 / self.printRate


class TaskQueue(Queue):
    pass

class Task:
    def __init__(self, time):
        self.timeStamp = time 
        self.pages = random.randint(1,20)
    
    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages
    
    def waitTime(self, currentTime):
        return currentTime - self.timeStamp
    

