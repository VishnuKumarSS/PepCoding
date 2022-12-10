n = int(input());
b = int(input());
def AnyToDec(n, base):
    reversed_n = str(n)[::-1]
    count=0
    answer = 0
    for i in reversed_n:
        answer += int(i) * base ** count
        count += 1
    return answer
if __name__ == "__main__":
  res = AnyToDec(n, b)
  print(res)


"""
1. You are given a number n.
2. You are given a base b. n is a number on base b.
3. You are required to convert the number n into its corresponding value in decimal number system.
Input Format
A number n
A base b
Output Format
A decimal number representing corresponding value of n in base b.

Constraints
0 <= d <= 1000000000
2 <= b <= 10
  
Sample Input
111001
2
Sample Output
57
"""