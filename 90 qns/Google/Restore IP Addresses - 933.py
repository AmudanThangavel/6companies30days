class Solution:
    def restoreIpAddresses(self, s):
        result = []
        if len(s) > 12:
            return result

        def bact_trrack(i, dots, ip):
            if dots == 4 and i == len(s):
                result.append(ip[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, len(s))):
                temp = s[i:j+1]
                if int(temp) < 256 and str(int(temp)) == str(temp):
                    bact_trrack(j+1, dots+1, ip+s[i:j+1]+".")
        bact_trrack(0, 0, "")
        return result


obj = Solution()
testcases = ["25525511135", "0000", "101023"]
for test in testcases:
    print(obj.restoreIpAddresses(test))
