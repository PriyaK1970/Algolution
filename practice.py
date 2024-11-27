"""#Algolution"""

#Count total negative numbers
def neg_count(l):
  count = 0
  for i in l:
    if i<0:
        count = count+1
  return count
l = []
n = int(input("Enter number of elements in array: "))
for i in range(n):
  elements = int(input("Enter elements: "))
  l.append(elements)
print(neg_count(l))

# max of all numbers
def max_num(l):
  max_num = l[0]
  for i in l:
    if i>max_num:
      max_num = i
  return max_num
l = []
n = int(input("Enter number of elements: "))
for i in range(n):
  elements = int(input("Enter elements: "))
  l.append(elements)
print(max_num(l))

# Merge two sorted arrays to third array
def merge(l1,l2):
  l3 = []
  i = 0
  j = 0
  while i<len(l2) and j<len(l1):
    if l1[j]<l2[i]:
      l3.append(l1[j])
      j = j+1
    else:
      l3.append(l2[i])
      i = i+1
  return l3
l1 = list(map(int, input("Enter a sorted list of elements separated by spaces: ").split()))
l2 = list(map(int, input("Enter a sorted list of elements separated by spaces: ").split()))
o = []
o = merge(l1,l2)
for i in o:
  print(i)

# 7 integers as input and reverse the order of numbers in array
def reverse(l):
  l.reverse()
  return l
l = []
for i in range(7):
  elements = int(input("Enter elements: "))
  l.append(elements)
l.reverse()
for i in l:
  print(i)

# 5 integers as input and find if order of number is palindrome
def find_order_of_palindrome(l):
  y = l.copy()
  y.reverse()
  if l == y:
    return True
  else:
    return False
l = []
for i in range(4):
  elements = int(input("Enter elements: "))
  l.append(elements)
if find_order_of_palindrome(l):
  print("True")
else:
  print("False")

# search a number in an array and print the index of input
def search(l,m):
  for i in range(len(l)):
    if l[i] == m:
      return i
  return -1
l = []
n = int(input("Enter number in array: "))
for i in range(n):
  elements = int(input("Enter elements: "))
  l.append(elements)
m = int(input("Enter number to search: "))
print(search(l,m))

# print unique numbers in array
def unique(l):
  for i in l:
    if l.count(i) == 1:
      print(i)
l = []
n = int(input("Enter numbers in array: "))
for i in range(n):
  elements = int(input("Enter elements: "))
  l.append(elements)
unique(l)

# count frequency of each number in array
def count_frequency(l):
  f = {}
  for i in l:
    if i in f:
      f[i] = f[i]+1
    else:
      f[i] = 1
  return f
l = []
n = int(input("Enter numbers in array: "))
for i in range(n):
  elements = int(input("Enter elements: "))
  l.append(elements)
print(count_frequency(l))

1# count total duplicate numbers
def total_duplicate(l):
  count = 0
  for i in l:
    if l.count(i)>1:
      count = count+1
  return count
l = []
n = int(input("Enter numbers in array: "))
for i in range(n):
  elements = int(input("Enter elements: "))
  l.append(elements)
print(total_duplicate(l))

# number of rows and column should be input to print parallelogram function
def print_parallelogram(r):
  for i in range(r,0,-1): #3
    for j in range(i-1):
      print(" ",end="")
    for k in range(r):
      print("*",end="")
    print()

r = int(input("Enter number of rows: "))
print_parallelogram(r)
'''
  ***
 ***
***
'''

# print right triange
def print_right_triangle(n):
  for i in range(n):
    for j in range(i+1):
      print("*",end=" ")
    print()
n = int(input("Enter number of rows: "))
print_right_triangle(n)

# print half diamond
def print_half_diamond(n):
  for i in range(1,n+1):
    print("*" *i)
  for j in range(n-1,0,-1):
    print("*" *j)
n = int(input("Enter number of columns: "))
print_half_diamond(n)



# pattern to be printed
12345
54321
12345
54321
12345
def pattern(n):
  for i in range(n):
    for j in range(1,n+1):
      print(j,end="")
    print()
  for i in range(n):
    for j in range(n,0,-1):
      print(j,end="")
    print()
n = int(input("Enter number of rows: "))
pattern(n)
