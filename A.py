#!env/bin/user python3
import sys


n = int(sys.stdin.readline())


def print_lvr(n):
    if n == 0:
        return
    print("I love Recursion")
    print_lvr(n - 1)

print_lvr(n)
