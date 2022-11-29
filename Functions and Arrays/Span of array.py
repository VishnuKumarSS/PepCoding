def getSpan(arr):
    minimum = arr[0]
    maximum = arr[0]
    for i in arr:
        if i<minimum:
            minimum = i
        if i>maximum:
            maximum = i
    answer = maximum - minimum
    return answer

if __name__ == '__main__':
    num = int(input())
    
    arr = [0] * num
    for i in range(0, num) :
        val = int(input())
        arr[i] = val
    
    solution = getSpan(arr)
    print(solution)


"""
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are required to find the span of input. Span is defined as difference of maximum value and minimum value.
Input Format
A number n
n1
n2
.. n number of elements
Output Format
A number representing max - min

Constraints
1 <= n <= 10^4
0 <= n1, n2
 .. n elements <= 10 ^9
Sample Input
6
15
30
40
4
11
9
Sample Output
36
"""