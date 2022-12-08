# binary search
n= int(input())

arr= []

for i in range(0, n):
    ele= int(input())
    arr.append(ele)
data= int(input())

low = 0
high = len(arr)-1

first = None
last = None
while low <= high:
    mid = (low+high)//2
    if arr[mid] < data:
        low = mid + 1
    elif arr[mid] > data:
        high = mid -1
    elif arr[mid] == data:
        first = mid
        high = mid -1

low = 0
high = len(arr)-1
while low <= high:
    mid = (low+high)//2
    if arr[mid] < data:
        low = mid + 1
    elif arr[mid] > data:
        high = mid -1
    elif arr[mid] == data:
        last = mid
        low = mid + 1
print(f"{first} {last}")
    
# without binary search (i.e) linear search

# first = None
# last = None
# count = 0
# for i in range(len(arr)):
#     if arr[i] == data and count == 0:
#         first = i
#         last = i
#         count += 1
#     elif arr[i] == data:
#         last = i
# print(first)
# print(last)






"""
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.

Asssumption - Array is sorted. Array may have duplicate values.
Input Format
A number n
n1
n2
.. n number of elements
A number d
Output Format
A number representing first index
A number representing last index

Constraints
1 <= n <= 1000
1 <= n1, n2, .. n elements <= 100
1 <= d <= 100
Sample Input
15
1
5
10
15
22
33
33
33
33
33
40
42
55
66
77
33
Sample Output
5
9

"""