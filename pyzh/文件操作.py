# -*- coding: utf-8 -*-
"""
文件操作 - Python文件操作函数的中文封装

open()     & 打开文件()
read()     & 读取文件()
write()    & 写入文件()
append()   & 追加文件()
readline() & 读取行()
mkdir()    & 创建目录()
remove()   & 删除文件()
rmdir()    & 删除目录()
rename()   & 重命名()
exists()   & 路径存在()
isfile()   & 是文件()
isdir()    & 是目录()

作者: [Tech#6]
版本: 0.0.1
许可证: MIT
"""

import os
import shutil

def 打开文件(文件路径, 模式='r', 编码=None):
    """打开文件 - open()的中文别名
    
    参数:
        文件路径: 要打开的文件路径
        模式: 打开模式，默认为'r'（只读）
        编码: 文件编码，默认为None
    
    返回:
        文件对象
    """
    return open(文件路径, mode=模式, encoding=编码)

def 读取文件(文件路径, 编码=None):
    """读取整个文件内容
    
    参数:
        文件路径: 要读取的文件路径
        编码: 文件编码，默认为None
    
    返回:
        文件内容字符串
        
    异常:
        如果文件不存在或无法读取，将引发相应的异常
    """
    try:
        with 打开文件(文件路径, 编码=编码) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {文件路径}")
    except PermissionError:
        raise PermissionError(f"无权限读取文件: {文件路径}")
    except Exception as e:
        raise Exception(f"读取文件时出错: {e}")

def 写入文件(文件路径, 内容, 编码=None):
    """写入内容到文件（覆盖原有内容）
    
    参数:
        文件路径: 要写入的文件路径
        内容: 要写入的内容
        编码: 文件编码，默认为None
        
    异常:
        如果文件无法写入，将引发相应的异常
    """
    try:
        with 打开文件(文件路径, 'w', 编码) as f:
            f.write(内容)
    except PermissionError:
        raise PermissionError(f"无权限写入文件: {文件路径}")
    except Exception as e:
        raise Exception(f"写入文件时出错: {e}")

def 追加文件(文件路径, 内容, 编码=None):
    """追加内容到文件末尾
    
    参数:
        文件路径: 要追加的文件路径
        内容: 要追加的内容
        编码: 文件编码，默认为None
    """
    with 打开文件(文件路径, 'a', 编码) as f:
        f.write(内容)

def 读取行(文件路径, 编码=None):
    """按行读取文件内容
    
    参数:
        文件路径: 要读取的文件路径
        编码: 文件编码，默认为None
    
    返回:
        文件行列表
    """
    with 打开文件(文件路径, 编码=编码) as f:
        return f.readlines()

def 创建目录(目录路径):
    """创建新目录
    
    参数:
        目录路径: 要创建的目录路径
    """
    os.makedirs(目录路径, exist_ok=True)

def 删除文件(文件路径):
    """删除文件
    
    参数:
        文件路径: 要删除的文件路径
        
    异常:
        如果文件不存在或无法删除，将引发相应的异常
    """
    try:
        if not 路径存在(文件路径):
            raise FileNotFoundError(f"要删除的文件不存在: {文件路径}")
        if not 是文件(文件路径):
            raise IsADirectoryError(f"指定的路径不是文件: {文件路径}")
        os.remove(文件路径)
    except PermissionError:
        raise PermissionError(f"无权限删除文件: {文件路径}")
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise Exception(f"删除文件时出错: {e}")

def 删除目录(目录路径):
    """删除目录及其内容
    
    参数:
        目录路径: 要删除的目录路径
    """
    shutil.rmtree(目录路径)

def 重命名(原路径, 新路径):
    """重命名文件或目录
    
    参数:
        原路径: 原始路径
        新路径: 新路径
    """
    os.rename(原路径, 新路径)

def 路径存在(路径):
    """检查路径是否存在
    
    参数:
        路径: 要检查的路径
    
    返回:
        布尔值，表示路径是否存在
    """
    return os.path.exists(路径)

def 是文件(路径):
    """检查是否为文件
    
    参数:
        路径: 要检查的路径
    
    返回:
        布尔值，表示是否为文件
    """
    return os.path.isfile(路径)

def 是目录(路径):
    """检查是否为目录
    
    参数:
        路径: 要检查的路径
    
    返回:
        布尔值，表示是否为目录
    """
    return os.path.isdir(路径)