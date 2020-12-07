#la compléxité temporelle de cette solution est O(N*M^2) avec M l'element maximal dans A
#la compléxité spatialle de cette solution est O(N*M) avec M l'element maximal dans A



#le but est de chercher P la plus proches à S/2 avec S étant la somme des valeurs absolus des élements du tableau A
def solution(A):
    N = len(A)
    M = 0

    #Calcul de S et de M
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)

    #initialiser le nombre d'occurences de chaque élements dans A
    count = [0] * (M + 1)
    for i in range(N):
        count[A[i]] += 1

    #initialiser le tableau dp à -1
    #si dp[i]=-1 alors on ne peut pas atteindre la somme i
    #si dp[i]>=1 alors on peut atteindre la somme i
    #dp[i] contient combient on a de valeurs
    dp = [-1] * (S + 1)
    dp[0] = 0


    for a in range(1, M + 1):
        #laisser passer seulements les valeurs qui existent dans A
        if count[a] > 0:
            for j in range(S):
                #si on peut atteindre la somme j
                if dp[j] >= 0:
                    #on n'a pas besoin d'utiliser un nombre a 
                    #et donc on affecte à dp[i] le nombre d'occurence de a
                    dp[j] = count[a]
                #on n'a pas atteint la valeur i et que j'ai encore des a à utiliser
                elif (j >= a and dp[j - a] > 0):
                    #on utilise un a et donc on décrémente par 1
                    dp[j] = dp[j - a] - 1
    result = S
    for i in range(S // 2 + 1):
        #si on a pu atteindre cette valeur
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    return result

print(solution([1,5,2,-2]))