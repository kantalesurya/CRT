""""
counter = 0
while counter < 12:
    print("san")
    counter += 1
"""
# count the no of digits
'''
n = int(input())
counter = 0
while n > 0:
    counter += 1
    n //=  10
print(counter)
'''
#use for loop and print hellow 5 times using for loops
"""
counter = 0
for counter in range(0,5,1):
    print("hellow")
"""
# input: [1,2,3,4,5] output:[1,4,9,16,25]
"""
li = [1,2,3,4,5]
for i in range(len(li)):
    li[i] = li[i] ** 2
print(li)

for ele in li:
    if ele % 2 == 0:
        print(ele,end=" ")
"""
# vowels
"""
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count  += 1
print(count)
"""
"""
for i in range(1,11):
    if i == 5:
        continue
    print( i, end=" ")
"""
#password
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        print("Wrong password")
        attempts = attempts + 1

if attempts == 3:
    print("Account locked")
