class Stack:
    def __init__(self):
        self.elements = []

    def push(self,new_element):
        self.elements.append(new_element)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []

    def topElement(self):
        return self.elements[-1]

    def bottomElement(self):
        return self.elements[0]

    def viewElements(self):
        return self.elements

    def nthElement(self,n):
        return self.elements[n-1]

    def deleteElements(self):
        self.elements = []
        return self.elements

A = Stack()
A.push(1)
A.push(5)
A.push(0)
A.push(5)
A.push(8)
print(A.size())
print(A.bottomElement())
print(A.topElement())
print(A.isEmpty())
print(A.nthElement(3))
print(A.viewElements())
print(A.pop())
print(A.viewElements())