from stack import Stack


def is_brackets_balanced(test_str: str) -> bool:
    brackets_open = '([{'
    brackets_close = ')]}'
    brackets_map = {')': '(', ']': '[', '}': '{'}
    result = Stack()
    for letter in test_str:
        if letter in brackets_open:
            result.push(letter)
        elif letter in brackets_close:
            if not result.size():
                return False
            tmp_bracket = result.pop()
            if tmp_bracket != brackets_map.get(letter):
                return False
    return not result.size()


if __name__ == '__main__':

    while True:
        test_str = input('\nВведите последовательность скобок для проверки на сбалансированность или "q" для выхода: ')
        if test_str == 'q':
            break
        print('Сбалансировано' if is_brackets_balanced(test_str) else 'Неcбалансировано')
