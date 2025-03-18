# -*- coding: utf-8 -*-
"""
类型转换 - Python类型转换函数的中文封装

int()     & 转整数()
float()   & 转浮点数()
str()     & 转字符串()
list()    & 转列表()
tuple()   & 转元组()
set()     & 转集合()
dict()    & 转字典()
bool()    & 转布尔值()
complex() & 转复数()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""

def 转整数(对象, 进制=10):
    """
    参数：
        对象 (any): 要转换为整数的对象。
        进制 (int, optional): 如果对象是字符串，则表示字符串的进制，默认为10。
    示例：
        转整数("1010", 2)  # 返回 10（二进制1010转为十进制）
    返回值：
        int: 转换后的整数。
    """
    if isinstance(对象, str):
        return int(对象, 进制)
    return int(对象)


def 转浮点数(对象):
    """
    参数：
        对象 (any): 要转换为浮点数的对象。
    示例：
        转浮点数("3.14")  # 返回 3.14
        转浮点数(42)  # 返回 42.0
    返回值：
        float: 转换后的浮点数。
    """
    return float(对象)


def 转字符串(对象):
    """
    参数：
        对象 (any): 要转换为字符串的对象。
    示例：
        转字符串(42)  # 返回 "42"
        转字符串([1, 2, 3])  # 返回 "[1, 2, 3]"
    返回值：
        str: 转换后的字符串。
    """
    return str(对象)


def 转列表(可迭代对象=None):
    """
    参数：
        可迭代对象 (iterable, optional): 要转换为列表的可迭代对象，默认为None。
    示例：
        转列表([1, 2, 3])  # 返回 [1, 2, 3]
    返回值：
        list: 转换后的列表。
    """
    return list() if 可迭代对象 is None else list(可迭代对象)


def 转元组(可迭代对象=None):
    """
    参数：
        可迭代对象 (iterable, optional): 要转换为元组的可迭代对象，默认为None。
    示例：
        转元组([1, 2, 3])  # 返回 (1, 2, 3)
    返回值：
        tuple: 转换后的元组。
    """
    return tuple() if 可迭代对象 is None else tuple(可迭代对象)


def 转集合(可迭代对象=None):
    """
    参数：
        可迭代对象 (iterable, optional): 要转换为集合的可迭代对象，默认为None。
    示例：
        转集合([1, 2, 2, 3])  # 返回 {1, 2, 3}
    返回值：
        set: 转换后的集合。
    """
    return set() if 可迭代对象 is None else set(可迭代对象)


def 转字典(可迭代对象=None, **关键字参数):
    """
    参数：
        可迭代对象 (iterable, optional): 包含键值对的可迭代对象，默认为None。
        **关键字参数: 以关键字参数形式提供的键值对。
    示例：
        转字典([("a", 1), ("b", 2)])  # 返回 {"a": 1, "b": 2}
    返回值：
        dict: 转换后的字典。
    """
    if 可迭代对象 is None and not 关键字参数:
        return dict()
    elif 可迭代对象 is None:
        return dict(**关键字参数)
    else:
        return dict(可迭代对象, **关键字参数)


def 转布尔值(对象):
    """
    参数：
        对象 (any): 要转换为布尔值的对象。
    示例：
        转布尔值(1)  # 返回 True
    返回值：
        bool: 转换后的布尔值。
    """
    return bool(对象)


def 转复数(实部, 虚部=None):
    """
    参数：
        实部 (number/str): 复数的实部，或表示复数的字符串。
        虚部 (number, optional): 复数的虚部，当实部为字符串时忽略，默认为None。
    示例：
        转复数(3, 4)  # 返回 (3+4j)
    返回值：
        complex: 转换后的复数。
    """
    return complex(实部, 虚部)