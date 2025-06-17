"""
一个简单的计算器模块，提供基本的数学运算功能
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


def power(x, y):
    """返回x的y次方"""
    return x ** y


def average(numbers):
    """返回一组数的平均值"""
    if not numbers:
        raise ValueError("输入的列表不能为空！")
    return sum(numbers) / len(numbers)


# 当直接运行这个模块时会执行的代码
if __name__ == "__main__":
    # 测试代码
    print("测试加法:", add(5, 3))
    print("测试减法:", subtract(5, 3))
    print("测试乘法:", multiply(5, 3))
    print("测试除法:", divide(6, 2))
    print("测试乘方:", power(2, 3))
    print("测试平均值:", average([1, 2, 3, 4, 5])) 