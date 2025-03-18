# -*- coding: utf-8 -*-
"""
对象类 - Python对象和类操作函数的中文封装

type()       & 类型()
isinstance() & 是实例()
issubclass() & 是子类()
object()     & 对象()
callable()   & 可调用()
id()         & 唯一标识()
globals()    & 全局符号()
locals()     & 局部符号()
dir()        & 属性列表()
vars()       & 属性字典()
help()       & 帮助()
repr()       & 字符串表示()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 类型(对象):
    """
    参数:
        对象 (any): 要获取类型的对象。
    示例:
        类型(42)  # 返回 <class 'int'>
    返回值:
        type: 对象的类型。
    """
    return type(对象)


def 是实例(对象, 类):
    """
    参数:
        对象: 要判断的对象。
        类: 类或类型对象，或者由类组成的元组。
    示例:
        是实例(42, int)  # 返回 True
    返回值:
        如果对象是指定类的实例，返回True；否则返回False。
    """
    return isinstance(对象, 类)


def 是子类(类1, 类2):
    """
    参数:
        类1: 潜在的子类。
        类2: 潜在的父类，或者由类组成的元组。
    示例:
        是子类(int, object)  # 返回 True
    返回值:
        如果类1是类2的子类，返回True；否则返回False。
    """
    return issubclass(类1, 类2)


def 对象():
    """
    示例:
        对象()  # 返回一个新的基础对象
    返回值:
        一个新的基础对象。
    """
    return object()


def 可调用(对象):
    """
    参数:
        对象: 要判断的对象。
    示例:
        可调用(类型)  # 返回 True
    返回值:
        如果对象可被调用，返回True；否则返回False。
    """
    return callable(对象)


def 唯一标识(对象):
    """
    参数:
        对象: 要获取标识符的对象。
    示例:
        唯一标识(42)  # 返回某个整数，如 4455324384
    返回值:
        对象的唯一标识符（整数）。
    """
    return id(对象)


def 全局符号():
    """
    示例:
        全局符号()  # 返回当前全局符号表的字典
    返回值:
        包含当前全局符号的字典。
    """
    return globals()


def 局部符号():
    """
    示例:
        局部符号()  # 返回当前局部符号表的字典
    返回值:
        包含当前局部符号的字典。
    """
    return locals()


def 属性列表(对象=None):
    """
    参数:
        对象: 要获取属性的对象。如果未提供，返回当前作用域的名称列表。
    示例:
        属性列表(42)  # 返回 ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', ...]
    返回值:
        对象的属性名称列表。
    """
    return dir(对象) if 对象 is not None else dir()


def 属性字典(对象=None):
    """
    参数:
        对象: 要获取属性的对象。如果未提供，返回当前局部作用域的属性字典。
    示例:
        属性字典(42)  # 返回 {'__class__': <class 'int'>, '__delattr__': <method-wrapper '__delattr__' of int object at 0x...>, ...}
    返回值:
        对象的属性字典。
    """
    return vars(对象) if 对象 is not None else vars()


def 帮助(对象=None):
    """
    参数:
        对象: 要获取帮助信息的对象。如果未提供，进入交互式帮助系统。
    示例:
        帮助(42)  # 打印 int 类的帮助信息
    返回值:
        无返回值，直接打印帮助信息。
    """
    return help(对象) if 对象 is not None else help()


def 字符串表示(对象):
    """
    参数:
        对象: 要获取字符串表示的对象。
    示例:
        字符串表示(42)  # 返回 '42'
    返回值:
        对象的字符串表示。
    """
    return repr(对象)
