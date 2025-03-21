# -*- coding: utf-8 -*-
"""
异常处理 - Python 异常和错误处理的中文封装

raise()  & 引发异常()
assert() & 断言()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 引发异常(异常对象):
    """
    参数:
        异常对象: 要引发的异常对象，可以是异常类或异常实例。
    示例:
        引发异常(ValueError('无效的值'))
    返回值:
        无返回值，函数会终止当前执行并引发指定的异常。
    """
    raise 异常对象


def 断言(条件, 消息=None):
    """
    参数:
        条件: 要检查的条件，必须是一个布尔表达式。
        消息: 当断言失败时显示的错误消息，默认为None。
    示例:
        断言(x > 0, 'x必须大于0')
    返回值:
        无返回值，如果条件为假则引发AssertionError。
    """
    assert 条件, 消息