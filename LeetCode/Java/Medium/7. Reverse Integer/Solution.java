class Solution {
    public int reverse(int x) {
        int sign = -1;
        int i = 0;
        x = math.abs(x);

        while(x.length()>i){
            int last = x / 10;
            int div = x % 10;
            int rev = rev * 10 + last;
        }
        if(x <0){
            return sign*rev;
        }
        else{
            return rev;
        }
    }
}