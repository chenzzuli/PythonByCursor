"""
高级数学运算模块
提供幂运算、平均值、阶乘、斐波那契数列等高级运算
"""


def power(x, y):
    """返回x的y次方"""
    return x ** y


def average(numbers):
    """返回一组数的平均值"""
    if not numbers:
        raise ValueError("输入的列表不能为空！")
    return sum(numbers) / len(numbers)


def factorial(n):
    """返回n的阶乘"""
    if n < 0:
        raise ValueError("负数没有阶乘！")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """返回斐波那契数列的第n个数"""
    if n < 0:
        raise ValueError("输入必须是非负整数！")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)