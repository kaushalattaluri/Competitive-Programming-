class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        ans=0
        for i in op:
            if '++' in i:
                ans+=1
            else:
                ans-=1
        return ans
