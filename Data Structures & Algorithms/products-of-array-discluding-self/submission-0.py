class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zerocount = 0
        prod = 1
        output = []

        for n in nums:
            if n == 0:
                zerocount += 1
            else:
                prod = prod*n
        
        if zerocount > 1:
            for i in range(len(nums)):
                output.append(0)
        elif zerocount == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(prod)
                else:
                    output.append(0)
        else:
            prod2 = prod/nums[0]
            output.append(int(prod2))
            for i in range(1, len(nums)):
                prod2 = (prod2/nums[i])*nums[i-1]
                output.append(int(prod2))
        
        return output



        