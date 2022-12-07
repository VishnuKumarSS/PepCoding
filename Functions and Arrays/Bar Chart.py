# n = 5
# arr = [ 3,1,0,7,5 ]

def func(n, arr):
    for i in range(max(arr), 0, -1):
        for j in arr:
            if i - j <= 0:
                print('*	', end = "")
            else:
                print("	", end= "")
        print()
    
if __name__ == '__main__':
    n = int(input())
    # arr = list(map(int, input().strip().split()))[:n]
    arr = []
    for i in range(n):
        arr.append(int(input()))
    func(n, arr)


"""
Bar Chart
Easy  Prev   Next
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are required to print a bar chart representing value of arr a.
Input Format
A number n
n1
n2
.. n number of elements
Output Format
A bar chart of asteriks representing value of array a
Question Video

  COMMENTConstraints
1 <= n <= 30
0 <= n1, n2, .. n elements <= 10
Sample Input
5
3
1
0
7
5
Sample Output
			*		
			*		
			*	*	
			*	*	
*			*	*	
*			*	*	
*	*		*	*	
"""