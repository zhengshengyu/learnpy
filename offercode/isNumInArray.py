import numpy as np

class Solution:
    # NO1: Find target in sequence array
    def FindSeries(self, target, series):
        ps = 0
        pe = len(series) - 1
        while ps <= pe:
            pm = (ps + pe) / 2
            if target > series[pm]:
                ps = pm
            elif target < series[pm]:
                pe = pm
            else:
                return True
        return False
    def Find(self, target, array):
        # write code here
        for row in range( len(array) - 1, -1, -1 ):
            if self.FindSeries( target, array[row][0:len(array[row])] ):
                return True
        return False

    def Find2(self, target, array):
        row = len(array) - 1
        col = 0
        while ( row >= 0 and col < len(array[row]) ):
            if array[row][col] > target:
                row -= 1
            elif array[row][col] < target:
                col += 1
            else:
                return True
        return False

    # NO2: Replace space with %20(one character to three characters)
    def replaceSpace(self, s):
        spacecount = 0
        for i in range( len(s)-1, -1, -1 ):
            if s[i] == ' ':
                spacecount += 1
        if spacecount == 0:
            return s
        oldp = len(s) - 1
        newp = oldp + 2*spacecount
        slist = [' ' for x in xrange(0, newp + 1)]
        print newp, len(slist)
        while oldp >= 0:
            if s[oldp] != ' ':
                slist[newp] = s[oldp]
                oldp -=1
                newp -=1
            else:
                for i in xrange(0, 3):
                    if i == 0:
                        slist[newp-i] = '0'
                    elif i == 1:
                        slist[newp-i] = '2'
                    elif i == 2:
                        slist[newp-i] = '%'
                newp -= 3
                oldp -= 1
        return slist

s = Solution()

# print s.Find( 7, np.array( [[1,2,3,4,5,6],[7,8,9,10,11,12]] ) )
strs = 'Hello kitty Hello Bank'

print s.replaceSpace( 'Hello kitty Hello Bank' )