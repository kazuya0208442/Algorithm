from typing import List, NewType


IndexNum = NewType('IndexNum', int)

def linear_search(numbers: List[int], value: int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 10) for _ in range(10)]
    print(nums)
    print(linear_search(nums, 4))