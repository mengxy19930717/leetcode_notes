
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_map1 = {}
        dict_map2 = {}
        for i in range(len(s)):
            if s[i] not in dict_map1:
                dict_map1[s[i]] = t[i]
            else:
                if dict_map1.get(s[i]) != t[i]:
                    return False
            if t[i] not in dict_map2:
                dict_map2[t[i]] = s[i]
            else:
                if dict_map2.get(t[i]) != s[i]:
                    return False
        return True






