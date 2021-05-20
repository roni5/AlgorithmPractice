def subsets(self, nums: List[int]) -> List[List[int]]:

    subsets = []

    self.dfs([], subsets, nums, 0)

    return subsets

def dfs(self, subset, subsets, nums, i):

    subsets.append(subset)

    for idx in range(i, len(nums)):
        self.dfs(subset + [nums[idx]], subsets, nums, idx + 1)