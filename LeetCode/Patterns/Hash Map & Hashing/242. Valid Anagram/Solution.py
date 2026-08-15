class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dist = {}
        distt = {}
        i = 0
        j = 0

        if len(s) != len(t):
            return False

        while len(s)>i:
            if s[i] not in dist:
                dist[s[i]] = 1
            else:
                dist[s[i]] += 1
            i += 1

        while len(t)>j:
            if t[j] not in distt:
                distt[t[j]] = 1
            else:
                distt[t[j]] += 1
            j += 1
        
        return dist == distt