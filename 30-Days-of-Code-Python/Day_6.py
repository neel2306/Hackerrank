'''
TASK:
Given a string, S, of length N that is indexed from  0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
'''
n = int(input())
for i in range(n):
    s = str(input())
    print(s[0::2] + " " + s[1::2])
