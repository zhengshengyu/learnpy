class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) -1 , -1, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return nums
    def removeDuplicates2(self, nums):
        if nums == []:
            return 0
        start, end = 1, len(nums)
        keyValue = nums[0]
        for i in range(end):
            if keyValue != nums[i]:
                nums[start] = nums[i]
                keyValue = nums[i]
                start += 1
        return start
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums) -1 , -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return nums
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def getFirstOrderMap(nums):
            for i in range(len(nums)-1,0,-1):
                if nums[i] > nums[i-1]:
                    return True, i-1
            return False, 0
        
        if len(nums) <= 1:
            return nums
        res, indexA = getFirstOrderMap(nums)
        if res == False:
            nums = sorted(nums)
            return nums
        else:
            for i in range(len(nums) - 1, indexA, -1):
                if nums[i] > nums[indexA]:
                    indexB = i
                    nums[indexA], nums[indexB] = nums[indexB], nums[indexA]
                    for j in range(indexA + 1, (len(nums)+indexA)/2):
                        nums[j], nums[len(nums)+1 -j] = nums[len(nums)+1 -j], nums[j]
                    break
            return nums
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] <= 0:
                return 1
            elif nums[0] == 1:
                return 2
            else:
                return 1
        if nums.count(0) == 0:
            nums.append(0)
        sortNums = sorted(nums)
        missNum = 0
        for i in range(0, len(sortNums) - 1):
            if sortNums[i] >= 0 and sortNums[i+1] > sortNums[i] + 1:
                    missNum = sortNums[i] + 1
        if missNum == 0:
                missNum = sortNums[len(sortNums) -1] + 1
        return missNum
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        
        ## generate a n*n matrix
        matrix = [None]*n
        for i in range(len(matrix)):  
            matrix[i] = [0]*n

        rStart = 0
        rEnd = n - 1
        cStart = 0
        cEnd = n - 1
        rIndex = rStart
        cIndex = cStart
        numCount = 0
        while numCount < n*n:
            if rIndex == rStart and cIndex == cStart:
                print('111')
                if cStart == cEnd:
                    numCount += 1
                    matrix[rStart][cStart] = numCount
                    break
                else:
                    for j in xrange(cStart, cEnd):
                        numCount += 1
                        print(numCount)
                        matrix[rStart][j] = numCount
                    rIndex = rStart
                    cIndex = cEnd
            elif rIndex == rStart and cIndex == cEnd:
                print('222')
                for i in xrange(rStart, rEnd):
                    numCount += 1
                    print(numCount)
                    matrix[i][cEnd] = numCount
                rIndex = rEnd
                cIndex = cEnd
            elif rIndex == rEnd and cIndex == cEnd:
                print('333')
                for j in xrange(cEnd, cStart, -1):
                    numCount += 1
                    print(numCount)
                    matrix[rEnd][j] = numCount
                rIndex = rEnd
                cIndex = cStart
            elif rIndex == rEnd and cIndex == cStart:
                print('444')
                for i in xrange(rEnd, rStart, -1):
                    numCount += 1
                    print(numCount)
                    matrix[i][cStart] = numCount
                rStart += 1
                rEnd -= 1
                cStart += 1
                cEnd -= 1
                rIndex = rStart
                cIndex = cStart
        return matrix
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums.count(nums[i])>2:
                nums.remove(nums[i])
        return len(nums)
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zeroRows = {}
        zeroCols = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRows[i] = 0
                    zeroCols[j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zeroRows.has_key(i):
                    matrix[i][j] = 0
                elif zeroCols.has_key(j):
                    matrix[i][j] = 0
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                nums = [1,1]
                for j in range(1,i):
                    nums.insert(j, res[i-1][j] + res[i-1][j-1])
                res.append(nums)
        return res
    def generate2(self, numRows):
        """
            1 3 3 1 0 
         +  0 1 3 3 1
         =  1 4 6 4 1
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
            ## print(res)
        return res[:numRows]
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        import copy
        res = [1]
        for i in range(1, rowIndex):
            temp1 = copy.deepcopy(res)
            temp1.append(0)
            temp2 = copy.deepcopy(res)
            temp2.insert(0, 0)
            res = map(lambda x, y: x+y, temp1, temp2)
        return res
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        diffs = []
        for i in xrange(len(prices)-1):
            for j in xrange(i+1, len(prices)):
                diffs.append(prices[j] - prices[i])
        profits = filter(lambda x: x>0, diffs)
        if len(profits) == 0:
            return 0
        return max(profits)
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        maxProfit = 0
        for i in xrange(len(prices) - 1):
            for j in xrange(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit
    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, minPrice = 0, float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = set(nums)
        nums = sorted(nums)
        maxConLen = 0
        conLen = 1
        for i in xrange(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                conLen += 1
            else:
                maxConLen = max(maxConLen, conLen)
                conLen = 1
        return max(maxConLen, conLen)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
            if dic[num] > len(nums)/2:
                return num
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k <= 0 or k >= len(nums):
            return nums
        return nums[len(nums) - k:] + nums[:len(nums)]
nums = [2,2,2,4,4,5,5,5]
s = Solution()
print(s.rotate(nums, 0))