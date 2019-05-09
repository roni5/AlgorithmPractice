 def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for number in nums:
            if number not in seen:
                seen[number] = 1
            else:
                seen[number] += 1
        for key, value in seen.iteritems():
            if value == 1:
                return key