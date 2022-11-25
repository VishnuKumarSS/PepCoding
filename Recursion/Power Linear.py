def powerLinear(x, n):
    if n <= 0:
        return 1
    return x * powerLinear(x, n-1)

num = int(input())
power = int(input())
print(powerLinear(num, power))


# 1. You are given a number x.
# 2. You are given another number n.
# 3. You are required to calculate x raised to the power n. Don't change the signature of power function .

# Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
# Input Format
# A number x
# A number n
# Output Format
# x raised to the power n

# Constraints
# 1 <= x <= 10
# 0 <= n <= 9
# Sample Input
# 2
# 5
# Sample Output
# 32