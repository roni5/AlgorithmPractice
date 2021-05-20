def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    res = []

    self.backtrack([], res, candidates, target, 0)

    return res

def backtrack(self, path, res, candidates, target, idx):

    if target == 0:
        res.append(path)
        return
    
    if target < 0:
        return
    
    for i in range(idx, len(candidates)):
        self.backtrack(path + [candidates[i]], res, candidates, target - candidates[i], i)
