class LogisticGate:
    def __init__( self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic() 
        return self.output

class BinaryGate(LogisticGate):
    def __init__( self, label):
        LogisticGate.__init__(self,label) 
        #super(BinaryGate,self).__init__(label)
        self.pinA = None 
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
    

    
class UnaryGate(LogisticGate):
    def __init__( self, label):
        self.pin = None
    
    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))


class andGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self,label)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class orGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self,label)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1

class notGate(UnaryGate):     
    def __init__(self, label):
        BinaryGate.__init__(self,label)
    
    def performGateLogic(self):
        a = self.getPin()
        return abs(a-1)
