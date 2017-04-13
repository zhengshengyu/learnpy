import math
# print dir(math)
print math.fmod(2, 3)
class BitManipulationSolution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
        	result ^= x
        return result
    def singleNumberII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _result = 0
        _maxbits = 64
        for i in range(0, _maxbits):
        	_bitcount = 0
        	for x in nums:
        		if (x & (1<<i)) != 0:
        			_bitcount += 1
        	if math.fmod( _bitcount, 3 ) != 0:
        		_result |= (1<<i)
        return int(_result)

solution = BitManipulationSolution()
nums = range(1,10)
nums2 = range(1,10)
# list merge
nums.extend(nums)
nums.extend(nums2) # nums += nums
nums.append( 800 )
print solution.singleNumberII( [-2,-2,1,1,-3,1,-3,-3,-4,-2] )