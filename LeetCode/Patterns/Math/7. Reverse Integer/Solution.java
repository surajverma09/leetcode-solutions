class Solution {
    public int reverse(int x) {
        int sign = 0;
        if(x > 2^31-1 || x < -(2^31)){
            return 0;
        }
        if(x > 0){
            sign = 1;
        }
        else{
            sign = -1;
        }
        x = Math.abs(x);
        int rev = 0;

        while(x != 0){
            int last = x % 10;
            rev = rev * 10 + last;
            x = x / 10;
        }return rev*sign;
}
    }