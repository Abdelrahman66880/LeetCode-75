class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        if str1 + str2 != str2 + str1:
            return ""

        def get_gcd_string(s1, s2):
            len_gcd = gcd(len(s1), len(s2))
            return s1[:len_gcd]

        return get_gcd_string(str1, str2)
