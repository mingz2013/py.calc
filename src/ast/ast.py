# -*- coding:utf-8 -*-
"""

ast相关定义

"""
__date__ = "16/12/2017"
__author__ = "zhaojm"


class Node(object):
    """节点基类"""

    def execute(self):
        """exe"""


class Expression(Node):
    """表达式基类"""


class Root(Node):
    """root"""


class Number(Node):
    """number基类"""

    def __init__(self, num):
        self.value = num

    def execute(self):
        """exe"""
        return self.value

    def __str__(self):
        # return self.__class__.__name__ + '(' + str(self.execute()) + ')'
        return str({
            "name": self.__class__.__name__,
            "value": self.value
        })

    def __repr__(self):
        # return self.__class__.__name__ + '(' + repr(self.execute()) + ')'
        return repr({
            "name": self.__class__.__name__,
            "value": self.value
        })


class BinaryOperator(Node):
    """二元操作符"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        # return self.__class__.__name__ + '(' + str(self.left) + ',' + str(self.right) + ')'
        return str({
            "name": self.__class__.__name__,
            "left": self.left,
            "right": self.right
        })

    def __repr__(self):
        # return self.__class__.__name__ + '(' + repr(self.left) + ',' + repr(self.right) + ')'
        return repr({
            "name": self.__class__.__name__,
            "left": self.left,
            "right": self.right
        })


class Add(BinaryOperator):
    """add"""

    def execute(self):
        """exe"""
        return self.left.execute() + self.right.execute()


class Sub(BinaryOperator):
    """sub"""

    def execute(self):
        """exe"""
        return self.left.execute() - self.right.execute()


class Mul(BinaryOperator):
    """mul"""

    def execute(self):
        """exe"""
        return self.left.execute() * self.right.execute()


class Div(BinaryOperator):
    """div"""

    def execute(self):
        """exe"""
        return self.left.execute() / self.right.execute()
