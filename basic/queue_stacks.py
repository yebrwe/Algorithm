#queue stacks

class Queue2Stacks():
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enqueue(self, item):
        self.instack.append(item)
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
queue = Queue2Stacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())