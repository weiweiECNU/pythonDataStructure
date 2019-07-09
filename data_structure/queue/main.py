from queue import Queue
from hotPatato import hotPatato
import printer_simulator

q = Queue()

print(q.isEmpty())

q.enqueue(4)

q.enqueue("dog")

q.enqueue(True)

print(q.size())

print(q.isEmpty())

q.enqueue(8.4)

q.dequeue()

q.dequeue()

print(q.size())


nameList = ["Bill","David","Susan","Jane","Keat","Brad"]
print( hotPatato(nameList,7 ) )

for i in range(10): 
    printer_simulator.simulation(3600,15,40)
