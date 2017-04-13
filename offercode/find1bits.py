class Solution(object):
    def find1bits_postiveint( num ):
        if num < 0:
            return 0
        count = 0
        while num != 0:
            count += num & 1
            num = num >> 1
        return count

    def find1bits_int( num ):
        count = 0
        flag = 1
        while flag <= pow(2, 64) - 1:
            if (num & flag) != 0:
                count += 1
            flag = flag << 1
        return count

    def is2power( num ):
        return (num & num - 1) == 0

    # print find1bits_postiveint( 100 )
    # print is2power( 1023 )
    # print find1bits_int( pow(2, 63) )