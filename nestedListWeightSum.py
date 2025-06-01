
class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth = 1) -> int:
        ans = 0
        for ele in nestedList:
            if ele.isInteger():
                ans+=ele.getInteger()*depth
            else:
                ans+=self.depthSum(ele.getList(), depth+1)
            
        return ans
        # tc O(n) n=total nested elements
        