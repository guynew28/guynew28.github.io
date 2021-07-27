# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]
l_2=[]
def sortednum():
    l_1.sort()
    return l_1

print(sortednum())

l_2=l_1[:4]
print(l_2)

print("================================")

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3=[]
newlist=[]

def mergednum():
    l_3=l_1+l_2
    l_3.sort()
    return l_3

x=mergednum()
print(x)

print("===================")

# If any duplicates need to be removed

for i in x:
    if i not in newlist:
        newlist.append(i)
print(newlist)
