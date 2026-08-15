class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        nums = "1234567890"
        result = 0
        for ch in operations:
            if ch == "C":
                stack.pop()
            elif ch == "+":
                stack.append(int(stack[-2]+stack[-1]))
            elif ch == "D":
                stack.append(int(stack[-1]*2))
            else:
                stack.append(int(ch))
        for i in stack:
            result = result + i
        return result
