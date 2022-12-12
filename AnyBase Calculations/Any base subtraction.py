def AnyToDec(n, base):
    reversed_n = str(n)[::-1]
    count=0
    answer = 0
    for i in reversed_n:
        answer += int(i) * base ** count
        count += 1
    return answer

def DecToAny(n, base):
    remainders = ""
    while n>0:
        remainderr = n % base
        n = n//base
        remainders += str(remainderr)
    # print("KKKK", remainders)
    answer = int(remainders[::-1])
    return answer
    
def getDifference(b, n1, n2):
    num1 = AnyToDec(n1, b)
    num2 = AnyToDec(n2, b)
    num = num2 - num1
    ans = DecToAny(num, b)
    return ans


if __name__ == '__main__':
    base = int(input())
    n1 = int(input())
    n2 = int(input())
    
    solution = getDifference(base, n1, n2)
    print(solution)


"""
1. You are given a base b.
2. You are given two numbers n1 and n2 of base b.
3. You are required to subtract n1 from n2 and print the value.
Input Format
A base b
A number n1
A number n2
Output Format
A number of base b equal in value to n2 - n1.

Constraints
2 <= b <= 10
0 <= n1 <= 256
n1 <= n2 <= 256
Sample Input
8
1
100
Sample Output
77
"""
