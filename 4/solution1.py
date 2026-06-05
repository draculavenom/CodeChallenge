strs = ["flower", "flow", "flight"]
#strs = ["dog", "racecar", "car"]
strs = ["flying", "fly"]

def longest_root():
    ans = strs[0]
    for s in strs[1:]:
        #print("word: " + s)
        for i in range(len(s)):
            #print("word: " + s[i])
            if len(ans) > i and s[i] != ans[i]:
                if i == 0:
                    return ""
                else:
                    ans = ans[0:i]
        if len(ans) > len(s):
            ans = ans[0:len(s)]
    return ans

print("the longest root is: " + longest_root())