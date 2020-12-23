import pytest
from main import is_brackets_balanced

TEST_STR = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']


class TestMain:

    def test_is_brackets_balanced_0(self):
        assert is_brackets_balanced(TEST_STR[0])

    def test_is_brackets_balanced_1(self):
        assert is_brackets_balanced(TEST_STR[1])

    def test_is_brackets_balanced_2(self):
        assert is_brackets_balanced(TEST_STR[2])

    def test_is_brackets_balanced_3(self):
        assert not is_brackets_balanced(TEST_STR[3])

    def test_is_brackets_balanced_4(self):
        assert not is_brackets_balanced(TEST_STR[4])

    def test_is_brackets_balanced_5(self):
        assert not is_brackets_balanced(TEST_STR[5])
