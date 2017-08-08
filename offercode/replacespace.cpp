class Solution {
public:
    void replaceSpace(char *str,int length) {
        //length 完全可无视，全凭'\0'
        if(str==NULL || length<=0)
            return;
        int orilen=0;
        int spacecount=0;
        for(int i = 0; str[i]!='\0'; i++){
            orilen++;
            if(str[i]==' ')
                spacecount++;
        }
        //从'\0'开始
        for(int i = orilen, j=orilen+2*spacecount; i>=0; i--,j--){
            if(str[i]==' ')
            {
                str[j--]='0';
                str[j--]='2';
                str[j]='%';
            }
            else
            {
                str[j]=str[i];
            }
        }
    }
};