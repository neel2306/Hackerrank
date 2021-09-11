'''
TASK:
Complete the factorial function in the editor below. Be sure to use recursion.
'''
n = int(input())
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)
print(factorial(n))
