class vector:

    def __init__(self, vec):
        self.vec = vec

    def __add__(self, other):
        list=[]
        for i in range(len(self.vec)):
            list.append(self.vec[i] + other.vec[i])

        return list




v = vector([1, 2,4])
v2 = vector([2, 3, 4])
print(v+v2)