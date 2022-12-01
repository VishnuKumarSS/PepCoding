def reverse(arr, n):
    reversed_array = []
    for i in range(len(arr)-1, -1, -1):
        reversed_array.append(arr[i])
    return reversed_array
def main():
    n = int(input())
    arr = []
    for i in range(n) :
        val = int(input())
        arr.append(val)
    arr = reverse(arr, n)
    for i in range(n) :
        print(arr[i], end = " ")

main()

"""
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are required to reverse the contents of array a.
Input Format
Input is managed for you
Output Format
Output is managed for you

Constraints
0 <= n < 10^4
-10^9 <= a[i] <= 10^9
Sample Input
5
1
2
3
4
5
Sample Output
5 4 3 2 1
"""