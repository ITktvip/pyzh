# -*- coding: utf-8 -*-
"""
序列操作 - Python序列操作函数的中文封装

len()       & 长度()
sorted()    & 排序()
reversed()  & 反转()
enumerate() & 枚举()
zip()       & 合并()
map()       & 显式映射()
filter()    & 过滤()
reduce()    & 累积运算()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""
from functools import reduce as _reduce


def 长度(序列):
    """
    参数：
        序列 (sequence): 要计算长度的序列对象。
    示例：
        长度('你好')  # 返回 2
    返回值：
        int: 序列的长度。
    """
    return len(序列)


def 排序(序列, *, 键=None, 反向=False):
    """
    参数：
        序列 (sequence): 要排序的序列。
        键 (function, optional): 排序依据的函数，默认为None。
        反向 (bool, optional): 是否反向排序，默认为False。
    示例：
        排序([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])  # 返回 [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    返回值：
        list: 排序后的新列表。
    """
    return sorted(序列, key=键, reverse=反向)


def 反转(序列):
    """
    参数：
        序列 (sequence): 要反转的序列。
    示例：
        list(反转([1, 2, 3]))  # 返回 [3, 2, 1]
    返回值：
        iterator: 反向迭代器对象。
    """
    return reversed(序列)


def 枚举(序列, 起始=0):
    """
    参数：
        序列 (sequence): 要枚举的序列。
        起始 (int, optional): 索引起始值，默认为0。
    示例：
        for 索引, 值 in 枚举(['a', 'b', 'c']):
            print(f'{索引}: {值}')
        # 输出:
        # 0: a
        # 1: b
        # 2: c
    返回值：
        enumerate: 枚举对象。
    """
    return enumerate(序列, 起始)


def 合并(*序列):
    """
    参数：
        *序列 (sequence): 要合并的序列，可以是多个。
    示例：
        list(合并([1, 2], ['a', 'b']))  # 返回 [(1, 'a'), (2, 'b')]
    返回值：
        iterator: 合并后的迭代器对象。
    """
    return zip(*序列)


def 显式映射(函数, *序列):
    """
    参数：
        函数 (function): 要应用的函数。
        *序列 (sequence): 要处理的序列，可以是多个。
    示例：
        list(显式映射(str.upper, ['a', 'b', 'c']))  # 返回 ['A', 'B', 'C']
    返回值：
        map: 映射对象。
    """
    return map(函数, *序列)


def 过滤(函数, 序列):
    """
    参数：
        函数 (function): 过滤函数，返回True保留元素，返回False过滤掉元素。
        序列 (sequence): 要过滤的序列。
    示例：
        list(过滤(lambda x: x > 0, [-1, 0, 1, 2]))  # 返回 [1, 2]
    返回值：
        filter: 过滤后的迭代器对象。
    """
    return filter(函数, 序列)


def 累积运算(函数, 序列, 初始值=None):
    """
    参数：
        函数 (function): 累积运算函数，接受两个参数。
        序列 (sequence): 要进行累积运算的序列。
        初始值 (any, optional): 累积运算的初始值，默认为None。
    示例：
        累积运算(lambda x, y: x + y, [1, 2, 3, 4])  # 返回 10
    返回值：
        any: 累积运算的结果。
    """
    if 初始值 is None:
        return _reduce(函数, 序列)
    return _reduce(函数, 序列, 初始值)