class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(1,n-1):
            if nums[i-1]<nums[i]<nums[i+1]:
                ans+=1
        maxx=[0 for i in range(n)]
        minn=[0 for i in range(n)]
        M=nums[0]
        m=nums[-1]
        for i in range(1,n):
            maxx[i]=M
            M=max(M,nums[i])
        for i in range(n-2,-1,-1):
            minn[i]=m
            m=min(m,nums[i])
        for i in range(1,n-1):
            if maxx[i]<nums[i]<minn[i]:
                ans+=1
        return ans
