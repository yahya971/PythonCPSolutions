# solution avec mod 2**p
# la compléxité spaciale et temporelle de cette solution est O(L)
# cette solution fournit le output indiqué dans l'énoncé

def solution(a,b):
    dp=[]
    dp= [0] * (len(a))
    dp[0]=1
    dp[1]=2
    for i in range(2,len(a)):
    	#on initialise les valeurs avec un modulo de 2**30 avec L=30
        dp[i]=(dp[i-1]+dp[i-2])& ((1 << 30) - 1)
    
    for i in range(len(a)):
    	#on utilise bitwise left shifting pour changer de modulo (de 2**30 à 2**b[i])
        a[i]=dp[a[i]-1]&((1<<b[i])-1)
    return a

print(solution([4,4,5,5,1],[3,2,4,3,1]))





#solution avec mod 2p 
#la compléxité spaciale et temporelle de cette solution est O(L)
#mais elle ne marche pas pour L assez grande (overflow exception)
import numpy as np
def solution1(a,b):
    dp=[]
    dp=[0] * (len(a))
    dp[0]=1
    dp[1]=2
    for i in range(2,len(a)):
        dp[i]=dp[i-1]+dp[i-2]
    
    for i in range(len(a)):
    	a[i]=dp[a[i]-1]%(2*b[i])
    return a

print(solution1([4,4,5,5,1],[3,2,4,3,1]))






