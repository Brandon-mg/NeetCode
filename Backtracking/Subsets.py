def subsets(nums):
    res=[]
    subset = []
    def dfs(i):
        if i>=len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)
    dfs(0)
    return res

if __name__ == "__main__":
    nums = [0,1,2]
    print("nums = [0,1,2]")
    print(subsets(nums))