def solution(number, limit, power):
    ans = 0
    divisors = []
    
    def getDivisor(n):
        divisorsList = []
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                divisorsList.append(i) 
                if ( (i**2) != n) : 
                    divisorsList.append(n // i)
        divisorsList.sort()
        return len(divisorsList)

    for i in range(1, number+1):
        divisors.append(getDivisor(i)) 
    
    for i in range(len(divisors)):
        if (divisors[i]) > limit:
            ans += power
        else:
            ans += divisors[i]
            
    return ans    