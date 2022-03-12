import sys
from typing import List
import random

def main(lines):
    numbers = list(map(int, lines[0].split()))
    # new_numbers = [random.randint(0, 100) for _ in range(100)]

    def _merge_sort(nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        center = len(nums) // 2
        left = nums[:center]
        right = nums[center:]

        _merge_sort(left)
        _merge_sort(right)          # この時点で、leftとrightは、sortされた状態で帰ってくる。return left(right) されているので、再帰関数が戻ってきたときには、left(right)書き変わる。

        i, j, k = 0, 0, 0
        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
        return nums
    
    print(_merge_sort(numbers))
    # print(_merge_sort(new_numbers))



if __name__ == '__main__':
    lines = []
    # original = []       # ['1 2 3 4 5\n']
    for l in sys.stdin:
        # original.append(l)
        lines.append(l.rstrip('\r\n'))
    # print(original)
    main(lines)

# if __name__ == '__main__':
#     lines = []
#     F = sys.stdin
#     lines.append(F.read().replace('\n', ''))
#     # lines.append(F.readline())
#     # lines.append(F.readline())
#     print(lines)
    