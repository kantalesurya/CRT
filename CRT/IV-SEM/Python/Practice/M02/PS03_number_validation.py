"""""
write a python code to check whether a number is armstrong or not
"""
"""
n = int(input("Enter number: "))
print("Armstrong" if n == sum(int(d)**len(str(n)) for d in str(n)) else "Not Armstrong")

"""
""""
prime or not 
"""
"""
n = int(input("Enter number: "))
print("Prime" if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)) else "Not Prime")
"""
"""
monotonic or not?
"""
"""
def is_monotonic(a):
    return a == sorted(a) or a == sorted(a, reverse=True)

nums = list(map(int, input().split()))
print("Monotonic" if is_monotonic(nums) else "Not monotonic")
"""
"""
num = int(input("Enter a number: "))

rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)
"""
"""""
def roman_to_int(s):
    r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i in range(len(s)-1):
        total += -r[s[i]] if r[s[i]] < r[s[i+1]] else r[s[i]]
    return total + r[s[-1]]

print(roman_to_int(input().upper()))
"""
"""
star print pattern

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
    """
"""
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
    """
"""
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
    """
""""

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    """
"""
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
    """
""""
n = int(input("Enter number : "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
    """
"""
li = [1, 2, 3, 4, 5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)
"""
"""
li1 = ['a', 'b', 'c']
result = "".join(li1)
print(result)
"""
"""
n = int(input())
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
   """ """
palindrome pattern:
"""
'''
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)) + " " + " ".join(str(x) for x in range(i - 1, 0, -1)))
    
'''