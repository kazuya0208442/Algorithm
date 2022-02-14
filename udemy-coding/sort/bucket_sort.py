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


def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers         # 1つに箱に入るサイズ

    buckets = [ [] for _ in range(len_numbers)]
    for num in numbers:
        i = num // size
        if i != len_numbers:
            buckets[i].append(num)
        else:
            buckets[len_numbers-1].append(num)

    for i in range(len_numbers):
        insertion_sort(buckets[i])

    result = []
    for i in range(len_numbers):
        result += buckets[i]

    return result

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100) for _ in range(5)]
    print(bucket_sort(nums))