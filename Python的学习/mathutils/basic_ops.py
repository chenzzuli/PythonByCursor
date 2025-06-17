"""
基础数学运算模块
提供加减乘除等基本运算
"""


def add(x, y):
    """返回两个数的和"""
    return x + y


def subtract(x, y):
    """返回两个数的差"""
    return x - y


def multiply(x, y):
    """返回两个数的积"""
    return x * y


def divide(x, y):
    """返回两个数的商"""
    if y == 0:
        raise ValueError("除数不能为零！")
    return x / y 