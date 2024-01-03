#Required No. of Paranthesis
class Solution:
    def no_of_paranthesis(self, s):
        sc = so = co = cc = 0
        for char in s:
            match char:
                case '(':
                    so +=1
                    continue
                case ')':
                    sc +=1
                    continue
                case '{':
                    co +=1
                    continue
                case '}':
                    cc +=1
                    continue
        curly = co - cc if co > cc else cc - co
        small = so - sc if so > sc else sc - so

        return curly + small

obj = Solution()
result = obj.no_of_paranthesis("{(()}({)")
print(result)       