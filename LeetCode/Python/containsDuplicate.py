def containsDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for num in nums:
            if num in count:
                return True
            else:
                count.add(num)
        return False