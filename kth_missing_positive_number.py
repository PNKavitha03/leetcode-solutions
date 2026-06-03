class Solution:
    def findKthPositive(self, arr, k):
        missing = []
        num = 1
        i = 0

        while len(missing) < k:
            # If number is in array
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                missing.append(num)

            num += 1

        return missing[k - 1]
