n = int(input())
d = int(input())

def freq(n, d):
    str_n = str(n)
    str_d = str(d)
    count = 0
    for i in str_n:
        if i == str_d:
            count += 1
    return count

if __name__ == "__main__":
  print(freq(n, d))


# 1. You are given a number n.
# 2. You are given a digit d.
# 3. You are required to calculate the frequency of digit d in number n.
# Input Format
# A number n
# A digit d
# Output Format
# A number representing frequency of digit d in number n

# Constraints
# 0 <= n <= 10^9
# 0 <= d <= 9
  
# Sample Input
# 994543234
#  4
# Sample Output
# 3