class Queue:
    def __init__(self):
        self.elements = []

    def enque(self,new_element):
        self.elements.insert(0,new_element)

    def deque(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []

    def firstElement(self):
        return self.elements[-1]

    def lastElement(self):
        return self.elements[0]

    def viewElements(self):
        return self.elements

    def nthElement(self,n):
        return self.elements[-n]

    def deleteElements(self):
        self.elements = []
        return self.elements

A = Queue()
A.enque(1)
A.enque(5)
A.enque(0)
A.enque(5)
A.enque(8)
print(A.size())
print(A.firstElement())
print(A.lastElement())
print(A.isEmpty())
print(A.nthElement(3))
print(A.viewElements())
print(A.deque())
print(A.viewElements())