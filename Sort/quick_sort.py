import sys
from typing import List
import random

# i は、pivot以下のindexを常に指している。
# _partition は、pivot よりも小さいほう大きいほうに分ける。
# _partition は、配列の大きさが2の時は、普通にsortされる。
# 配列の数が2の時 -> nums 本体がちゃんとsortされている。
# 分割して、小さくなったところからsortされて、本体も書き変わっていく。


def main(lines):
    numbers = list(map(int, lines[0].split()))
    # new_nums = [random.randint(0, 1000) for _ in range(100)]

    def _partition(nums: List[int], low: int, high: int) -> int:
        i = low - 1
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i+1], nums[high], = nums[high], nums[i+1]              # [4,1] の場合、i=-1, nums[high]=1なので、nums[i+1] = 4, nums[high] = 1 になり、入れ替わる。sort される。

        return i+1
    
    def _quick_sort(nums: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = _partition(nums, low, high)
            _quick_sort(nums, low, partition_index-1)
            _quick_sort(nums, partition_index + 1, high)
        
        # return nums
        
    _quick_sort(numbers, 0, len(numbers) - 1)
    # _quick_sort(new_nums, 0, len(new_nums) - 1)

    print(numbers)
    # print(new_nums)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)






