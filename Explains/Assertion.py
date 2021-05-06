import unittest
import random
from unittest import skip
'''
断言常用的方法例子，更多其他的断言方法请参考python-unittest官方文档
'''


@skip
class Test(unittest.TestCase):  # 相等 assertEqual(a,b) a==b
    def setUp(self):
        self.number = 5

    def test_case(self):
        self.assertEqual(self.number, 5, msg='Your input is not 10')

    def tearDown(self):
        pass


@skip
class NotEqual(unittest.TestCase):  # 不相等
    def setUp(self) -> None:
        self.number = random.randint(1, 5)

    def test_case(self):
        self.assertNotEqual(self.number, 6)

    def tearDown(self) -> None:
        pass


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@skip
class AssertTrue(unittest.TestCase):    # 是

    def setUp(self):
        print('开始测试')

    def test_case(self):
        self.assertTrue(is_prime(7), msg='Is not prime')

    def tearDown(self):
        print('测试结束')


@skip
class AssertFalse(unittest.TestCase):   # 否
    def setUp(self):
        print('测试开始')

    def test_case(self):
        self.assertFalse(is_prime(9), msg='是素数')

    def tearDown(self):
        print('测试结束')


@skip
class AssertIn(unittest.TestCase):  # 包含
    def setUp(self) -> None:
        print('测试开始')

    def test_case(self):
        a = 'he'
        b = 'hello'
        self.assertIn(a, b, msg='a is not in b')

    def tearDown(self) -> None:
        print('测试结束')


class AssertNotIn(unittest.TestCase):   # 不包含
    def setUp(self) -> None:
        print('测试开始')

    def test_case(self):
        a = 'hello'
        b = 'he'
        self.assertNotIn(a, b, msg='a is in b')

    def tearDown(self) -> None:
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
