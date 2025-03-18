class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        charc = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in charc.values():
                stack.append(i)
            elif i in charc.keys():
                if not stack or charc[i] != stack.pop():
                    return False
        return not stack            
                