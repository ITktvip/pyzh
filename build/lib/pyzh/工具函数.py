# -*- coding: utf-8 -*-
"""
工具函数 - Python工具函数的中文封装

delattr()  & 删除对象()
eval()     & 求值()
abs()      & 绝对值()
callable() & 是否可调用()
id()       & 唯一标识()
globals()  & 获取全局符号表()
locals()   & 获取局部符号表()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""

# 导入其他模块中的函数，避免用户需要修改代码
from .数值运算 import 绝对值
from .对象类 import 可调用 as 是否可调用
from .对象类 import 唯一标识
from .对象类 import 全局符号 as 获取全局符号表
from .对象类 import 局部符号 as 获取局部符号表
from .编译执行 import 求值

# 从对象属性模块导入删除属性函数，并重命名为删除对象以保持兼容性
from .对象属性 import 删除属性 as 删除对象