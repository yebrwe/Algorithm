class Stack():
    def __init__(self):
        self.arr = [0]*10000
        self.top = 0
        self.size = 0
    def empty(self):
        return 1 if self.size == 0 else 0
    def push(self, value):
        self.arr[self.top] = value
        self.top += 1
        self.size += 1
    def pop(self):
        if self.top == 0:
            return -1
        else:
            pop_value = self.arr[self.top-1]
            self.top -= 1
            self.size -= 1
            return pop_value
n=int(input())
stack=Stack()
commands_list = [input().split() for _ in range(n)]
for commands in commands_list:
    if len(commands) == 2:
        [_, x] = commands
        stack.push(x)
    else:
        [command] = commands
        if command == 'pop':
            print(stack.pop())
        if command == 'size':
            print(stack.size)
        if command == 'empty':
            print(stack.empty())
        if command == 'top':
            if stack.top == 0:
                print(-1)
            else:
                print(stack.arr[stack.top-1])
            

