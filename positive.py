num=int(input("Enter the number:"))
l1=list()

print("Enter the list elements:")
for i in range(num):
    x=int(input())
    l1.append(x)
l=[]
for m in l1:
    if(m>=0):
        l.append(m)
print(l)


        