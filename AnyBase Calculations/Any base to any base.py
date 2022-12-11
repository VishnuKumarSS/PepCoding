n = int(input())
d1 = int(input())
d2 = int(input())
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

    answer = int(remainders[::-1])
    return answer

def AnyToAny(n, d1, d2):
    decimal = AnyToDec(n, d1)
    answer = DecToAny(decimal, d2)
    return answer
if __name__ == "__main__":
    res = AnyToAny(n, d1, d2)
    print(res)


"""
1. You are given a number n.
2. You are given a base b1. n is a number on base b.
3. You are given another base b2.
4. You are required to convert the number n of base b1 to a number in base b2.
Input Format
A number n
A base b1
A base b2
Output Format
A number of base b2 equal in value to n of base b1.

Constraints
0 <= n <= 512
2 <= b1 <= 10
2 <= b2 <= 10
Sample Input
111001
2
3
Sample Output
2010
"""