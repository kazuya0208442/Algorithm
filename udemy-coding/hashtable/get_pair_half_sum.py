from typing import List, Tuple, Optional


def get_pair_v1(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        cache.add(num)
        val = target - num
        if val in cache:
            return val, num      #同じ数が返されてしまうのであんまりよくない。先にcacheに入れてるからだね。


def get_pair_v2(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)           #改良版、cacheに入れるのを最後にした。


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    if sum_numbers % 2 != 0:
        return
    half_sum = int(sum_numbers / 2)

    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)




if __name__ == '__main__':
    nums = [11, 2, 5, 9, 10, 3]
    # print(get_pair_v2(nums, 18))
    print(get_pair_half_sum(nums))

