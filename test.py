#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 07:49:06 2019

@author: heremias
"""

# =============================================================================
# def factori(n):
#      if n == 1:
#          return 1
#      return n * factori(n - 1)
#  
# print(factori(5))
# =============================================================================

# =============================================================================
# def iter_fact(n, a = 0, b = 1, p = []):
#     for c in range(n):
#         a, b = b, a + b 
#         if a > 1:
#             for i in range(2, a):
#                 if (a % i) == 0:
#                    print(a,"is the {}th fibonacci number and is not a prime number".format(c))
#                    print(i,"times",a//i,"is",a)
#                    break
#             else:
#                 p.append(a)
#                 print(a,"is a prime number and is the {}th fib number".format(c))
#     return p
#     
# 
# print(iter_fact(43))
# =============================================================================

#def memoize(f):
#    memo = {}
#    def helper(x):
#        if x not in memo:            
#            memo[x] = f(x)
#        return memo[x]
#    return helper
#    
#@memoize
#class f:
#    def fib(n):
#        if n == 0:
#            return 0
#        elif n == 1:
#            return 1
#        else:
#            f = fib(n-1) + fib(n-2)
#            return f
#
#n = 50
#v = f.fib
#v(50)
#if (v % i) == 0:
#    pass
#else:
#    print(v,"is a prime number" )

#for i in range(50):
#    print(fib(i))


#lower = 100
#upper = 2000
#for num in range(lower, upper + 1):
#   # order of number
#   order = len(str(num))
#    
#   # initialize sum
#   sum = 0
#   temp = num
#   while temp > 0:
#       digit = temp % 10
#       sum += digit ** order
#       temp //= 10
#   if num == sum:
#       print(num)
#  

l1 = [1,2,3,5,7,8,9,11,13,19]
l2 = [1,3,6,7,7,12,15,18,20,24,34]
l3 = [4,7,9,22,45,78]
nums = []
def merge_right(l1, l2):
    if len(l1) == 1 and len(l2) == 1:
        pass
    elif len(l1) == 1 and l1[0] > l2[0]:
        nums.append(l2[0])
        l2.remove(l2[0])
        pass
    elif len(l1) == 1 and l1[0] < l2[0]:
        nums.append(l1[0])
        nums.
        nums = nums + l2
        l1.remove(l1[0])
        pass
    elif len(l2) == 1 and l1[0] > l2[0]:
        nums.append(l2[0])
        nums = nums + l1
        l2.remove(l2[0])
        pass
    elif len(l2) == 1 and l1[0] < l2[0]:
        nums.append(l1[0])
        l1.remove(l1[0])
        pass
    elif l1[0] < l2[0]:
        nums.append(l1[0])
        l1.remove(l1[0])
        pass
    elif l2[0] < l1[0]:
        nums.append(l2[0])
        l2.remove(l2[0])
        pass
    elif l1[0] == l2[0]:
        nums.append(l1[0])
        l1.remove(l1[0])
        l2.remove(l2[0])
        pass
#    else:
#        nums.append(l2[0])
#        l2.remove(l2[0])
        
    
    
#    if l1[-1] < l2[-1]:
#        nums.append(l2[-1])
#        l2.remove(l2[-1])
#    elif l1[-1] > l2[-1]:
#        nums.append(l1[-1])
#        l1.remove(l1[-1])
    
    


for num in range(15):
    merge_right(l1,l2)
    print(nums)
    print(l1)
    print(l2)





    
    
    
    
    
    
    
    