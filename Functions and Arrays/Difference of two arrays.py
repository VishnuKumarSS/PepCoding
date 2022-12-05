n1 = int(input())
arr1 = []
for i in range(n1) :
    val = int(input())
    arr1.append(val)

n2 = int(input())
arr2 = []
for i in range(n2) :
    val = int(input())
    arr2.append(val)

num1 = ""
num2 = ""
for i in arr1:
    num1+= str(i)
for j in arr2:
    num2+= str(j)
ans = int(num2) - int(num1)
for i in str(ans):
    print(int(i))


# minn = min(len(arr1), len(arr2))
# maxx = max(len(arr1), len(arr2))
# answer = []

# for i in range(minn):
#     answer.append(arr1[i]+arr2[i])
# # print(answer)
# if len(arr1) == maxx:
#     ele = arr1
# else:
#     ele = arr2

# for i in range((maxx-minn)):
#     answer.insert(0, ele[-1-i])

# for i in answer:
#     print(i)


"""
1. You are given a number n1, representing the size of array a1.
2. You are given n1 numbers, representing elements of array a1.
3. You are given a number n2, representing the size of array a2.
4. You are given n2 numbers, representing elements of array a2.
5. The two arrays represent digits of two numbers.
6. You are required to find the difference of two numbers represented by two arrays and print the arrays. a2 - a1

Assumption - number represented by a2 is greater.
Input Format
A number n1
n1 number of elements line separated
A number n2
n2 number of elements line separated
Output Format
A number representing difference of two numbers (a2 - a1), represented by two arrays.

Constraints
1 <= n1, n2 <= 100
0 <= a1[i], a2[i] < 10
number reresented by a1 is smaller than number represented by a2
Sample Input
3
2
6
7
4
1
0
0
0
Sample Output
7
3
3
"""