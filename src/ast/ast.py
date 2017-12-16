# -*- coding:utf-8 -*-
"""

ast相关定义

"""
__date__ = "16/12/2017"
__author__ = "zhaojm"


class Node(object):
    """节点基类"""


class Expression(Node):
    """表达式基类"""


class Statement(Node):
    """语句基类"""


class Declaration(Node):
    """声明基类"""


class Ident(object):
    """标识符"""


