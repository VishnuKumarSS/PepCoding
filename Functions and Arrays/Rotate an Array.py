def func(arr, k):   
    if k<0:
        k = abs(3)
        for i in range(k):
            ele = arr.pop(0)
            arr.append(ele)
            
    else:
        for i in range(k):
            ele = arr.pop()
            arr.insert(0, ele)
    # print(arr)
    return arr

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    k = int(input())
    ans = func(arr, k)
    for i in range(len(ans)):
        print(ans[i], end=" ")


"""
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are given a number k.
4. Rotate the array a, k times to the right (for positive values of k), and to
the left for negative values of k.
Input Format
Input is managed for you
Output Format
Output is managed for you

Constraints
0 <= n < 10^4
-10^9 <= a[i], k <= 10^9
Sample Input
5
1
2
3
4
5
3
Sample Output
3 4 5 1 2
"""