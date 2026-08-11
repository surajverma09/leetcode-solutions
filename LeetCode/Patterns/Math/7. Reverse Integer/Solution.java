class Solution {
    public int reverse(int x) {
        int sign;
        if(x > 0){
            int sign = 1;
        }
        else{
            int sign = -1;
        }
        x = Math.abs(x);
        int rev = 0;

        while(x != 0){
            int last = x % 10;
            rev = rev * 10 + last;
            x = x / 10;
        }
    }return rev*sign;
}