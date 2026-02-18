'''
list - Built-in Data structure
use [] to create a list
list is mutable
list is heterogenous
list is indexed
list is ordered
 list allows duplicate values
'''
'''
li = [1,12.5,True,1,"Python",2+5j]
print(li,type(li))
print(len(li))
# update
li[2] = False
print(li)
# add element
li.append(100)
print(li)

li.insert(1,100)
print(li)

li.insert(20,200)
print(li)

li.insert(-20,300)
print(li)

li.extend([300,400,500])
print(li)

#removing element from list
li.pop()
print(li)

li.pop(1)
print(li)

li.pop(20)
print(li)

li.remove(100)
print(li)

li.clear()
print(li)

li = [1,2,3]
l2 = l1
l3 = l1.copy()

print(l1,l2,l3)

li.append(4)
print(li,l2,l3)
'''
from array import array
arr = array('i',[10,20,30])
print(arr,type(arr))

arr.append(12)
