class Solution:
    def plusOne(self, digits):

        # Traverse from last digit
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0
            digits[i] = 0

        # If all digits were 9
        return [1] + digits
