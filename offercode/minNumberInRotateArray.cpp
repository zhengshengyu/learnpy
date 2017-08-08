//数组{2,3,4,5,1,2,2,2,2,2,2}为{1,2,2,2,2,2,2,2,3,4,5}的一个旋转
class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        return binSearchMin(rotateArray, 0, rotateArray.size()-1);
    }
    int binSearchMin(vector<int> rotateArray, int begin, int end){
        if(rotateArray.empty() || begin > end)
            return 0;

        int mid = begin;
        while(rotateArray[begin] >= rotateArray[end]){
            if (end-begin ==1) //这个循环一定要加，不然跳不出while
            {
                mid = end;
                break;
            }
            mid = begin + (end-begin)/2;
            if(rotateArray[mid] == rotateArray[begin] && rotateArray[mid] == rotateArray[end])
            {
                int minVal = rotateArray[begin];
                for (int i = begin; i <= end; ++i)
                {
                    minVal = min(minVal,rotateArray[i]);
                }
                return minVal;
            }

            if(rotateArray[mid] >= rotateArray[begin])
                begin = mid;
            else if(rotateArray[mid] <= rotateArray[end])
                end = mid;
        }
        return rotateArray[mid];
    }
};