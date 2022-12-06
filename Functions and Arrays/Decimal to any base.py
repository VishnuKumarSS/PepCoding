n = int(input());
b = int(input());
def DecToAny(n, base):
    remainders = ""
    while n>0:
        remainderr = n % base
        n = n//base
        remainders += str(remainderr)

    answer = int(remainders[::-1])
    return answer
if __name__ == "__main__":
  res = DecToAny(n, b)
  print(res)


"""
1. You are given a decimal number n.
2. You are given a base b.
3. You are required to convert the number n into its corresponding value in base b.
Input Format
A number n
A base b
Output Format
A number representing corresponding value of n in number system of base b

Constraints
0 <= d <= 512
2 <= b <= 10
  
Sample Input
57
 2
Sample Output
111001
"""