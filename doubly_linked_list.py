class Node:
    def __init__(self,value=0,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def insertBegin(self,value):
        
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else :
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertLast(self,value):

        newNode = Node(value)
        if(self.tail == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insertMiddle(self,value):

        index = int(self.count()/2)

        newNode = Node(value)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
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

        while(current != None):
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

    def removeFromBegin(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return 1

        self.head = self.head.next
        self.head.prev = None

    def removeFromLast(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return 1

        self.tail = self.tail.prev
        self.tail.next = None


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


d_linked_list = DoubleLinkedList()
d_linked_list.insertLast(4)
d_linked_list.insertLast(3)
d_linked_list.insertLast(2)
d_linked_list.insertLast(1)

d_linked_list.insertMiddle(5)

d_linked_list.removeFromLast()

d_linked_list.printListFromBegin()



        