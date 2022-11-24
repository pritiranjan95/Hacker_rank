class Stack:
    def __init__(self):
        self.lists=[]

    def add(self, a, b):
        print(f"{a+b}")

    def push(self,item):
        self.lists.append(item)

    def __str__(self):
        return str(self.lists)

if __name__=="__main__":

    s=Stack()
    s.add(2,5)
    s.push(6)
    s.push(5)
    print(s)


