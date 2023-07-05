class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kel = celsius + 273.15
        ans.append(kel)
        fahr = (celsius * 1.8) + 32
        ans.append(fahr)
        return ans
