x = 13
y = 5
print( x & y)
print( x | y)
print( x ^ y)
print( x << 2)
print( x >> 2)

# membership operator
print( "on" in "python")
print(100 in [10,20,30])

#Identity operators
x = 10
y = 20
z = 10
print(x is y)
print(x is z)

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)
print(id(l1),id(l2))