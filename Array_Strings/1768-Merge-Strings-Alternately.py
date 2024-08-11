class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_str = ""
        min_len    = min(len(word1), len(word2)) 
        
        for i in range(min_len):
            merged_str += word1[i] + word2[i]

        final_result = merged_str + word1[i+1:] + word2[i+1:]

        return final_result