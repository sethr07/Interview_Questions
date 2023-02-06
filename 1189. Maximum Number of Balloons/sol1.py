class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        c1 = Counter(text)
        count = 0

        while c1['b'] > 0 and c1['a'] > 0 and c1['l'] > 1 and c1['o'] > 1 and c1['n'] > 0:

              c1['b'] -= 1
              c1['a'] -= 1
              c1['l'] -= 2
              c1['o'] -= 2
              c1['n'] -= 1
              count += 1
        
        return count



