
#Factorial And Combinations
MOD = 10**9 + 7
def factorial(i):
    if i<=1:
        return i
    
    return factorial(i-1) * i  % MOD

def combination(n,r):
    
    factorial(n) * pow(factorial(n-r),-1,MOD) * pow(factorial(r),-1,MOD) % MOD

