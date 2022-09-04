class Node:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self,head=None):
        self.head = head

    def insert(self,value):

        newNode = Node(value)

        if self.head == None :
            self.head = newNode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = newNode

    def search(self,value)->Node:
        current = self.head
        while(current != None):
            if(value == current.value):
                return current
            current = current.next

    def count(self)->int:

        count = 0
        current = self.head

        while(current != None):
                count+=1
                current = current.next
        return count

    def delete(self,index)->bool:

        if self.count() < index:
            return 0

        if index == 1 :
            self.head = self.head.next
            return 1

        current = self.head
        for i in range(index-1):
            prev = current
            current = current.next
        
        prev.next = current.next

    def printList(self):
        current = self.head
        while(current != None):
            print(current.value, "->")
            current = current.next

    def isEmpty(self)->bool:
        return self.head == None

linkedList = LinkedList()
linkedList.insert(3)
linkedList.insert(2)
linkedList.insert(1)
linkedList.insert(5)

found = linkedList.search(5)
print(found.value)

linkedList.delete(3)

linkedList.printList()




