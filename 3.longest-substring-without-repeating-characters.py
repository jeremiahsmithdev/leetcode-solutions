class Solution(object):


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subs = []
        sub = ''
        longest = 0
        for x in s:
            if x not in sub:
                sub += x
            else:

                if len(sub) > longest:
                    longest = len(sub)
                # subs.insert(0, sub)
                sub += x
                sub = sub[sub.index(x)+1:]

        if len(sub) > longest:
            longest = len(sub)
        # subs.insert(0, sub)
        # return len(max(subs, key=len))
        return longest
    #
    # print(lengthOfLongestSubstring(0, 'wpwwkews'))
