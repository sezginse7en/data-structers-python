class MinHeap:
    def __init__(self,max_size) :
        self.max_size = max_size
        self.size = 0
        self.Heap = [0] * (self.max_size + 1)

    
    def getLeft(self,pos):
        return 2*pos

    def getRight(self,pos):
        return 2*pos + 1
    
    def getParent(self,pos):
        return pos // 2

    def isLeaf(self,pos):
        return pos*2 > self.size

    def swap(self,fpos,spos):
        self.Heap[fpos],self.Heap[spos] = self.Heap[spos],self.Heap[fpos]

    def minHeapify(self,pos):
        if self.isLeaf(pos):
            return
        
        if self.Heap[pos] > self.Heap[self.getLeft(pos)] or self.Heap[pos] > self.Heap[self.getRight(pos)]:
            if self.Heap[self.getLeft(pos)] < self.Heap[self.getRight(pos)]:
                self.swap(pos,self.getLeft(pos))
                self.minHeapify(self.getLeft(pos))
            else:
                self.swap(pos,self.getRight(pos))
                self.minHeapify(self.getRight(pos))
    
    def minHeap(self):

        for pos in range(self.size // 2 , 0, -1):
            self.minHeapify(pos)

    def insert(self,element):

        if self.size >= self.max_size:
            return

        self.size+=1
        self.Heap[self.size] = element
        current = self.size

        while self.Heap[self.getParent(current)] > self.Heap[current]:
            self.swap(current,self.getParent(current))
            current = self.getParent(current)

    def remove(self):
        popped = self.Heap[1]
        self.Heap[1] = self.Heap[self.size-1]
        self.Heap[self.size-1] = popped
        self.minHeapify(1)
        self.size -= 1
        return popped


    def print(self):
        for i in range(1,(self.size//2) + 1):
            print("Parent : ", self.Heap[i])
            print("Parent : ", self.Heap[self.getLeft(i)])
            print("Parent : ", self.Heap[self.getRight(i)])

print('The minHeap is ')
minHeap = MinHeap(15)
minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
minHeap.minHeap()

#minHeap.print()

minHeap.remove()

minHeap.print()