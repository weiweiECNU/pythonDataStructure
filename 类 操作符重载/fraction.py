class fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def show(self):
        print( self.top,"/",self.bottom)

    def __str__(self):
        return str(self.top)+"/"+str(self.bottom)

    def __add__(self, otherFraction):
        
        newTop = self.top * otherFraction.bottom + otherFraction.top * self.bottom

        newBottom = self.bottom * otherFraction.bottom

        common = gcd(newTop,newBottom)

        return fraction(newTop/common, newBottom/common)

    def __sub__(self, otherFraction):
        newTop = self.top * otherFraction.bottom - otherFraction.top * self.bottom

        newBottom = self.bottom * otherFraction.bottom

        common = gcd(newTop,newBottom)

        return fraction(newTop/common, newBottom/common)

    def mul(self,otherFraction):
        newTop = self.top * otherFraction.bottom * otherFraction.top * self.bottom

        newBottom = self.bottom * otherFraction.bottom

        common = gcd(newTop,newBottom)

        return fraction(newTop/common, newBottom/common)

    def __truediv__(self, otherFraction):
        newTop = self.top * otherFraction.bottom / otherFraction.top * self.bottom

        newBottom = self.bottom * otherFraction.bottom

        common = gcd(newTop,newBottom)

        return fraction(newTop/common, newBottom/common)
        

    def __eq__(self, other):
        """
        深相等
        """
        firstnum = self.top * other.bottom 
        secondnum = other.top * self.bottom 
        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.top * other.bottom 
        secondnum = other.top * self.bottom 
        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.top * other.bottom 
        secondnum = other.top * self.bottom 
        return firstnum > secondnum



def gcd(m,n): 
    while m%n != 0: 
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn 
    return n



