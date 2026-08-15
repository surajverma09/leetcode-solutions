class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []
        stringgg = ''
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                num_stack.append(num)
                num = 0
                string_stack.append(ch)
            elif ch == "]":
                stringg = ""
                while string_stack[-1] != "[":
                    x = string_stack.pop()
                    stringg = x + stringg
                string_stack.pop()
                y = num_stack.pop()
                main_string = (int(y) * stringg)
                string_stack.append(main_string)
            else:
                string_stack.append(ch)
        
        for i in string_stack:
            stringgg = stringgg + i
        return stringgg
