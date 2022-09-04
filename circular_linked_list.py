class Node:
    def __init__(self,value=0,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class CircularLinkedList:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def insert(self,value):

        index = int(self.count()/2)

        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif self.head.next == None:
            self.head.next = newNode
            newNode.prev = self.head
            self.tail = newNode
            self.tail.next = self.head
        else:
            current = self.head
            for i in range(index):
                previous = current
                current = current.next

            previous.next = newNode
            newNode.prev = previous
            newNode.next = current

    def count(self)->int:
        count = 0
        current = self.head

        while(current != self.tail):
                count+=1
                current = current.next
        return count

    def removeFromMiddle(self,value):

        if self.head.value == value:
            self.head = self.head.next

        current = self.head
        while(current != None and current.value != value):
            previous = current
            current = current.next
        
        previous.next = current.next
        current.next.prev = previous

    def printListFromBegin(self):
        current = self.head
        print("Begin to Last")
        while(current != None):
            print(current.value, "->")
            current = current.next

    def printListFromLast(self):
        current = self.tail
        print("Last to Begin")
        while(current != None):
            print(current.value, "->")
            current = current.prev


c_linked_list = CircularLinkedList()
c_linked_list.insert(4)
c_linked_list.insert(3)
c_linked_list.insert(2)
c_linked_list.insert(1)
c_linked_list.insert(5)

c_linked_list.printListFromBegin()



        