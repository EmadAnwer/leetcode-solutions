#!env/bin/user python3
# https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/N

# N. Sum of a Matrix
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Given two matrices A and B of size R * C. Print the summation of A and B.

# Note: Solve this problem using recursion.

# Input
# First line contains two numbers R and C (1 ≤ R, C ≤ 100). number of rows and number of columns respectively.

# Next R lines will contain C numbers ( - 100 ≤ Ai, j ≤ 100) matrix A numbers.

# Next R lines will contain C numbers ( - 100 ≤ Bi, j ≤ 100) matrix B numbers.

# Output
# Print the summation result.

# Example
# inputCopy
# 2 3
# 1 2 3
# 4 5 6
# 1 3 5
# 7 9 11
# outputCopy
# 2 5 8
# 11 14 17


#!env/bin/user python3
import sys


r, c = map(int, sys.stdin.readline().split())
def sum_matrix(a, b, r, c):

    if r == 0:
        return

    sum_matrix(a, b, r - 1, c)

    for i in range(c):
        print(a[r - 1][i] + b[r - 1][i], end=" ")
    print()

a = []
b = []
for i in range(r):
    a.append(list(map(int, sys.stdin.readline().split())))
for i in range(r):
    b.append(list(map(int, sys.stdin.readline().split())))
sum_matrix(a, b, r, c)

