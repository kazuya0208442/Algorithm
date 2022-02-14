def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():    #条件節の中でもpop()発動して、リストから取り除ける。
                return False

    if stack:
        return False

    return True



def sample(numbers):
    for num in numbers:
        if num == numbers.pop():        # 条件節の中でもpop()発動して、リストから取り除ける。
            print("yeah")


if __name__ == '__main__':
    input = "{}[({})]"
    print(validate_format(input))

    numbers = [i for i in range(10)]
    print(sample(numbers))



