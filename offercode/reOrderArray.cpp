//一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
class Solution {
public:
    void reOrderArray(vector<int> &vector1) {
        int oddCount = 0;
        for (int i = 0; i < vector1.size(); ++i) //先统计偶数个数
            if ((vector1[i]&0x1)==0)
                oddCount++;
        for (int i = 0; i < vector1.size() && oddCount>0;)//当遇到偶数，插入到尾部，i不动；基数i++
        {
            if(vector1[i]&0x1){
                ++i;
                continue;
            }
            oddCount--;
            int odd = vector1[i];
            int j = i+1;
            for (; j < vector1.size(); ++j)
            {
                vector1[j-1]=vector1[j];
            }
            vector1[j-1] = odd;
        }
    }
};