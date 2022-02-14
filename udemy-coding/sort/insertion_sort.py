from typing import List

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]        # iはtempのインデックスを決めるだけ。入れ替え操作はjでやる
        j = i - 1                # jはtempの1個前
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp
    
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100) for _ in range(5)]
    print(insertion_sort(nums))