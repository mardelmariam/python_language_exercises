# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:50:53 2024

@author: mdelm
"""

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    else:
        
        if len(s)==2:
            return 0
        
        elif len(s)==3:
            if s[0]==s[1]:
                return 2
            elif s[0]==s[2]:
                return 1
            elif s[1]==s[2]:
                return 0
        
        else:
            """
            # 17.6 us
            for i in range(len(s)):
                s_test = ''.join((s[j]) for j in range(len(s)) if j!=i)
                if s_test == s_test[::-1]:
                    return i
            """
            #8.4us
            n = len(s)
            for i in range(n//2+1):
                if s[i] != s[n-1-i]:
                    if s[i] == s[n-2-i] and s[i+1] == s[n-3-i]:
                        return n-1-i
                    else:
                        return i
                
        
        return -1


#print(palindromeIndex("ab"))
#print('\n')
#print(palindromeIndex("baa"))
#print('\n')
#print(palindromeIndex("aaa"))
#print('\n')
#print(palindromeIndex("aaab"))
#print('\n')
#print(palindromeIndex("baaa"))
#print('\n')
print(palindromeIndex("aaaaba"))
print('\n')

