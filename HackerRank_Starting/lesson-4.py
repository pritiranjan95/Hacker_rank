class vector:
    def __init__(self, vec):
        self.vec=vec

    def __str__(self):
       return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

    def __add__(self, vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return vector(newlist)


v=vector([7, 8, 20])
v2=vector([2,3,5])
print(v)
print(v+v2)