//给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
class Solution {
public:
    double Power(double base, int exponent) {
        double res = 1;
        if(abs(base) <= 0.000001)
            return 0;
        if (exponent<0)
            return Power(1/base, -exponent);
        else if(exponent==0)
            return 1;
        else{
            for (int i = 0; i < exponent; ++i)
            {
                res*=base;
            }
            return res;
        }
    }
};