class Solution:
    def checkStatus(self, a, b, flag):
        # Condition 1: Either a or b is non-negative (but not both) and flag is False
        if ((a >= 0 and b < 0) or (a < 0 and b >= 0)) and not flag:
            return True
        # Condition 2: Both a and b are negative and flag is True
        elif a < 0 and b < 0 and flag:
            return True
        else:
            return False

if __name__ == "__main__":
    a = int(input())  
    b = int(input())  
    flag = input().strip().lower() == 'true'
    solution = Solution()
    print(solution.checkStatus(a, b, flag))