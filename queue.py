class Queue:
    
    def __init__(self,queue_array = []):
        self.queue_array = queue_array

    def enqueue(self,value):
        self.queue_array.append(value)

    def dequeue(self):
        if self.isEmpty() :
            return "Queue is empty"
        return self.queue_array.pop(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue_array)

# 1 2 3 4#
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

for s in range(queue.size()):
    print(queue.dequeue())