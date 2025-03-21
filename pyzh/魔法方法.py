# -*- coding: utf-8 -*-
"""
魔法方法 - Python特殊方法的中文封装

__init__()     & 构造方法()
__del__()      & 析构方法()
__str__()      & 字符串表示()
__repr__()     & 表示方法()
__call__()     & 可调用对象()
__len__()      & 获取长度()
__getitem__()  & 获取元素()
__setitem__()  & 设置元素()
__delitem__()  & 删除元素()
__iter__()     & 获取迭代器()
__next__()     & 获取下一个元素()
__contains__() & 包含元素()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""

def 构造方法(类实例, *参数, **关键字参数):
    """
    参数:
        类实例 (object): 当前类实例。
        *参数: 位置参数。
        **关键字参数: 关键字参数。
    示例:
        构造方法(self, 参数1, 参数2, 关键字=值)
    返回值:
        None: 该函数没有返回值。
    """
    return object.__init__(类实例, *参数, **关键字参数)

def 析构方法(类实例):
    """
    参数:
        类实例 (object): 当前类实例。
    示例:
        析构方法(self)
    返回值:
        None: 该函数没有返回值。
    """
    return object.__del__(类实例)

def 字符串表示(类实例):
    """
    参数:
        类实例 (object): 当前类实例。
    示例:
        字符串表示(self)
    返回值:
        str: 对象的字符串表示。
    """
    return str(类实例)

def 表示方法(类实例):
    """表示方法的中文封装，对应__repr__
    
    参数:
        类实例: 当前类实例
        
    返回:
        对象的详细字符串表示
    """
    return repr(类实例)

def 可调用对象(类实例, *参数, **关键字参数):
    """可调用对象方法的中文封装，对应__call__
    
    参数:
        类实例: 当前类实例
        *参数: 位置参数
        **关键字参数: 关键字参数
        
    返回:
        调用结果
    """
    return 类实例.__call__(*参数, **关键字参数)

def 获取长度(类实例):
    """获取长度方法的中文封装，对应__len__
    
    参数:
        类实例: 当前类实例
        
    返回:
        对象的长度
    """
    return len(类实例)

def 获取元素(类实例, 键):
    """获取元素方法的中文封装，对应__getitem__
    
    参数:
        类实例: 当前类实例
        键: 索引或键值
        
    返回:
        指定位置的元素
    """
    return 类实例[键]

def 设置元素(类实例, 键, 值):
    """设置元素方法的中文封装，对应__setitem__
    
    参数:
        类实例: 当前类实例
        键: 索引或键值
        值: 要设置的值
    """
    类实例[键] = 值

def 删除元素(类实例, 键):
    """删除元素方法的中文封装，对应__delitem__
    
    参数:
        类实例: 当前类实例
        键: 要删除元素的索引或键值
    """
    del 类实例[键]

def 获取迭代器(类实例):
    """获取迭代器方法的中文封装，对应__iter__
    
    参数:
        类实例: 当前类实例
        
    返回:
        迭代器对象
    """
    return iter(类实例)

def 获取下一个元素(类实例):
    """获取下一个元素方法的中文封装，对应__next__
    
    参数:
        类实例: 当前类实例
        
    返回:
        序列中的下一个元素
        
    异常:
        如果没有更多元素，抛出StopIteration异常
    """
    return next(类实例)

def 包含元素(类实例, 元素):
    """包含元素判断方法的中文封装，对应__contains__
    
    参数:
        类实例: 当前类实例
        元素: 要判断的元素
        
    返回:
        如果元素在容器中返回True，否则返回False
    """
    return 元素 in 类实例