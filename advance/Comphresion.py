a=[4,3,5,6,8,7,6,2]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
#
# print(b)

#This is a way to print all the even no.
#anther way in shortcut

b = [i for i in a if i%2==0]
print(b)