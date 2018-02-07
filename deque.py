class Deque:
    def __init__(self):
        self.elements = []

    def addFront(self,new_element):
        self.elements.append(new_element)

    def addEnd(self,new_element):
        self.elements.insert(0,new_element)

    def removeFront(self):
        return self.elements.pop()

    def removeEnd(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []

    def firstElement(self):
        return self.elements[0]

    def lastElement(self):
        return self.elements[-1]

    def viewElements(self):
        return self.elements

    def nthElement(self,n):
        return self.elements[n]

    def deleteElements(self):
        self.elements = []
        return self.elements
