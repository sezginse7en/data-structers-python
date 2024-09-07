class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0] * (self.max_size + 1)
    
    def getLeft(self, pos):
        return 2 * pos

    def getRight(self, pos):
        return 2 * pos + 1
    
    def getParent(self, pos):
        return pos // 2

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if self.isLeaf(pos):
            return
        
        left = self.getLeft(pos)
        right = self.getRight(pos)

        # Check if children are within bounds and find the smallest child
        if left <= self.size and self.Heap[pos] > self.Heap[left]:
            smallest = left
        else:
            smallest = pos

        if right <= self.size and self.Heap[smallest] > self.Heap[right]:
            smallest = right

        # If the current node is not the smallest, swap and heapify
        if smallest != pos:
            self.swap(pos, smallest)
            self.minHeapify(smallest)

    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    def insert(self, element):
        if self.size >= self.max_size:
            return

        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        # Move the newly inserted element to its correct position
        while current > 1 and self.Heap[self.getParent(current)] > self.Heap[current]:
            self.swap(current, self.getParent(current))
            current = self.getParent(current)

    def remove(self):
        if self.size == 0:
            return None

        popped = self.Heap[1]  # Min element is at the root (1st index)
        self.Heap[1] = self.Heap[self.size]  # Move last element to root
        self.size -= 1
        self.minHeapify(1)
        return popped

    def print_heap(self):
        # Print the heap level by level
        for i in range(1, (self.size // 2) + 1):
            left = self.getLeft(i)
            right = self.getRight(i)

            print(f"Parent: {self.Heap[i]}")
            if left <= self.size:
                print(f" Left Child: {self.Heap[left]}")
            if right <= self.size:
                print(f" Right Child: {self.Heap[right]}")
            print()

# Example usage
print('The minHeap is:')
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

minHeap.print_heap()

print("Removed element:", minHeap.remove())

minHeap.print_heap()
