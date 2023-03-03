# 2383. Minimum Hours of Training to Win a Competition

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        ene = initialEnergy
        exp = initialExperience
        n = len(energy)
        for i in range(n):
            print(ene,exp)
            if(ene <= energy[i]):
                res += (energy[i]-ene+1)
                ene = 1
            else:
                ene -= energy[i]
            if(exp <= experience[i]):
                res += (experience[i]-exp+1)
                exp = experience[i]+1
            exp += experience[i]
        return res
