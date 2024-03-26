def productExceptSelfPrePost(nums):
    pre = [1 for i in range(len(nums))]
    post = [1 for i in range(len(nums))]
    ans = [1 for i in range(len(nums))]
    n = len(nums)
    for i in range(n-1):
        pre[i+1]=pre[i]*nums[i]
    for i in range(n-1, 0 , -1):
        post[i-1]=post[i]*nums[i]
    
    for i in range(n):
        ans[i] = pre[i]*post[i]
    return ans

def productExceptSelfInPlace(nums):
    ans = [1 for i in range(len(nums))]
    pre=1
    for i in range(len(nums)):
        ans[i]=pre
        pre*=nums[i]
    post=1
    for i in range(len(nums)-1, -1, -1):
        ans[i]*=post
        post*=nums[i]
    return ans

if __name__ == '__main__':
    nums = [1,2,3,4]
    print('nums = [1,2,3,4]')
    print(productExceptSelfPrePost(nums))
    print(productExceptSelfInPlace(nums))
    nums = [-1,1,0,-3,3]
    print("nums = [-1,1,0,-3,3]")
    print(productExceptSelfPrePost(nums))
    print(productExceptSelfInPlace(nums))