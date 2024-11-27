# Subarray with largest sum
def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = list(map(int, input("Enter the integer array: ").split()))
result = max_subarray_sum(nums)
print("The maximum subarray sum is:", result)

# Count inversions of given array
def merge_and_count_inversions(arr, left, mid, right):
    inv_count = 0

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            inv_count += (len(left_arr) - i)
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return inv_count

def merge_sort(arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, left, mid)
        inv_count += merge_sort(arr, mid + 1, right)

        inv_count += merge_and_count_inversions(arr, left, mid, right)

    return inv_count

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
result = merge_sort(arr, 0, len(arr) - 1)
print(result)

# kth largest element in the array
import heapq

def find_kth_largest(nums, k):
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

    return min_heap[0]

nums = list(map(int, input("Enter the numbers in the array separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

result = find_kth_largest(nums, k)
print("The", k, "th largest element in the array is:", result)

# a phase palindrome
def is_palindrome(s):
    def process_string(s):
        alphanumeric_chars = [char.lower() for char in s if char.isalnum()]
        return "".join(alphanumeric_chars)

    processed_s = process_string(s)

    return processed_s == processed_s[::-1]

s = input("Enter a string to check if it is a palindrome: ")

result = is_palindrome(s)
if result:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")

# Equilibrium point
def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]

        if left_sum == total_sum:
            return i + 1

        left_sum += arr[i]

    return -1

arr = input("Enter the array elements separated by spaces: ")
arr = list(map(int, arr.split()))

equilibrium_index = find_equilibrium_index(arr)

if equilibrium_index != -1:
    print("Equilibrium index is:", equilibrium_index)
else:
    print("No equilibrium index found in the array.")

# Naive Approach:
def find_pair_naive(arr, N, X):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == X:
                return "Yes"
    return "No"

N = int(input("Enter the size of the array: "))
A = list(map(int, input("Enter the elements of the array (sorted): ").split()))
X = int(input("Enter the target sum: "))

result_naive = find_pair_naive(A, N, X)
print("Using Naive Approach - Output:", result_naive)

# Two Pointer Technique
def find_pair_two_pointer(arr, N, X):
    left = 0
    right = N - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == X:
            return "Yes"
        elif current_sum < X:
            left += 1
        else:
            right -= 1

    return "No"

N = int(input("Enter the size of the array: "))
A = list(map(int, input("Enter the elements of the array (sorted): ").split()))
X = int(input("Enter the target sum: "))

result_two_pointer = find_pair_two_pointer(A, N, X)
print("Using Two Pointer Technique - Output:", result_two_pointer)

# maximum sum of k
def max_sum_subarray(arr, n, k):
    if k > n:
        return "Invalid"

    max_sum = 0
    window_sum = sum(arr[:k])

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the value of 'k': "))

n = len(arr)
result = max_sum_subarray(arr, n, k)
print("Output:", result)

# price of stock
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print("Output:", result)

# Hashmap
def max_length_subarray(nums, target):
    max_length = 0
    sum_index_map = {}
    current_sum = 0
    result_subarray = []

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum == target:
            max_length = i + 1
            result_subarray = nums[:i+1]

        if current_sum not in sum_index_map:
            sum_index_map[current_sum] = i

        if current_sum - target in sum_index_map:
            if i - sum_index_map[current_sum - target] > max_length:
                max_length = i - sum_index_map[current_sum - target]
                result_subarray = nums[sum_index_map[current_sum - target] + 1:i+1]

    if result_subarray:
        return result_subarray
    else:
        return "No subarray found with the given sum"

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8
result = max_length_subarray(nums, target)
print("Output:", result)

def heapify(arr, n, i, heap_type):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if heap_type == 'min':
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
    elif heap_type == 'max':
        if left < n and arr[left] < arr[largest]:
            largest = left
        if right < n and arr[right] < arr[largest]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, heap_type)

def heap_sort(arr, heap_type):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, heap_type)
    return arr

A = list(map(int, input("Enter the elements of the array: ").split()))
Max_heap = heap_sort(A.copy(),'max')
Min_heap = heap_sort(A.copy(),'min')
print("Max heap: ",Max_heap)
print("Min heap: ",Min_heap)

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
def max_contagious_subarray(A,k):

A = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the value of 'k': "))
print(max_contagious_subarray(A,k))
