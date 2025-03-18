# -*- coding: utf-8 -*-
"""
编译执行 - Python编译与执行功能的中文封装

compile() & 编译()
exec()    & 执行()
eval()    & 求值()
globals() & 获取全局命名空间()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""


def 编译(源代码, 文件名='<string>', 模式='exec', 标志=0, dont_inherit=False, optimize=-1):
    """
    参数:
        源代码 (str): 要编译的源代码字符串。
        文件名 (str): 代码的文件名（用于错误消息），默认为'<string>'。
        模式 (str): 编译模式，可以是'exec'（语句序列）、'eval'（单个表达式）或'single'（单个交互式语句）。
        标志 (int): 编译器标志，默认为0。
        dont_inherit (bool): 是否不继承编译器标志，默认为False。
        optimize (int): 优化级别，默认为-1。
    示例:
        代码 = "x = 1 + 2"
        编译后代码 = 编译(代码)
    返回值:
        code: 编译后的代码对象。
    """
    return compile(源代码, 文件名, 模式, 标志, dont_inherit, optimize)


def 执行(代码, 全局命名空间=None, 局部命名空间=None):
    """
    参数:
        代码 (str/code): 要执行的Python代码（字符串或代码对象）。
        全局命名空间 (dict, 可选): 全局命名空间字典，默认为None。
        局部命名空间 (dict, 可选): 局部命名空间字典，默认为None。
    示例:
        执行('print("你好，世界!")')
        x = 1
        执行('y = x + 1', {'x': x})
    返回值:
        无返回值，直接执行代码。
    """
    return exec(代码, 全局命名空间, 局部命名空间)


def 求值(表达式, 全局命名空间=None, 局部命名空间=None):
    """
    参数:
        表达式 (str/code): 要计算的Python表达式（字符串或代码对象）。
        全局命名空间 (dict, 可选): 全局命名空间字典，默认为None。
        局部命名空间 (dict, 可选): 局部命名空间字典，默认为None。
    示例:
        结果 = 求值('1 + 2 * 3')
        print(结果)  # 输出：7
        x = 10
        结果 = 求值('x * 2', {'x': x})
        print(结果)  # 输出：20
    返回值:
        result: 表达式的计算结果。
    """
    return eval(表达式, 全局命名空间, 局部命名空间)


def 获取全局命名空间():
    """
    参数:无
    示例:
        全局变量 = 获取全局命名空间()
        print(全局变量.keys())
    返回值:
        dict: 包含全局变量的字典。
    """
    return globals()
