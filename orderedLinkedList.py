class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def setValue(self,newValue):
        self.value = newValue

    def getValue(self):
        return self.value

    def setNext(self,nextValue):
        self.next = nextValue

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,newValue):
        temp = self.head
        previous = None
        stop = False
        while temp != None and not stop:
            if temp.getValue() > newValue:
                stop = True
            else:
                previous = self.head
                temp = previous.getNext()
        newN = Node(newValue)
        if previous == None:
            newN.setNext(self.head)
            self.head = newN
        else:
            newN.setNext(temp)
            previous.setNext(newN)


    def isEmpty(self):
        return self.head == None

    def size(self):
        temp = self.head
        total = 0
        while temp != None:
            total += 1
            temp = temp.getNext()
        return total

    def search(self,value):
        temp = self.head
        found = False
        stop = False
        while temp != None and not found and not stop:
            if temp.getValue() == value:
                found = True
            else:
                if temp.getValue > value:
                    stop = True
                else:
                    temp = temp.getNext()
        return found

    def remove(self,value):
        temp = self.head
        previous = None
        found = False
        while not found:
            if temp.getValue() == value:
                found = True
            else:
                previous = temp
                temp = temp.getNext()
        if previous == None:
            self.head = temp.getNext()
        else:
            previous.setNext(temp.getNext())
