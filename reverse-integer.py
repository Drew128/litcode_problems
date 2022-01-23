class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            answer = -int(str(-x)[::-1])
            if answer < -2147483647:
                return 0
            return answer
        else:
            answer = int(str(x)[::-1])
            if answer > 2147483647:
                return 0
            else:
                return answer
