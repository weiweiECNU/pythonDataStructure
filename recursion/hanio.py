from stack import Stack


def movePlate(fromBar, toBar):
    """打印转移盘子的字符串，打印转以后各个 Bar 上的盘子"""
    #print("moving disk from",fromBar,"to",toBar)
    toBar.push(fromBar.pop())

def hanoi(height, fromBar, toBar, withBar):
    """hanoi 问题
    基本结束条件 : 只有一个圆盘
    向基本结束条件演进: 
    1把圆盘数减一层数的小塔经过目标杆移动到中间杆
    2、把剩下的圆盘移动到目标杆  
    3、把圆盘数减一层数的小塔从中间杆，经过起始杆移动到目标杆"""

    if height >= 1:
        hanoi( height - 1, fromBar, withBar, toBar)

        movePlate(fromBar, toBar)
        printBars(fromBar, toBar, withBar)

        hanoi( height - 1, withBar, toBar, fromBar)

def printBars(fromBar, withBar, toBar):
    print("##########################")
    print("FromBar: ", fromBar)
    print("WithBar: ", withBar)
    print("Tobar: ", toBar)
    

height = 5
fromBar = Stack()
toBar = Stack()
withBar = Stack()

for plate in range(height,0,-1):
    fromBar.push(plate)
printBars(fromBar, withBar, toBar)

hanoi(height, fromBar, toBar, withBar)


    





