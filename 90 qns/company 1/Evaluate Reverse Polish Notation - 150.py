class Solution:
    def evalRPN(self, tokens):
        nums = []
        l = len(tokens)
        for i in range(l):
            if tokens[i] == "+":
                nums[-2] += nums[-1]
                nums.pop()
            elif tokens[i] == "-":
                nums[-2] -= nums[-1]
                nums.pop()
            elif tokens[i] == "*":
                nums[-2] *= nums[-1]
                nums.pop()
            elif tokens[i] == "/":
                nums[-2] /= nums[-1]
                nums[-2] = int(nums[-2])
                nums.pop()
            else:
                nums.append(int(tokens[i]))
        return nums[0]


obj = Solution()
testcases = [["2", "1", "+", "3", "*"], ["4", "13", "5", "/", "+"],
             ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
for t in testcases:
    print(obj.evalRPN(t))
