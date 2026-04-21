class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        unresolvedTemps = []

        for idx, val in enumerate(temperatures):
            while(len(unresolvedTemps) > 0 and unresolvedTemps[-1][0] < val):
                daysUntilNextWarmDate = idx - unresolvedTemps[-1][1]
                result[unresolvedTemps[-1][1]] = daysUntilNextWarmDate
                unresolvedTemps.pop()
            unresolvedTemps.append([val,idx])
        
        # iterate through pending unresolved temps

        for temp in unresolvedTemps:
            result[temp[1]] = 0
        

        return result
        