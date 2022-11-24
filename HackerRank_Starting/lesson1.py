#Create a 2d vector first, then a 3d vector inside it

class C2dvec:
    def __init__(self, i, j):
        self.i=i
        self.j=j

    def ee(self):
        print(f"{self.i}i + {self.j}j")


class C3dvec(C2dvec):
    def __init__(self, i, j, k):
        super().__init__(i,j) #No need to give again value to self when you can use the parent class constructor.
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


v2d=C2dvec(2,3)
v2d.ee()
v3d=C3dvec(4,5,6)
print(v3d)
print(v3d.__str__()) #Another way to print