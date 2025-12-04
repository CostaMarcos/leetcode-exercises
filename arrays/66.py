class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # fazer tratamento para arr de tamanho 1

        rev = digits[::-1]

        carry = 1
        pos = 0

        while carry > 0:
            total = rev[pos] + carry

            if total > 9:
                rev[pos] = 0
                carry = total - 9
            else:
                rev[pos] = total
                carry = 0

            pos += 1

            if carry > 0 and pos == len(rev):
                rev.append(0)
        
        return rev[::-1]




a = Solution()
print(a.plusOne([1, 2, 3]))
print(a.plusOne([4,3,2,1]))
print(a.plusOne([9,9,9,9]))
print(a.plusOne([1,2,9,9]))
print(a.plusOne([1,9,9,9]))