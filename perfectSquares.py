import numpy
from math import inf

class Solution:
    def numSquares(self, n: int) -> int:
        target = n
        upper_bound = numpy.sqrt(target) # not sure if it will let me use that
        upper_bound = upper_bound.astype(int)

        total_dict = {}

        for i in range(upper_bound, 0, -1):
            sum = i * i
            total = 1
            for j in range(i, 0, -1):
                while j > 0:
                    while sum < target:
                        sum += j * j
                        total += 1
                    if sum > target:
                        if j > 0:
                            sum -= j * j
                            total -= 1
                            j -= 1
                        else:
                            break
                    if sum == target:
                        if i in total_dict:
                            if total < total_dict[i]:
                                total_dict[i] = total
                        else:
                            total_dict[i] = total
                        sum = i * i
                        total = 1
                        break

        # now we need to find the min item in the dict
        min_total = inf

        for item in total_dict:
            if total_dict[item] < min_total:
                min_total = total_dict[item]

        return min_total



if __name__ == "__main__":
    n = 43
    Solution().numSquares(n)