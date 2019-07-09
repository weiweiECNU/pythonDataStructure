#You have two jugs: a A-gallon jug and a B-gallon jug ( A > B ). 
# Neither of the jugs have markings on them. 
# There is a pump that can be used to fill the jugs with water. 
# How can you get exactly C gallons of water in the A-gallon jug? 
# Suppose the B <= C <= A and they are integer. 
import math

class Jar:
    def __init__(self, size, label):
        self.size = size
        self.volumn = 0
        self.label = label

    def fill( self ):
        print( self.label, "is filled")
        self.volumn = self.size
        self.display()
    
    def pour( self ):
        print( self.label, "is poured")
        self.volumn = 0
        self.display()

    def trans( self, toJar):
        if self.volumn + toJar.volumn >= toJar.size:
            self.volumn -= (toJar.size - toJar.volumn) 
            toJar.volumn = toJar.size
        else:
            toJar.volumn += self.volumn
            self.volumn = 0
        print( "Trans from", self.label, "to", toJar.label)
        self.display()
        toJar.display()
    
    def display(self):
        print("###############################")
        print( "The volumn of the jar: ", self.label, "has ", self.volumn)

        


def jarRC( jarLarge, jarSmall, want,):
    """ 递归解决水壶问题
    结束条件: want = gcd
    递进过程: want = want - gcd

    gcd 最大公约数
    通过不断的来回倒水，每次 large 里多出 最大公约数个体积水
    large 大瓶里的水体积
    small 小瓶里的水体积
    jarList [largesize smallsize] 大小瓶的体积
    want 希望得到的水的体积
    """
    gcd = math.gcd(jarLarge.size, jarSmall.size)
    if want % gcd != 0:
        print("Can not")
        return False

    else:
        if want == gcd:
            jarLarge.fill()
            jarLarge.trans( jarSmall )
            jarSmall.pour()

            jarLarge.display()
            jarSmall.display()
            return jarLarge,jarSmall
        else:
            jarLarge,jarSmall = jarRC(jarLarge, jarSmall, want - gcd)

            jarLarge.trans( jarSmall )
            jarLarge.fill()
            jarLarge.trans( jarSmall )
            jarSmall.pour()

            jarLarge.display()
            jarSmall.display()
            return jarLarge,jarSmall



jarLarge = Jar(4,"large")
jarSmall = Jar(2,"small")
jarRC(jarLarge,jarSmall,3)
