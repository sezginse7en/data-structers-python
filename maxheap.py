class MaxHeap:
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

    def maxHeapify(self, pos):
        if self.isLeaf(pos):
            return
        
        left = self.getLeft(pos)
        right = self.getRight(pos)

        # Check if children are within bounds and find the largest child
        if left <= self.size and self.Heap[pos] < self.Heap[left]:
            largest = left
        else:
            largest = pos

        if right <= self.size and self.Heap[largest] < self.Heap[right]:
            largest = right

        # If the current node is not the largest, swap and heapify
        if largest != pos:
            self.swap(pos, largest)
            self.maxHeapify(largest)

    def maxHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.maxHeapify(pos)

    def insert(self, element):
        if self.size >= self.max_size:
            return

        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        # Move the newly inserted element to its correct position
        while current > 1 and self.Heap[self.getParent(current)] < self.Heap[current]:
            self.swap(current, self.getParent(current))
            current = self.getParent(current)

    def remove(self):
        if self.size == 0:
            return None

        popped = self.Heap[1]  # Max element is at the root (1st index)
        self.Heap[1] = self.Heap[self.size]  # Move last element to root
        self.size -= 1
        self.maxHeapify(1)
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
print('The maxHeap is:')
maxHeap = MaxHeap(15)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)
maxHeap.maxHeap()

maxHeap.print_heap()

print("Removed element:", maxHeap.remove())

maxHeap.print_heap()
