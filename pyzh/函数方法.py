# -*- coding: utf-8 -*-
"""
函数方法 - Python函数和方法的中文封装



作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""

from functools import reduce


def 匿名函数(表达式):
    """
    参数：
        表达式 (str): 包含参数和函数体的字符串，格式为"参数:函数体"。
    示例：
        平方函数 = 匿名函数("x: x * x")
    返回值：
        function: 创建的匿名函数对象。
    """
    参数部分, 函数体 = 表达式.split(':', 1)
    return eval(f'lambda {参数部分}: {函数体}')


def 过滤(函数, 序列):
    """
    参数：
        函数 (function): 一个返回布尔值的函数。
        序列 (sequence): 要过滤的序列。
    示例：
        偶数 = list(过滤(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))  # 返回 [2, 4, 6]
    返回值：
        filter: 一个迭代器，包含所有使函数返回True的元素。
    """
    return filter(函数, 序列)


def 映射(函数, *序列):
    """
    参数：
        函数 (function): 要应用的函数。
        *序列 (sequence): 一个或多个序列。
    示例：
        平方数 = list(映射(lambda x: x * x, [1, 2, 3, 4]))  # 返回 [1, 4, 9, 16]
    返回值：
        map: 一个迭代器，包含函数应用的结果。
    """
    return map(函数, *序列)


def 累积运算(函数, 序列, 初始值=None):
    """
    参数:
        函数 (function): 一个接收两个参数的函数。
        序列 (sequence): 要进行累积运算的序列。
        初始值 (any, optional): 累积运算的初始值，默认为None。
    示例:
        总和 = 累积运算(lambda x, y: x + y, [1, 2, 3, 4, 5])
    返回值:
        any: 累积运算的结果。
    """
    if 初始值 is not None:
        return reduce(函数, 序列, 初始值)
    return reduce(函数, 序列)