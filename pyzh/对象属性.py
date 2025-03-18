# -*- coding: utf-8 -*-
"""
对象属性 - Python对象属性操作函数的中文封装

delattr() & 删除属性()
getattr() & 获取属性()
hasattr() & 是否有属性()
setattr() & 设置属性()
super()   & 父类()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 删除属性(对象, 属性名):
    """
    参数:
        对象 (object): 要操作的对象。
        属性名 (str): 要删除的属性名称。
    示例:
        删除属性(对象, '属性名')
    返回值:
        None: 该函数没有返回值。
    """
    return delattr(对象, 属性名)


def 获取属性(对象, 属性名, 默认值=None):
    """
    参数:
        对象 (object): 要操作的对象。
        属性名 (str): 要获取的属性名称。
        默认值 (any, optional): 如果属性不存在，返回的默认值，默认为None。
    示例:
        值 = 获取属性(对象, '属性名', '默认值')
    返回值:
        any: 属性的值，如果属性不存在且提供了默认值，则返回默认值。
    """
    return getattr(对象, 属性名, 默认值)


def 是否有属性(对象, 属性名):
    """
    参数:
        对象 (object): 要检查的对象。
        属性名 (str): 要检查的属性名称。
    示例:
        if 是否有属性(对象, '属性名'):
            print('对象有这个属性')
    返回值:
        bool: 如果对象有指定属性返回True，否则返回False。
    """
    return hasattr(对象, 属性名)


def 设置属性(对象, 属性名, 值):
    """
    参数:
        对象 (object): 要操作的对象。
        属性名 (str): 要设置的属性名称。
        值 (any): 要设置的属性值。
    示例:
        设置属性(对象, '属性名', 42)
    返回值:
        None: 该函数没有返回值。
    """
    return setattr(对象, 属性名, 值)


def 父类(当前类=None, 当前实例=None):
    """
    参数:
        当前类 (class, optional): 当前类，默认为None（自动获取）。
        当前实例 (object, optional): 当前实例，默认为None（自动获取）。
    示例:
        父类方法 = 父类().方法名
    返回值:
        super: 返回父类的代理对象。
    """
    import inspect
    if 当前类 is None or 当前实例 is None:
        frame = inspect.currentframe().f_back
        if 当前类 is None:
            当前类 = frame.f_locals.get('self').__class__
        if 当前实例 is None:
            当前实例 = frame.f_locals.get('self')
    return super(当前类, 当前实例)