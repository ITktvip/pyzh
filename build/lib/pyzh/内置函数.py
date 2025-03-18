# -*- coding: utf-8 -*-
"""
内置函数 - Python内置函数的中文封装

print()     & 打印()
input()     & 输入()
len()       & 长度()
range()     & 范围()
type()      & 类型()
int()       & 整数()
float()     & 浮点数()
str()       & 字符串()
list()      & 列表()
tuple()     & 元组()
set()       & 集合()
dict()      & 字典()
max()       & 最大值()
min()       & 最小值()
sum()       & 总和()
sorted()    & 排序()
enumerate() & 枚举()
filter()    & 过滤()
map()       & 映射()
zip()       & 压缩()
any()       & 任意()
all()       & 全部()
abs()       & 绝对值()
round()     & 取整()
pow()       & 幂运算()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""

# 导入其他模块中的函数，避免用户需要修改代码
from .输入输出 import 打印, 输入
from .序列操作 import 长度
from .类型转换 import 转整数 as 整数, 转浮点数 as 浮点数, 转字符串 as 字符串
from .类型转换 import 转列表 as 列表, 转元组 as 元组, 转集合 as 集合, 转字典 as 字典
from .数值运算 import 绝对值, 四舍五入 as 取整, 幂运算, 最大值, 最小值, 求和 as 总和
from .序列操作 import 排序, 枚举
from .函数方法 import 过滤, 映射
from .逻辑判断 import 任一真 as 任意, 全真 as 全部
from .对象类 import 类型

# 基本函数
# 这些函数从其他专用模块导入，避免重复定义

def 范围(*参数):
    """
    参数:
        *参数: 范围参数，可以是(stop)或(start, stop)或(start, stop, step)。
    示例:
        for i in 范围(5):  # 返回 0, 1, 2, 3, 4
    返回值:
        range: 一个范围对象。
    """
    return range(*参数)

# 类型转换函数从类型转换模块导入

# 序列操作函数从序列操作模块导入

def 压缩(*可迭代对象):
    """
    参数:
        *可迭代对象: 要压缩的可迭代对象，可以是多个。
    示例:
        list(压缩([1, 2, 3], ['a', 'b', 'c']))  # 返回 [(1, 'a'), (2, 'b'), (3, 'c')]
    返回值:
        zip: 一个压缩后的迭代器对象。
    """
    return zip(*可迭代对象)

# 逻辑操作函数从逻辑判断模块导入

# 数学运算函数从数值运算模块导入