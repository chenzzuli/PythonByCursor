"""
数学工具包
包含基础运算和高级运算功能
"""

# 指定包的公共接口
__all__ = (
    'add', 'subtract', 'multiply', 'divide',
    'power', 'average', 'factorial', 'fibonacci'
)

# 导入子模块中的所有函数
from .basic_ops import add, subtract, multiply, divide
from .advanced_ops import power, average, factorial, fibonacci

# 版本信息
__version__ = "1.0.0"