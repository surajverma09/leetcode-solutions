class Solution {
     public static  int evalRPN(String[] tokens) {
        
        Stack<Integer> stack = new Stack<>();

        for(String token : tokens){
            if(token.equals("*")){
                int x = stack.pop();
                int y = stack.pop();
                int mul = y * x;
                stack.push(mul);
            }
            else if(token.equals("-")){
                int x = stack.pop();
                int y = stack.pop();
                int sub = y - x;
                stack.push(sub);
            }
            else if(token.equals("+")){
                int x = stack.pop();
                int y = stack.pop();
                int add = y + x;
                stack.push(add);
            }
            else if(token.equals("/")){
                int x = stack.pop();
                int y = stack.pop();
                int div = y / x;
                stack.push(div);
            }
            else{
                stack.push(Integer.parseInt(token));
            }
        }return stack.pop();
    }
}