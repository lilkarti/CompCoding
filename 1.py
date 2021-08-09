class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        print(nums)
        print(target)
        """
        
        prevmap = {} #vali:index
        
        #i = index 
        #n = list value^^^
        for i,n in enumerate(nums):
            #enumerate gives back 2 values i = index and n = value
            diff = target - n
                if(diff in prevmap)
                    return(prevmap[diff], i)
            prevmap[n] = i 
        return 
        
        
