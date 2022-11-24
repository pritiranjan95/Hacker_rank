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
        def __len__(self):
            l= len(self.vec)
            n = len(vec1.vec)
            if l==n:
                newlist = []
                for i in range(len(self.vec)):
                    newlist.append(self.vec[i] + vec1.vec[i])
                return vector(newlist)
            else:
                return "Error"



    def __mul__(self, vec2):
        multi=0
        for i in range(len(self.vec)):
            multi += self.vec[i]* vec2.vec[i]
        return multi

    def __len__(self):
        return len(self.vec)

    def __len__(self):
        return len(self.vec)

v=vector([2,4,5])
v2 = vector([3,4,6])
# print(v)
print(len(v))
print(len(v2))
print(v+v2)
print(v*v2)

