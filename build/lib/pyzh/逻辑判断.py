# -*- coding: utf-8 -*-
"""
逻辑判断 - Python逻辑判断函数的中文封装

all() & 全真()
any() & 任一真()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 全真(序列):
    """
    参数:
        序列 (sequence): 要判断的序列对象。
    示例:
        全真([True, True, True])  # 返回 True
    返回值:
        bool: 如果序列中所有元素都为真，返回True；否则返回False。空序列将返回True。
    """
    return all(序列)


def 任一真(序列):
    """
    参数:
        序列 (sequence): 要判断的序列对象。
    示例:
        任一真([False, True, False])  # 返回 True
    返回值:
        bool: 如果序列中存在任一真值元素，返回True；否则返回False。空序列将返回False。
    """
    return any(序列)