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


class File(Node):
    """root"""

    def __init__(self):
        self.statements = []  # 语句集合

    def __str__(self):
        # return self.__class__.__name__ + '(' + str(self.execute()) + ')'
        return str({
            "name": self.__class__.__name__,
            "statements": self.statements
        })

    def __repr__(self):
        # return self.__class__.__name__ + '(' + repr(self.execute()) + ')'
        return repr({
            "name": self.__class__.__name__,
            "statements": self.statements
        })

    def append_statements(self, statement):
        self.statements.append(statement)


class EndNode(Node):
    def __init__(self, pos, tok, lit):
        self.pos = pos
        self.tok = tok
        self.lit = lit

    def __str__(self):
        # return self.__class__.__name__ + '(' + str(self.execute()) + ')'
        return str({
            "name": self.__class__.__name__,
            "tok": self.tok,
            "pos": self.pos,
            "lit": self.lit
        })

    def __repr__(self):
        # return self.__class__.__name__ + '(' + repr(self.execute()) + ')'
        return repr({
            "name": self.__class__.__name__,
            "tok": self.tok,
            "pos": self.pos,
            "lit": self.lit
        })


class Number(EndNode):
    """number基类"""

    def execute(self):
        """exe"""
        return int(self.lit)


class Ident(EndNode):
    pass



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


class Assign(BinaryOperator):
    """赋值="""

    def execute(self):
        return Node
