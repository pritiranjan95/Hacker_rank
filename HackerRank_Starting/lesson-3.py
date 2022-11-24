class vector:
    def __init__(self, vec):
        self.vec=vec

    def __str__(self):
        str1=" "
        index=0
        for i in self.vec:
            str1 += f" {i}a{index} + "
            index=index+1
        return str1 [:-1]

    def __add__(self, vec1):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec1.vec[i])
        return vector(newlist)

    def __mul__(self, vec2):
        sum=0
        for i in range(len(self.vec)):
            sum += self.vec[i]* vec2.vec[i]
        return sum




v=vector([2,4,5])
v2 = vector([3,4,6])
print(v)
print(v+v2)
print(v*v2)
