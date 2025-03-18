# -*- coding: utf-8 -*-
"""
迭代生成 - Python迭代器与生成器功能的中文封装

iter() & 获取迭代器()
next() & 获取下一个()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 获取迭代器(可迭代对象, 哨兵=None):
    """
    参数:
        可迭代对象 (iterable): 任何可迭代的对象（如列表、元组、字符串等）。
        哨兵 (any, optional): 当迭代到某个值时停止，默认为None。
    示例:
        列表 = [1, 2, 3]
        迭代器 = 获取迭代器(列表)
    返回值:
        iterator: 返回一个迭代器对象。
    return iter(可迭代对象, 哨兵) if 哨兵 is not None else iter(可迭代对象)
    """
    return iter(可迭代对象, 哨兵) if 哨兵 is not None else iter(可迭代对象)



def 获取下一个(迭代器, 默认值=None):
    """
    参数:
        迭代器: 要获取下一个元素的迭代器。
        默认值: 当迭代器没有更多元素时返回的值（可选）。
    返回:
        迭代器的下一个元素。如果迭代器已经耗尽且指定了默认值，则返回默认值。
    示例:
        列表 = [1, 2, 3]
        迭代器 = 获取迭代器(列表)
        元素 = 获取下一个(迭代器)  # 1
        元素 = 获取下一个(迭代器)  # 2
    """
    try:
        return next(迭代器) if 默认值 is None else next(迭代器, 默认值)
    except StopIteration:
        if 默认值 is None:
            raise StopIteration("迭代器已经没有更多的元素")
        return 默认值


def 生成器返回(值):
    """
    参数:
        值 (any): 要返回的值。
    示例:
        列表 = [1, 2, 3]
        迭代器 = 获取迭代器(列表)
        for 元素 in 迭代器:
            生成器返回(元素)
    返回值:
        无。
    """
    yield 值