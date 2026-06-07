class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            # Sort the word to create a key
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
