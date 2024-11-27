#Cyclic palindrome
def head_shift(s):
  return s[1:] + s[0]

def tail_shift(s):
  return s[-1] + s[:-1]

def is_palindrome(s):
  return s == s[::-1]

def is_cyclic_palindrome(s):
  if is_palindrome(s):
    return 0
  n = len(s)
  min_shifts = float('inf')
  for i in range(n):
    head = s[i:] + s[:i]
    if is_palindrome(head):
      min_shifts = min(min_shifts, i)
      break
    tail = s[-i:] + s[:-i]
    if is_palindrome(tail):
      min_shifts = min(min_shifts, i)
      break
  if min_shifts == float('inf'):
    return -1
  else:
    return min_shifts
n = int(input("Enter the number of strings: "))
for i in range(n):
  s = input("Enter a string: ")
  print(is_cyclic_palindrome(s))

# square_free_number
def square_free_number(n):
   def is_square_free(num):
    for i in range(2, int(num**0.5)+1):
      if num % (i*i) == 0:
        return False
    return True
   count = 0
   l = []
   for i in range(2,n+1):
    if n % i == 0 and is_square_free(i):
      l.append(i)
      count = count+1
   return count,l
n = int(input("Enter a number: "))
print(square_free_number(n))

# contiguous subarray
def maxContagiousSubarray(A,k):
  n = len(A)
  result = []
  for i in range(0, n-k+1):
    maxValue = max(A[i:i+k])
    result.append(maxValue)
  return result
A = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the value of 'k': "))
o = maxContagiousSubarray(A,k)
print("Output:", o)

# OR of subarrays
def orOfSubarrays(A):
  n = len(A)
  subarraysOr = []
  for i in range(n):
    orValue = 0
    for j in range(i, n):
      orValue |= A[j]
      subarraysOr.append(orValue)
  finalOr = 0
  for orVal in subarraysOr:
    finalOr |= orVal
  return finalOr

A = list(map(int, input("Enter the elements of the array: ").split()))
output = orOfSubarrays(A)
print(output)

def checkValidString(s):
  leftMin = leftMax = 0
  for char in s:
    if char == '(':
      leftMin += 1
      leftMax += 1
    elif char == ')':
      leftMin -= 1
      leftMax -= 1
    else:
      leftMin -= 1
      leftMax += 1
    if leftMax < 0:
      return False
    leftMin = max(leftMin,0)
  return leftMin == 0
s = input("Enter the elements: ")
output = checkValidString(s)
print(output)

def is_valid(s):
  bracket_map = {'(':')','[':']','{':'}'}
  stack = []
  for char in s:
    if char in bracket_map :
      stack.append(char)
    elif char in bracket_map.values():
      top_element = stack.pop() if stack else '#'
      if bracket_map[top_element] != char:
        return False
    else:
        stack.append(char)
  return not stack
s = input("Enter string: ")
result = is_valid(s)
print(result)

def number_to_text(n):
  text = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred"}
  if n<=20:
    return text[n]
  elif n<100:
    tens = n//10 * 10
    ones = n%10
    return text[tens] + (''if ones == 0 else''+ text[ones])
  else:
    return text[100]

def count_vowels(text):
  vowels = set('aeiou')
  return sum(1 for char in text if char in vowels)

def count_pairs(numbers,target):
  count = 0
  seen = {}
  for number in numbers:
    complement = target - number
    if complement in seen:
      count += seen[complement]
    seen[number] = seen.get(number, 0) + 1
  return count
n = int(input("Enter number of elements: "))
number = list(map(int, input("Enter the elements: ").split()))
totalVowels = sum(count_vowels(number_to_text(num))for num in number)
d = totalVowels
pairs_count = count_pairs(numbers,d)
if pairs_count>100:
  print("Greater than 100")
else:
  print(number_to_text(pairs_count))
