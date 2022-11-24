n=input().split()
arr = list(map(int, input().split( )))
print(arr)

a=max(arr)
print(a)

c=arr.count(a)
print(c)

for i in range(c):
    arr.remove(a)

print(arr)

b=max(arr)
print(f"runner up score is {b}")
