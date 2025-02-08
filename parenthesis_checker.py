#to check the validation of the parenthesis of the code
class Solution(object):
    def isValid(self, s):
        a = list(s)
        i = 0
        while i < len(a) - 1:
            if (a[i] == "(" and a[i + 1] == ")") or (a[i] == "{" and a[i + 1] == "}") or (a[i] == "[" and a[i + 1] == "]"):
                a.pop(i)
                a.pop(i)
                i = 0
            else:
                i += 1
        return len(a) == 0
#({[]})
s = input()
sol = Solution()
print(sol.isValid(s))