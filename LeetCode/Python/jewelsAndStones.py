class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        jewel = set()
        for j in J:
            jewel.add(j)

        for s in S:
            if s in jewel:
                ans += 1

        return ans
