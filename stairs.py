#Write a program that prints a staircase of size
# Input Format
#
# A single integer,n, denoting the size of the staircase.
#
# Output Format
#
# Print a staircase of size using # symbols and spaces.
#
# Note: The last line must have spaces in it.
#https://www.hackerrank.com/challenges/staircase/problem

def devins_stairs(n):
    print "\n".join([" "*(n - i - 1) + "#"*(i+1) for i in range(n)])

def anns_stairs(n):
    x = ""
    for i in range(n+1):
        print((n-i)*' ' + i*'#')
# AYE
anns_stairs(10)
