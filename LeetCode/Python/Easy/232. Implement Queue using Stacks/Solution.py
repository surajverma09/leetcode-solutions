class MyQueue:

    def __init__(self):
        self.first = []
        self.sec = []

    def push(self, data: int) -> None:
        self.first.append(data)

    def pop(self) -> int:
        if len(self.sec)>0:
            return self.sec.pop()
        elif len(self.first)>0:
            while self.first:
                self.sec.append(self.first.pop())
            return self.sec.pop()
        else:
            return None


    def peek(self) -> int:
        if len(self.sec)>0:
            return self.sec[-1]
        elif len(self.first)>0:
            while self.first:
                self.sec.append(self.first.pop())
            return self.sec[-1]
        else:
            return None
        

    def empty(self) -> bool:
        return len(self.first)==0 and len(self.sec)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()